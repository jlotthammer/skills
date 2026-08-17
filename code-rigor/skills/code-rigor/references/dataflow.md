# Dataflow

**A well-architected path has clear producers, canonical representations, explicit boundaries, and consumers that do not repeatedly reinterpret the same information.**

Trace important paths as:

`source → validation/canonicalization → state/computation → persistence/output`

At each boundary ask:

- who owns the value now;
- which representation the consumer requires;
- whether a copy/allocation/materialization/serialization/synchronization occurs;
- how long derived information remains valid;
- whether the next consumer immediately reconstructs another form.

## Lifetime-aligned derivation

Compute derived information at the earliest scope where all dependencies are known and remain invariant. Repeatedly rebuilding stable indexes, masks, mappings, parsed metadata, layout, normalized configuration, or other structural data usually indicates misplaced ownership.

Do not cache mutable derived state without a clear source of truth and invalidation rule.

## Canonical boundaries

Accept flexible or untrusted forms at external boundaries when required. Parse, validate, and canonicalize there. Internal code should not repeatedly defend against representations the system itself controls.

## Materialization

Copies, conversions, serialization, indexing materialization, device/domain transitions, and I/O are real operations. They are justified when a consumer or ownership boundary requires them, not because a local helper finds another representation convenient.

## Storage and persistence

Choose stored form according to access patterns and durable contracts. Avoid persistence formats that unnecessarily expose unstable internal object structure or force repeated expensive reconstruction.

## Bulk computation

For numerical/data-heavy paths, preserve bulk representations when they express the computation directly. Do not decompose bulk data into object/scalar work without an algorithmic reason, but do not create enormous intermediates merely to eliminate loops.

## Audit

For a changed path ask:

1. Where is the canonical representation established?
2. What work occurs at each transition?
3. What is repeated although its inputs are invariant at a larger lifetime?
4. Can moving a boundary eliminate a representation, transformation, branch, or source of truth?
