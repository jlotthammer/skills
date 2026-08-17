---
name: code-rigor
description: Use when implementing, refactoring, debugging, or optimizing substantive software where architecture, interfaces, dataflow, state, testing, failure semantics, maintainability, or performance materially matter.
---

# Code Rigor

## Principle

Prefer the smallest architecture that makes the required behavior explicit.

Repository evidence outranks generic design instinct. Preserve or expand behavior while reducing concepts, paths, states, representations, transformations, and proof obligations.

## Core invariants

1. **Repository grounding** — find the existing owner, callers, contracts, and local conventions before introducing architecture.
2. **Canonical interface and source of truth** — one concept should normally have one owner, one normal path, and one authoritative state.
3. **Ownership and lifetime** — mutable state, resources, and derived information belong at the scope where their validity is clear.
4. **Canonical dataflow** — normalize at real boundaries, keep representations aligned with consumers, and avoid unnecessary conversion, copying, materialization, serialization, or synchronization.
5. **Explicit failure semantics** — preserve precise failure information; do not invent fallback, coercion, retry, or compatibility behavior without a real requirement.
6. **Complexity must reduce a named obligation** — new abstraction, state, cache, mode, dependency, fast path, or concurrency creates proof obligations and must pay for them.

For a substantive path, ask:

**OWNER → INTERFACE → LIFETIME → REPRESENTATION → WORK**

Then ask: **Can the same behavior be preserved with fewer concepts or obligations?**

## Change discipline

Prefer, in order:

1. remove unnecessary machinery;
2. fix the existing owner;
3. strengthen the existing contract;
4. move normalization or derivation to the correct boundary/lifetime;
5. eliminate redundant work or representations;
6. add the smallest new mechanism required.

Do not create a second path to avoid repairing the first.

Be skeptical when adding machinery and evidence-driven when removing existing machinery. Existing copies, locks, retries, synchronization, compatibility handling, numerical stabilization, or caches may encode real constraints; establish their semantics before deleting them.

## Testing

Tests are production code. Protect durable behavior, contracts, invariants, and demonstrated regressions—not helper names, internal call choreography, source layout, or historical cleanup decisions.

When tests are materially added, removed, weakened, mocked, skipped, or made more tolerant, load `references/testing.md`.

## Completion

For a substantial coherent diff, invoke sibling `code-rigor-review` before reporting architectural completion. Broad correctness, security, and ordinary regression review remain the responsibility of the host's normal code-review process and repository tooling.

## References

Load only references relevant to the change:

- `references/interfaces.md` — API boundaries, ownership, genericity, compatibility, and abstraction quality.
- `references/dataflow.md` — representation flow, canonicalization, materialization, storage/I/O boundaries, and repeated work.
- `references/state-and-lifetime.md` — mutable/derived state, caches, resources, aliases, iterators, and invalidation.
- `references/failure-semantics.md` — errors, recovery, retries, fallbacks, coercion, and suppressions.
- `references/testing.md` — durable test contracts, regression tests, mocking, TDD, and avoiding implementation-pinning tests.
- `references/concurrency.md` — task/thread/process ownership, cancellation, synchronization, and resource lifetime.
- `references/optimization.md` — performance work ordered by elimination of work, lifetime, data movement, algorithmic cost, locality, and only then added machinery.
- `references/python.md` — optional Python-specific ownership, typing, iteration, import, and runtime concerns.
- `references/pytorch.md` — optional PyTorch-specific autograd, storage, device, module-state, and checkpoint concerns.
