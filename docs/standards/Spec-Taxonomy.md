# Enterprise E-Commerce Specification Taxonomy

## Purpose

Provide a consistent structure for business, engineering, architecture, testing, and AI-generated specifications.

---

# Naming Convention

Format:

```text
<Domain>-<Type>-<Sequence>-<Capability>-v<Major>.<Minor>
```

Examples:

```text
ECOM-BR-001-CustomerAcquisition-v1.0
ECOM-SR-015-AsyncOrderProcessing-v1.2
ECOM-API-004-OrderService-v1.0
ECOM-NFR-003-PaymentLatency-v1.0
ECOM-ADR-007-EventDrivenCheckout-v2.0
```

---

# Spec Types

| Prefix | Meaning |
|----------|----------|
| BR | Business Requirement |
| SR | Software Requirement |
| API | API Specification |
| NFR | Non-Functional Requirement |
| EVT | Event Contract |
| ADR | Architecture Decision Record |
| TST | Test Specification |

---

# Versioning Scheme

| Version | Meaning |
|----------|---------|
| 1.0.0 | Initial Release |
| 1.1.0 | Enhancement |
| 1.1.1 | Clarification |
| 2.0.0 | Breaking Change |

---

# Folder Hierarchy

```text
specs/
├── business/
├── requirements/
├── api/
├── events/
├── architecture/
├── testing/
├── quality/
└── memory/
```

---

# Spec Quality Gates

Minimum quality score:

```text
90+ Approved
75-89 Review Required
<75 Rework Required
```

---

# Required Sections

Every spec must include:

- Metadata
- Business Goal
- User Story
- Functional Requirements
- Scenarios
- NFRs
- Acceptance Criteria
- Test Cases
- Traceability