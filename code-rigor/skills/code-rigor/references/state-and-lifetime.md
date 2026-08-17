# State and Lifetime

**Every mutable thing needs an owner. Every derived thing needs a validity interval.**

Scrutinize shared mutable state, globals/singletons, hidden caches, closures over mutable values, caller-owned mutation, import/startup side effects, long-lived references, environment-dependent state, worker/process state, and resource handles.

## Copies and aliases

Do not copy by reflex. A copy should correspond to a known aliasing, mutation, isolation, or lifetime requirement.

Demand a reason before adding a copy; demand evidence before removing an existing one.

## Derived state and caches

Before retaining derived state, answer:

1. What is the source of truth?
2. What makes this value valid?
3. What invalidates it?
4. Who performs invalidation?
5. How long may it live?
6. Is recomputation materially costly?

If invalidation is vague, the cache is unsafe state.

## Resources and iterators

Resource creation should imply clear cleanup/cancellation ownership. Avoid helpers that open sessions, files, processes, transactions, streams, or temporary resources while obscuring who closes them.

One-shot iterators and generators are stateful; consuming them for inspection or validation changes subsequent behavior unless explicitly reconstructed.
