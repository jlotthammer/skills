---
name: code-rigor
description: Use when implementing, refactoring, debugging, or optimizing software where architecture, interfaces, dataflow, state, control flow, testing, failure semantics, maintainability, or performance matter.
---

# Code Rigor

## Principle

Use the smallest architecture that makes the required behavior explicit.

Repository evidence outranks generic design instinct. Preserve or expand required behavior while you remove unnecessary concepts, execution paths, architectural paths, reachable states, representations, transformations, and proof obligations.

## Directive vocabulary

Use these verbs consistently:

- **Identify** — locate and name the relevant owner, caller, contract, path, state, representation, or boundary.
- **Establish** — confirm a claim from repository evidence. With a value or a condition as its object, the word keeps its ordinary sense: bring it into being at an owner.
- **Define** — specify behavior or a contract that the change must introduce.
- **Measure** — obtain quantitative evidence.
- **Verify** — confirm an expected property or behavior by execution or direct observation.
- **Remove** — delete existing machinery only after you establish that its requirement does not apply.
- **Do not** — prohibited unless the instruction gives an explicit exception.
- **Prefer** — use judgment because more than one option can be correct.

Do not use “check,” “consider,” or similar vague verbs when a more specific directive applies.

## Terms

These words mean the same thing in every file.

- **owner** — the single component responsible for a value, a resource, or a decision: its validity, its changes, and its cleanup.
- **boundary** — a point where responsibility changes: between owners, between outside the repository and inside it, or between memory and storage. A boundary is *owned* when code here decides what crosses it.
- **contract** — what a caller may rely on: preconditions, postconditions, the invariants maintained, and the failures the operation can produce.
- **interface** — the named operations and types through which callers reach a concept.
- **public** — a contract is public when a consumer you do not control depends on it. Treat another repository, a published package, a persisted format, a command line, or a network API as public unless you enumerate every consumer as `references/evidence.md` requires. A contract that is not public is internal.
- **lifetime** — the interval in which a value, a resource, or a derived result stays valid.
- **representation** — the concrete form a value takes at a point on a path: its type, shape, units, encoding, or layout.
- **canonical** — the single form or route that the repository agrees on. Every alternative is converted to it or justified by a requirement.
- **source of truth** — the one place where a concept's current value lives. Every other copy derives from it.
- **materialization** — a value computed and held in memory or storage, rather than derived where it is used.
- **machinery** — code that manages something rather than expressing the operation: a cache, a lock, a retry, a wrapper, a mode, a compatibility path.
- **durable** — a property that survives refactoring, because something outside the implementation depends on it.
- **concept** — one thing the system reasons about: an entity, an operation, or a rule that a reader would name once.
- **policy** — a decision about what the system does, as distinct from the code that carries it out: a default, a retry rule, a timeout, a device choice.
- **idempotent** — an operation that can run more than once with the same effect as running once.
- **work** — computation, allocation, I/O, copying, conversion, or synchronization that the machine performs.
- **path** — an *execution path* is a route through code; an *architectural path* is the way a concept is reached; a *data path* is the route a value takes from source to output. Qualify the word where the sense is not clear from context.
- **state** — mutable data with an owner and a lifetime. Where the word means a reachable condition of a state machine, the text says so.
- **proof obligation** — a condition that must stay true for the code to remain correct, and that someone must re-establish after every later change.
- **substantive** — a path or a diff is substantive when it changes behavior, a contract, ownership, a representation, a lifetime, or a failure mode. A rename of an internal symbol, a comment, or a formatting change is not.

**invariant** carries two senses. The numbered items under Core invariants are this skill's rules. Everywhere else an invariant is a condition that holds throughout a scope.

## Requirements

Most rules here permit an action "when a requirement needs it". A requirement is **stated**. It comes from the user, a specification, an existing public contract, an existing caller of, or the implementation behind, the surface the change touches, a supported environment (one the repository declares), or a measurement.

Do not infer a requirement. An unstated need is a proposal until someone states it.

When a decision needs a requirement that nobody has stated:

- Stop and ask one specific question when the decision changes a public contract,
  migrates persisted data, or has effects outside the repository. State the
  options and your recommendation.
- Otherwise take the smallest option that satisfies the known behavior, and state
  the assumption with the change.

A brainstorming skill, where present, owns pre-plan questions; this section owns the requirement found missing during implementation.

## Core invariants

1. **Repository grounding** — identify the existing owner, callers, contracts, and local conventions before you introduce architecture. Search can locate candidates. Read the implementation to establish behavior. See `references/evidence.md`.
2. **Canonical interface and source of truth** — one concept has one owner, one canonical interface, and one source of truth. A second owner is acceptable only at a boundary the repository does not control, such as a copy held by an external system. Do not create parallel interfaces or sources of truth without a requirement. See `references/interfaces.md`.
3. **Ownership and lifetime** — assign mutable state, resources, and derived information to the scope that owns their validity and cleanup. See `references/state-and-lifetime.md`.
4. **Canonical dataflow** — canonicalize at owned boundaries. Keep representations aligned with consumers. Remove unnecessary conversion, copying, materialization, serialization, and synchronization. See `references/dataflow.md`.
5. **Explicit failure semantics** — preserve precise failure information. Do not add fallback, coercion, retry, compatibility behavior, or suppression without a requirement that owns that policy. See `references/failure-semantics.md`.
6. **Locally comprehensible control flow** — keep the normal execution path visible. Minimize the conditions and states a reader must track at one time. Do not split cohesive logic only to reduce a complexity metric. See `references/control-flow.md`.
7. **Complexity must reduce a named obligation** — each new abstraction, state, cache, mode, dependency, fast path, or concurrency machinery creates proof obligations. Add it only when it removes or satisfies a specific requirement.

For a substantive change, identify:

**OWNER → INTERFACE → LIFETIME → REPRESENTATION → WORK**

Then ask:

**Can the same required behavior exist with fewer concepts or obligations?**

## Change discipline

Use this order unless repository evidence requires a different one:

1. remove unnecessary machinery;
2. fix the existing owner;
3. strengthen the existing contract;
4. move canonicalization or derivation to the correct boundary or lifetime;
5. remove redundant work or representations;
6. add the smallest new machinery that the requirement needs.

Do not create a second path to avoid repairing the first.

Before you remove existing copies, locks, retries, synchronization, compatibility handling, numerical stabilization, or caches, establish why the machinery exists. Where history does not name the requirement, establish from the current code that no requirement applies, with the enumeration `references/evidence.md` requires for a removal, and state that history was silent.

## Testing

Treat tests as production code. Protect durable behavior, contracts, invariants, and demonstrated regressions.

When a change adds, removes, weakens, mocks, skips, or loosens tests, load `references/testing.md`.

## Completion

For a substantive diff, invoke sibling `code-rigor-review` before you report the change complete.

Broad correctness, security, and ordinary regression review remain the responsibility of the host's normal code-review process and repository tooling.

## References

Load only the references that apply to the change. Invariants 1 to 6 name their own references; the rest are described here.

- `references/testing.md` — durable test contracts, regression tests, mocking, TDD, and implementation-pinning tests.
- `references/concurrency.md` — task, thread, and process ownership; cancellation; synchronization; resource lifetime.
- `references/optimization.md` — performance work ordered by elimination of work, lifetime, data movement, algorithmic cost, locality, and only then added machinery.
- `references/python.md` — optional Python-specific ownership, typing, iteration, import, and runtime concerns.
- `references/pytorch.md` — optional PyTorch-specific autograd, storage, device, module-state, and checkpoint concerns.
