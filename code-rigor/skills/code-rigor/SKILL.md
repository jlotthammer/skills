---
name: code-rigor
description: Use when implementing, refactoring, debugging, or optimizing substantive software where architecture, interfaces, dataflow, state, control flow, testing, failure semantics, maintainability, or performance materially matter.
---

# Code Rigor

## Principle

Use the smallest architecture that makes the required behavior explicit.

Repository evidence outranks generic design instinct. Preserve or expand required behavior while you remove unnecessary concepts, execution paths, architectural paths, states, representations, transformations, and proof obligations.

A path or a diff is **substantive** when it changes behavior, a contract, ownership, a representation, a lifetime, or a failure mode. A rename, a comment, or a formatting change is not.

## Directive vocabulary

Use these verbs consistently:

- **Identify** — locate and name the relevant owner, caller, contract, path, state, representation, or boundary.
- **Establish** — confirm a claim from repository evidence.
- **Define** — specify behavior or a contract that the change must introduce.
- **Measure** — obtain quantitative evidence.
- **Verify** — confirm an expected property or behavior by execution or direct observation.
- **Remove** — delete existing machinery only after you establish that its requirement does not apply.
- **Do not** — prohibited unless the instruction gives an explicit exception.
- **Prefer** — use judgment because more than one option can be correct.

Do not use “check,” “consider,” or similar vague verbs when a more specific directive applies.

## Requirements

Most rules here permit an action "when a requirement needs it". A requirement is **stated**. It comes from the user, a specification, an existing public contract, a supported environment, or a measurement.

Do not infer a requirement. An unstated need is a proposal until someone states it. You cannot supply one on the repository's behalf.

When a decision needs a requirement that nobody has stated:

- If the decision is hard to reverse, or it changes a public contract, stop and
  ask one specific question. State the options and your recommendation.
- Otherwise take the smallest option that satisfies the known behavior, and state
  the assumption with the change.

A brainstorming or scoping skill, where the session has one, owns the questions that come before a plan exists. This section owns the requirement you find missing during implementation.

## Core invariants

1. **Repository grounding** — identify the existing owner, callers, contracts, and local conventions before you introduce architecture. Search can locate candidates. Read the implementation to establish behavior. See `references/evidence.md`.
2. **Canonical interface and source of truth** — one concept should normally have one owner, one normal architectural path, and one authoritative state. A second owner is acceptable only at a boundary the repository does not control, such as a copy held by an external system. Do not create parallel interfaces or sources of truth without a requirement. See `references/interfaces.md`.
3. **Ownership and lifetime** — assign mutable state, resources, and derived information to the scope that owns their validity and cleanup. See `references/state-and-lifetime.md`.
4. **Canonical dataflow** — normalize at real boundaries. Keep representations aligned with consumers. Remove unnecessary conversion, copying, materialization, serialization, and synchronization. See `references/dataflow.md`.
5. **Explicit failure semantics** — preserve precise failure information. Do not add fallback, coercion, retry, compatibility behavior, or suppression without a requirement that owns that policy. See `references/failure-semantics.md`.
6. **Locally comprehensible control flow** — keep the normal execution path visible. Minimize the conditions and states a reader must track at one time. Do not split cohesive logic only to reduce a complexity metric. See `references/control-flow.md`.
7. **Complexity must reduce a named obligation** — each new abstraction, state, cache, mode, dependency, fast path, or concurrency mechanism creates proof obligations. Add it only when it removes or satisfies a specific requirement.

For a substantive path, identify:

**OWNER → INTERFACE → LIFETIME → REPRESENTATION → WORK**

Then ask:

**Can the same required behavior exist with fewer concepts or obligations?**

## Change discipline

Use this order unless repository evidence requires a different one:

1. remove unnecessary machinery;
2. fix the existing owner;
3. strengthen the existing contract;
4. move normalization or derivation to the correct boundary or lifetime;
5. remove redundant work or representations;
6. add the smallest new mechanism that the requirement needs.

Do not create a second path to avoid repairing the first.

Before you remove existing copies, locks, retries, synchronization, compatibility handling, numerical stabilization, or caches, establish why the machinery exists. Existing machinery can encode a real constraint even when its purpose is not obvious from the current call site.

## Testing

Treat tests as production code. Protect durable behavior, contracts, invariants, and demonstrated regressions.

Do not protect helper names, internal call order, source layout, or historical cleanup decisions unless one of them is itself a durable contract.

When tests are materially added, removed, weakened, mocked, skipped, or made more tolerant, load `references/testing.md`.

## Completion

For a substantial coherent diff, invoke sibling `code-rigor-review` before you report architectural completion.

Broad correctness, security, and ordinary regression review remain the responsibility of the host's normal code-review process and repository tooling.

## References

Load only the references that apply to the change:

- `references/evidence.md` — establish behavior before you make claims; enumerate exhaustiveness claims; seek refutation.
- `references/interfaces.md` — API boundaries, ownership, genericity, compatibility, and abstraction quality.
- `references/dataflow.md` — representation flow, canonicalization, materialization, storage and I/O boundaries, and repeated work.
- `references/state-and-lifetime.md` — mutable and derived state, caches, resources, aliases, iterators, and invalidation.
- `references/failure-semantics.md` — errors, recovery, retries, fallbacks, coercion, and suppressions.
- `references/control-flow.md` — branching, nesting, state transitions, local readability, decomposition, and complexity-tool interpretation.
- `references/testing.md` — durable test contracts, regression tests, mocking, TDD, and implementation-pinning tests.
- `references/concurrency.md` — task, thread, and process ownership; cancellation; synchronization; resource lifetime.
- `references/optimization.md` — performance work ordered by elimination of work, lifetime, data movement, algorithmic cost, locality, and only then added machinery.
- `references/python.md` — optional Python-specific ownership, typing, iteration, import, and runtime concerns.
- `references/pytorch.md` — optional PyTorch-specific autograd, storage, device, module-state, and checkpoint concerns.
