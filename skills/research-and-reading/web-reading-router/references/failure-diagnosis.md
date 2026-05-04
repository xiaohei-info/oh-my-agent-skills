# Failure Diagnosis

Use this reference when a URL could not be read cleanly.

## Classify the failure

### 1. Empty or title-only extraction
Meaning:
- lightweight extraction saw the page shell but not the body

Best next step:
- try a second lightweight path
- then escalate to browser if the page likely needs rendering

### 2. Truncated or obviously partial content
Meaning:
- extraction worked, but not fully

Best next step:
- retry with browser if the page is JS-heavy
- otherwise try a lightweight external reader for public pages

### 3. Login wall
Meaning:
- content requires account state

Best next step:
- tell the user clearly
- ask for the smallest needed assist only if they want to continue

### 4. CAPTCHA / slider / anti-bot
Meaning:
- automation reached a challenge page, not the target content

Best next step:
- report the blocker exactly
- do not pretend the page was read
- ask for pasted text, screenshots, a mirror link, or user-completed verification

### 5. File misclassification
Meaning:
- the URL was treated like a webpage but is really a PDF, image, feed, or API payload

Best next step:
- switch to the correct file-specific analyzer

## User-facing rule

Always report:
- what path was tried
- what failed exactly
- what the best next move is

Avoid vague messages like “couldn’t read it” when the actual blocker is known.
