# State and Lifetime

For each new or changed mutable value, identify:

- who can mutate it;
- who owns its lifetime;
- what other state it aliases or depends on;
- what operation ends its validity.

Apply this to shared mutable state, globals and singletons, hidden caches, closures over mutable values, caller-owned mutation, import or startup state, environment-dependent state, worker or process state, and resource handles.

## Copies and aliases

Add a copy only when it satisfies a known aliasing, mutation, isolation, or lifetime requirement.

A caller keeps ownership of a value it passes. Do not mutate it unless the contract names the mutation. Do not return a reference to state you own unless the contract names which side may mutate it.

Before you remove an existing copy, establish why it exists, and enumerate every reader of the shared value to establish that none depends on the copy's isolation.

## Derived state and caches

Before you retain a derived value, answer all of these questions:

1. What is the source of truth?
2. What dependencies determine the value?
3. What makes the value valid?
4. What invalidates it?
5. Who performs invalidation?
6. How long may the value live?
7. Is recomputation costly, by a measurement or by the cost structure?

If you cannot define invalidation for mutable dependencies, do not retain the derived value as a cache.

Where the dependencies remain invariant for a larger owned lifetime, `dataflow.md` owns the rule: derive the value once at that lifetime.

## Resources and iterators

For each resource, identify who creates it and who closes, cancels, joins, or releases it.

Do not hide resource creation inside a helper when doing so obscures cleanup ownership.

Apply this rule to sessions, files, processes, transactions, streams, temporary resources, tasks, and similar handles.

Treat one-shot iterators and generators as mutable state. Do not consume one for logging, validation, or inspection unless the operation owns that consumption or reconstructs the iterator.
