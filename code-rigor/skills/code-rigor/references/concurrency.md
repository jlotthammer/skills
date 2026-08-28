# Concurrency

**Concurrency adds ownership, ordering, cancellation, synchronization, and failure obligations. Add it only for a real concurrency requirement or a measured bottleneck.**

Before you add a task, thread, process, worker pool, queue, lock, or similar mechanism, identify:

1. who creates and owns it;
2. who waits, joins, cancels, or shuts it down;
3. which state is shared;
4. how shared state is synchronized;
5. how failures reach the owner;
6. whether work can be repeated safely;
7. which resources remain valid across concurrent lifetimes.

Do not create fire-and-forget work whose lifetime can exceed the owner that created it.

Do not hide blocking I/O or synchronization behind an asynchronous interface.

Retries, queues, locks, worker pools, and background tasks create additional states that must remain correct during failure and shutdown.

Add one only when the requirement or measurement justifies those additional obligations.
