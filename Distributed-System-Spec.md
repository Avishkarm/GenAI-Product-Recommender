# ECOM-SR-015 Async Order Processing

## Metadata

| Field | Value |
|---------|---------|
| Requirement ID | ECOM-SR-015 |
| Business Goal | BR-002 Order Fulfillment |
| Priority | P0 |
| Version | 1.0.0 |

---

# Objective

Support asynchronous order processing across Order, Payment, Inventory, and Notification services.

---

# Architecture

```text
Customer
   |
   v
Order Service
   |
   +--> OrderCreated Event
             |
             +--> Payment Service
             +--> Inventory Service
             +--> Notification Service
```

---

# Event Contract

## OrderCreated

```json
{
  "eventId": "EVT-123",
  "orderId": "ORD-456",
  "customerId": "CUS-001",
  "timestamp": "2026-09-19T12:00:00Z"
}
```

---

# Happy Path

1. Customer submits order.
2. Order persisted.
3. OrderCreated event published.
4. Payment authorized.
5. Inventory reserved.
6. Confirmation sent.

Expected:

```text
Order Status = Confirmed
```

---

# Failure Modes

## Payment Failure

```text
Payment authorization fails
Order Status = PaymentFailed
Inventory reservation released
```

## Inventory Failure

```text
Inventory unavailable
Compensation event published
Payment voided
```

## Event Bus Failure

```text
Retry 5 times
Persist to Outbox
Background publisher retries
```

## Duplicate Event

```text
Validate eventId
Ignore duplicate
```

---

# Eventual Consistency

Consistency Window:

```text
≤ 10 seconds
```

SLO:

```text
99.9% orders synchronized within 10 seconds
```

---

# Non-Functional Requirements

## Performance

| ID | Requirement |
|------|-------------|
| NFR-PERF-001 | Order API P95 < 500ms |
| NFR-PERF-002 | Event Publish < 100ms |
| NFR-PERF-003 | Fulfillment < 10 sec |

## Reliability

| ID | Requirement |
|------|-------------|
| NFR-REL-001 | Event Delivery ≥ 99.99% |
| NFR-REL-002 | Duplicate Processing = 0 |

## Availability

| ID | Requirement |
|------|-------------|
| NFR-AVL-001 | Service Availability ≥ 99.95% |

## Security

| ID | Requirement |
|------|-------------|
| NFR-SEC-001 | Event Payload Encryption |
| NFR-SEC-002 | Mutual TLS |

---

# Test Cases

### TC-001

Valid order

Expected:

```text
Confirmed
```

### TC-002

Payment declined

Expected:

```text
PaymentFailed
```

### TC-003

Inventory unavailable

Expected:

```text
Compensation triggered
```

### TC-004

Duplicate event

Expected:

```text
Ignored
```