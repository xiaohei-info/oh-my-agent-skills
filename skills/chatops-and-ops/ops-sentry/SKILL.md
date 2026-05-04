---
name: ops-sentry
description: Build log monitoring systems that avoid duplicate alerts and false positives. Use when creating cron-based monitoring, log error tracking, or alert deduplication.
version: 1.0.0
metadata:
  hermes:
    tags: [monitoring, logs, alerts, cron, devops]
---

# Ops Sentry - Log Monitoring & Alerting

Pattern for building log monitoring systems that avoid duplicate alerts and false positives.

## When to Use

- Building a cron-based monitoring system that scans logs for errors
- Implementing alert deduplication across multiple log files
- Creating stateful alert tracking to avoid re-reporting known issues
- Checking service health before reporting connection errors

## Core Patterns

### 1. Issue Normalization

Dynamic content in log messages causes identical issues to have different signatures. Always normalize:

```python
def normalize_issue_text(text: str) -> str:
    normalized = text
    replacements = [
        # Request IDs are unique per request
        (r"\(request id: [^)]+\)", "(request id:<redacted>)"),
        (r"request id: [A-Za-z0-9_-]+", "request id:<redacted>"),
        # UUIDs are unique
        (r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", "<uuid>"),
        # Timestamps and counters
        (r"attempt=\d+/\d+", "attempt=<n>/<n>"),
        (r"instance-\d{6,}(?:-\d+)?", "instance-<id>"),
        # Retry counts
        (r"retry \d+/\d+", "retry <n>/<n>"),
    ]
    for pattern, repl in replacements:
        normalized = re.sub(pattern, repl, normalized, flags=re.IGNORECASE)
    return normalized.strip()
```

### 2. Signature Generation

Use normalized text for signatures so similar issues group together:

```python
def issue_signature(text: str, source: str) -> str:
    # Normalize first, then hash
    normalized = normalize_issue_text(text)
    content = f"{source}:{normalized}"
    return hashlib.sha256(content.encode()).hexdigest()[:16]
```

### 3. Aggregation Key

When collecting issues from multiple log files, use normalized text as the aggregation key:

```python
issues_by_key = defaultdict(list)
for entry in log_entries:
    key = normalize_issue_text(entry["text"])
    issues_by_key[key].append(entry)
```

### 4. Service State Checking

Before reporting connection errors, verify the service isn't actually running:

```python
def is_port_listening(port: int, host: str = "127.0.0.1") -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            return result == 0
    except Exception:
        return False

def should_report_connection_error(port: int, error_text: str) -> bool:
    # Only report if port is NOT listening (actual outage)
    if "connection refused" in error_text.lower():
        return not is_port_listening(port)
    return True  # Report other errors regardless
```

### 5. Recovery Marker Suppression

Connection errors are often transient. If the same component later logs a clear recovery marker, suppress the alert unless the recovery is older than the error.

Typical recovery markers:
- `Connected to daemon`
- `listening on`
- `ready`
- `health check passed`
- `reconnected`

```python
def last_marker_after(lines: list[dict], error_ts: datetime, markers: list[str]) -> bool:
    marker_set = tuple(m.lower() for m in markers)
    for line in reversed(lines):
        ts = line.get("ts")
        text = (line.get("text") or "").lower()
        if not ts or ts <= error_ts:
            continue
        if any(marker in text for marker in marker_set):
            return True
    return False

# Example: suppress stale hindsight connection errors if daemon reconnected later
if "127.0.0.1:9460" in issue_text and last_marker_after(
    log_lines,
    error_ts,
    ["connected to daemon", "hindsight initialized"],
):
    continue
```

This catches the common case where ops-sentry scans the latest error line, but a later log line already proves the service recovered.

### 5a. Service-Specific Health Probes

When monitoring one concrete subsystem (for example a Dockerized watcher/compiler), do not rely on generic log scraping alone. Add a dedicated collector that checks the real deployment artifacts in this order:

1. **Deployment exists** — compose file, service unit, binary path, or config file exists
2. **Runtime object exists** — container/unit/process is present
3. **Runtime state is healthy** — running vs exited/restarting, restart count, exit code, started_at
4. **Recent subsystem logs** — scan only a bounded recent window for `ERROR` or explicit failed-item markers
5. **Normalize one representative sample** — use the normalized first failing line as the signature anchor

Typical implementation pattern:

```python
def collect_service_issues() -> list[dict[str, str]]:
    if not COMPOSE_FILE.exists():
        return []  # service not deployed here

    issues = []
    if not CONFIG_FILE.exists():
        issues.append(issue("svc-config-missing", "P1", "system:svc:config", "service config missing", str(CONFIG_FILE)))

    # check runtime object
    # inspect state
    # scan bounded recent logs
    return issues
```

