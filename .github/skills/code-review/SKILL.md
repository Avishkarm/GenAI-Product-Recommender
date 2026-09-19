# SKILL.md
# Enterprise Pull Request Review Skill for GitHub Copilot

## Purpose

This document defines how GitHub Copilot, Copilot Coding Agent, and AI reviewers should evaluate Pull Requests (PRs) in this repository.

The goal is to ensure:

- Business alignment
- Architectural consistency
- Requirement traceability
- Security compliance
- Scalability
- Testability
- AI-readability
- Production readiness

---

# Review Workflow

## Step 1: Understand Change Scope

Review:

- PR title
- PR description
- Linked Jira tickets
- Business requirements
- Changed files

Verify:

```text
Why is this change being made?
What business goal does it support?
What requirements are affected?
```

---

# Step 2: Requirements Traceability Review

## Validation Rules

Every requirement must trace to a business objective.

### Verify

```text
Business Goal ID exists
Requirement ID exists
Acceptance Criteria exists
```

### Example

```text
BG-001 → TDL-SR-001 → FR-001 → TC-001
```

---

## Findings Format

```text
Traceability Gap

Requirement FR-003 is not linked to a business objective.

Recommendation:
Add traceability to BG-001.
```

---

# Step 3: Functional Review

Verify:

```text
Requirements implemented
Acceptance criteria satisfied
Happy path covered
Failure path covered
Boundary conditions covered
```

### Review Questions

```text
Can the feature succeed?

Can the feature fail safely?

Are edge cases documented?
```

---

# Step 4: Architecture Review

## Verify

### Design Consistency

```text
Follows existing architecture
Respects service boundaries
Uses approved patterns
```

### Distributed Systems Review

Check:

```text
Event contracts defined
Retry strategy documented
Idempotency handled
Compensation flow defined
Eventual consistency explained
```

### Example Finding

```text
High Severity

Duplicate event handling not specified.

Recommendation:
Implement idempotency key validation.
```

---

# Step 5: API Review

Verify:

```text
Request schema defined
Response schema defined
Error contract defined
Versioning defined
```

### Example

```json
POST /tasks

Request:
{
  "title":"Task"
}
```

```json
Response:
{
  "taskId":"123"
}
```

---

# Step 6: NFR Review

## Performance

Verify measurable thresholds.

✅ Good

```text
Response Time ≤ 500ms P95
```

❌ Bad

```text
System should be fast
```

---

## Reliability

Verify:

```text
Availability
Error Rate
Recovery Targets
```

Examples:

```text
Availability ≥ 99.9%

Error Rate ≤ 0.1%

RTO ≤ 15 min
```

---

## Security

Verify:

```text
Authentication
Authorization
Encryption
Audit Logging
Secrets Handling
```

---

# Step 7: Testability Review

Verify:

```text
Acceptance Criteria present
Test Cases present
Expected Results present
```

### Minimum Requirement

Every feature must contain:

```text
1 Happy Path

1 Failure Scenario

1 Edge Case
```

---

# Step 8: AI Readability Review

## AI Parsability Checklist

Verify:

```text
Structured headings
Stable identifiers
JSON examples
API contracts
Requirement IDs
NFR IDs
```

---

## Reject If

```text
Ambiguous language

Missing IDs

Missing acceptance criteria

Unstructured text blocks
```

---

# Spec Quality Score

## Scoring Model

| Metric | Weight |
|----------|---------|
| Completeness | 30% |
| Testability | 25% |
| Traceability | 25% |
| AI Parsability | 20% |

---

## Score Bands

| Score | Outcome |
|---------|---------|
| 90-100 | Approve |
| 75-89 | Review Required |
| Below 75 | Request Changes |

---

# Anti-Pattern Detection

## Flag These Issues

### AP-001 Missing Traceability

Example:

```text
Requirement exists but no business goal.
```

---

### AP-002 Weak NFR

Example:

```text
System should be scalable.
```

Expected:

```text
Support 100,000 users.
```

---

### AP-003 Missing Failure Path

Example
