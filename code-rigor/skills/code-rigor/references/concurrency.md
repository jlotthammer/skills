# Concurrency

**Concurrency adds ownership, ordering, cancellation, synchronization, and failure obligations. Add it only for a concurrency requirement or a measured bottleneck.**

Before you add a task, thread, process, worker pool, queue, lock, or similar machinery, identify:

1. who creates and owns it;
2. who waits, joins, cancels, or shuts it down;
3. which state is shared;
4. how shared state is synchronized;
5. how failures reach the owner;
6. whether the work is idempotent;
7. which resources remain valid across concurrent lifetimes.

Do not create fire-and-forget work whose lifetime can exceed the owner that created it.

Do not perform blocking I/O or take a blocking lock on the thread that runs an `async` function or an event loop. Move it to an executor, or make the interface synchronous.

Where more than one lock exists, acquire them in one fixed order everywhere. Two paths that take the same locks in different orders can deadlock.

Do not hold a lock across I/O, a wait on another task, or a call into code you do not own. Compute under the lock; perform the work outside it.

For each task that can be cancelled, identify the state a cancellation leaves behind, and who restores it.

Give every queue a bound. An unbounded queue converts a rate mismatch into
unbounded memory growth, and it hides the mismatch until the process fails.

Define what happens when a bounded queue is full: the producer waits, the
producer fails, or the queue drops work. That choice is backpressure, and it
belongs to the requirement that owns throughput.

`failure-semantics.md` owns time limits for waits and what a caller does when one
expires.

Retries, queues, locks, worker pools, and background tasks create additional states that must remain correct during failure and shutdown.
