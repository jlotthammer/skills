---
name: code-rigor-review
description: Use when reviewing a coherent software diff for architectural fidelity, interfaces, dataflow, ownership, lifetime, state, control flow, testing, failure semantics, scope, or maintainability after implementation is complete.
---

# Code Rigor Review

## Independent reconstruction

Do not adopt the implementer's framing as the review basis.

Establish the review basis from:

1. **Original requirement** — read the user's actual request and explicit constraints.
2. **Pre-change repository state** — identify the relevant owners, interfaces, callers, tests, configuration, persistence contracts, and behavior.
3. **Final diff** — read the implementation that changed those surfaces.

From those sources, independently establish:

- the required externally observable behavior;
- the existing architectural owner;
- the relevant invariants and contracts;
- the minimum surfaces the requirement must affect. A **surface** is anything a
  consumer can depend on: an interface, a schema, a persisted form, a wire
  format, or an error.

Treat implementer-authored plans, rationales, summaries, and completion claims as context, not evidence.

If the original requirement or meaningful pre-change state is unavailable, state that limitation. Do not substitute an implementation summary for missing evidence.

## Review

Compare the reconstructed obligations with the diff. The dimensions below apply
the sibling skill's Requirements section and Core invariants from the reviewer's
side.

1. **Goal fidelity** — establish whether the diff solves the requested problem rather than a nearby problem.
2. **Repository grounding** — establish whether the diff extends the repository's actual owners and conventions.
3. **Contract integrity** — identify whether affected surfaces use one canonical invariant or create local interpretations.
4. **Scope traceability** — identify the requirement that justifies each material change.
5. **Ownership and lifetime** — identify the owner and valid lifetime of changed mutable state, derived state, and resources.
6. **Dataflow** — trace changed boundaries, representations, materialization, persistence, and repeated work.
7. **Failure semantics** — identify where failures originate, where policy is applied, and whether fallback, coercion, retry, or suppression hides required failure information.
8. **Control flow** — identify whether changed branching, nesting, or state handling makes the normal path difficult to reconstruct. Do not require decomposition when the branching is intrinsic and the explicit form is clearer.
9. **Testing integrity** — establish whether changed or new tests protect the requirement or a durable invariant rather than the patch's internal decomposition.
10. **Proof obligations** — name each new mode, cache, state, representation, compatibility path, concurrency machinery, dependency, or lifecycle rule that must remain correct.
11. **Simplification** — identify any obligation or difficult control flow that can disappear by changing the owner, boundary, representation, state model, or path.

Report only specific, evidenced, actionable findings.

For each finding:

1. name the violated obligation or invariant;
2. name the repository evidence;
3. name the changed path;
4. identify the smallest owner-level correction.

**REQUIRED REFERENCE:** Before you report a finding, read `../code-rigor/references/evidence.md`.

The Directive vocabulary, Terms, and Requirements sections of `../code-rigor/SKILL.md` govern this skill.

For each finding, name the implementing line that makes the finding true and state what evidence would refute it.

Most review claims are exhaustiveness claims. One traced path does not establish “only,” “all,” or “the existing owner.” If you cannot establish how the behavior arises, report a question rather than a defect.

End with:

**goal fidelity: satisfied / partially satisfied / not established**

## Boundaries

Broad correctness, security, and ordinary regression review belong to the host's normal code-review process.

Pure deletion or YAGNI review can be handled by Ponytail when installed.

Do not duplicate those reviews unless the issue directly violates a Code Rigor obligation.

For deeper analysis, load the relevant sibling reference:

- evidence → `../code-rigor/references/evidence.md`
- interfaces → `../code-rigor/references/interfaces.md`
- dataflow and persistence → `../code-rigor/references/dataflow.md`
- state and lifetime → `../code-rigor/references/state-and-lifetime.md`
- failure handling → `../code-rigor/references/failure-semantics.md`
- control flow → `../code-rigor/references/control-flow.md`
- tests → `../code-rigor/references/testing.md`
- concurrency → `../code-rigor/references/concurrency.md`
- optimization → `../code-rigor/references/optimization.md`
- Python → `../code-rigor/references/python.md`
- PyTorch → `../code-rigor/references/pytorch.md`
