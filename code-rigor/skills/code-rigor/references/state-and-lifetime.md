# State and Lifetime

**Every mutable value needs an owner. Every derived value needs a validity interval.**

For each new or changed mutable value, identify:

- who can mutate it;
- who owns its lifetime;
- what other state it aliases or depends on;
- what operation ends its validity.

Apply this to shared mutable state, globals and singletons, hidden caches, closures over mutable values, caller-owned mutation, import or startup state, environment-dependent state, worker or process state, and resource handles.

## Copies and aliases

Do not copy by reflex.

Add a copy only when it satisfies a known aliasing, mutation, isolation, or lifetime requirement.

Before you remove an existing copy, establish why it exists and verify that shared storage cannot change required behavior.

## Derived state and caches

Before you retain a derived value, answer all of these questions:

1. What is the source of truth?
2. What dependencies determine the value?
3. What makes the value valid?
4. What invalidates it?
5. Who performs invalidation?
6. How long may the value live?
7. Is recomputation materially costly?

If you cannot define invalidation for mutable dependencies, do not retain the derived value as a cache.

If the dependencies remain invariant for a larger owned lifetime, derive the value once at that lifetime instead of repeatedly rebuilding it.

## Resources and iterators

For each resource, identify who creates it and who closes, cancels, joins, or releases it.

Do not hide resource creation inside a helper when doing so obscures cleanup ownership.

Apply this rule to sessions, files, processes, transactions, streams, temporary resources, tasks, and similar handles.

Treat one-shot iterators and generators as mutable state. Consuming one for inspection or validation changes later behavior unless you explicitly reconstruct it.
