# Dataflow

Trace substantive data paths as:

`source → validation/canonicalization → state/computation → persistence/output`

For each transition, identify:

- who owns the value after the transition;
- the representation the next consumer requires;
- each copy, allocation, materialization, serialization, synchronization, or device/domain transition;
- how long derived information remains valid;
- whether the next consumer immediately reconstructs another representation.

## Lifetime-aligned derivation

For derived information, identify all dependencies and the largest scope in which those dependencies remain invariant.

For structural derived data — an index, a mask, a mapping, parsed metadata, a layout, canonicalized configuration — compute the value at the earliest owned scope where all dependencies are known and remain valid. Leave a value that costs less to recompute than to carry at its point of use.

Derive early only when a named owner establishes the value and the reader can
reach that owner. Otherwise keep the condition local. See `control-flow.md`.

Do not cache mutable derived state unless you can identify its source of truth and invalidation rule. See `state-and-lifetime.md` when invalidation matters.

## Canonical boundaries

Accept flexible or untrusted forms at external boundaries only when the contract requires that flexibility.

At the owning boundary:

1. parse;
2. validate;
3. canonicalize.

After that boundary, internal code relies on the established representation.

Do not repeatedly defend against representations that the system itself controls.

## Materialization

Treat copies, conversions, serialization, indexing materialization, device or domain transitions, and I/O as work.

Add any of these only when a consumer, an ownership boundary, a persistence contract, or a measured performance requirement needs it.

Do not change representation only because a local helper prefers another form.

## Storage and persistence

Choose stored representation from the durable contract and the required access pattern.

Do not persist internal object structure unless that structure is itself part of the contract.

Do not choose a stored form that forces repeated expensive reconstruction when a durable canonical form can avoid it.

Identify what a reader observes when a write stops part way. Where a reader must
never observe a partial write, write to a temporary location and rename, or use
the transaction the store provides. Flush and sync the temporary file before the
rename where the data must survive a crash.

Do not treat a multi-step write as atomic because the steps are adjacent in the
source.

When you define a persisted form, define how a reader tells it apart from later forms. A reader rejects a form it does not support; it does not misread it.

## Bulk operations

For numerical or data-heavy paths, keep data in bulk form when that form directly expresses the computation.

Do not decompose bulk data into many per-element objects or scalar operations without an algorithmic or semantic requirement.

Do not create a very large intermediate only to remove an explicit loop. Compare total work, memory, and locality.

Do not perform per-element I/O, queries, or synchronization inside a loop when the boundary offers a bulk operation. One round trip per element is a data-path decision, not an optimization to defer.

## Audit

For each changed data path:

1. Identify where the canonical representation is established.
2. Identify the work performed at each transition.
3. Identify work that repeats although its inputs remain invariant at a larger lifetime.
4. Identify representations that exist only to satisfy an intermediate helper.
5. Identify whether moving a boundary can remove a representation, a transformation, a branch, or a duplicate source of truth.
