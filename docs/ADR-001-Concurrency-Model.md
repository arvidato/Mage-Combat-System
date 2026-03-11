# ADR-001: Concurrency Model

## Status
Accepted

## Context

The combat system must support concurrent spell execution. Multiple characters may cast spells simultaneously, which requires a controlled concurrency model.

To avoid uncontrolled thread creation, the system must use bounded concurrency.

## Decision

The system uses Python's ThreadPoolExecutor to manage concurrent spell execution.

A fixed number of worker threads process spell actions.

A shared MetricsRegistry object records statistics such as total spells cast.

To ensure thread safety, a lock is used when updating shared metrics.

## Consequences

Advantages:
- Controlled thread management
- Simple implementation
- Easy testing of concurrent behavior

Disadvantages:
- Slight overhead from thread management
- Requires synchronization for shared resources