This avoids false negatives where the container is up but the workload inside is failing, and false positives where the service simply is not deployed on this machine.

### 5b. Verify Collectors Without Consuming Alert State

If ops-sentry uses a state file to suppress repeat alerts, verify new logic at the **collector function** level before triggering the full cron/script. Otherwise a manual end-to-end run may consume the issue into state and make follow-up checks ambiguous.

Preferred verification sequence:

1. syntax-check the script
2. import the module and call the new collector directly
3. confirm the returned issue list/signatures/details are correct
4. only then run the full script/cron once to verify integration and state writeback

```python
spec = importlib.util.spec_from_file_location("ops_sentry", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
print(mod.collect_service_issues())
```

### 5c. System Scheduler and DB-Backed Collect Monitoring Extensions

When extending ops-sentry for Hermes host health, keep these additions inside the same umbrella instead of creating separate micro-skills:

- **system cron / systemd timer health**
  - check `cron.service` or `crond.service`
  - inspect current-user crontab readability
  - inspect `/etc/crontab` and `/etc/cron.d/*` conservatively
  - use `systemctl list-timers --all` and inspect failed timer/service units
  - prefer deterministic state checks over speculative missed-run inference

- **DB-backed trading collect monitoring**
  - prefer the trading DuckDB `raw_feed` as primary truth instead of giant log scraping
  - inspect freshness, `items_count`, repeated errors, and source-group coverage
  - treat `items_count=0` on historically non-zero sources as suspicious
  - attach short log evidence only as secondary context

- **Telegram readability discipline**
  - group by severity first, then domain (`Collect`, `Hermes`, `System`, `Other`)
  - keep summary lines compact and card-like
  - do not let raw log fragments dominate the human-facing alert

### 6. State Tracking

Track reported issues to avoid re-alerting:

```python
STATE_PATH = HERMES_HOME / "run-state" / "ops-sentry-state.json"

def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"active_issue_signatures": [], "updated_at": None}

def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2))

def is_new_issue(signature: str, state: dict) -> bool:
    return signature not in state.get("active_issue_signatures", [])
```

### 6. Log Time Window

Only report issues from recent logs to avoid stale alerts:

```python
RECENT_LOG_WINDOW_MINUTES = 90

def is_recent(ts: datetime | None, now: datetime) -> bool:
    if not ts:
        return False
    age = (now - ts).total_seconds() / 60
    return age <= RECENT_LOG_WINDOW_MINUTES
```

### 6a. For Dockerized Watchers, Prefer `started_at` Over a Fixed Window

For long-lived containers that run watcher/compiler loops, a fixed lookback like `2h` or `4h` can keep resurfacing errors that were already resolved by a container restart or config change. When possible, use the container's current `started_at` timestamp as the lower bound for log scanning.

Pattern:

```python
def docker_log_cutoff(container_name: str, fallback_hours: int = 2) -> datetime:
    started_at = inspect_container_started_at(container_name)
    if started_at is not None:
        return started_at
    return datetime.now(timezone.utc) - timedelta(hours=fallback_hours)
```

Use this for service-specific collectors that read `docker logs`:
- if the container restarted after a fix, pre-restart errors should not keep the alert active
- keep a small fallback window only for cases where `started_at` cannot be read
- still normalize the first post-cutoff failing line for signature stability

This pattern is especially useful for `compile --watch` style services where operators often restart the container to apply config changes.

## Pitfalls

- **Do NOT use raw log text as signature** - Dynamic content causes duplicates
- **Do NOT skip service state check** - Connection errors may be stale (service recovered)
- **Do NOT report all log matches** - Filter by time window and state
- **Do NOT aggregate by source file** - Same issue appears in multiple logs (gateway + run_agent)

## Verification

After implementation:
1. Syntax-check the script/module
2. Call the new collector directly and inspect its raw returned issues
3. Run the full script manually and check output
4. Verify no duplicate issues in report
5. Verify resolved issues don't reappear (service running = no connection error)
6. Check state file contains expected signatures

## Example Output Format

```
## Active Issues (2)

### Issue 1: API Token Invalid
- Source: default profile
- Last Seen: 2025-01-13 22:53:47
- Occurrences: 3
- Sample: Context summary failed: 401 Invalid token (request id:<redacted>)

### Issue 2: Service Not Running
- Source: trading profile
- Last Seen: 2025-01-13 22:30:12
- Occurrences: 1
- Sample: Cannot connect to hindsight at localhost:9177
```

## Related

- `webhook-subscriptions` - For triggering agents on external events
- Cron jobs in Hermes - Use `hermes cron` to schedule monitoring runs