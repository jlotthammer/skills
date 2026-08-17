# Concurrency

**Concurrency introduces ownership, ordering, cancellation, and failure obligations. Add it only for a real concurrency requirement or measured bottleneck.**

Make explicit:

- who creates and owns tasks/threads/processes;
- who waits, joins, cancels, or shuts them down;
- which state is shared and how synchronization is enforced;
- how failures propagate;
- whether work can be repeated safely;
- which resources remain valid across concurrent lifetimes.

Avoid fire-and-forget work whose lifetime exceeds the owner that created it. Do not hide blocking I/O or synchronization behind an asynchronous interface.

Retries, queues, locks, worker pools, and background tasks are not free performance abstractions; each creates new states that must remain correct during failure and shutdown.
