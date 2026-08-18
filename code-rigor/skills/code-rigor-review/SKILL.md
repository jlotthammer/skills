---
name: code-rigor-review
description: Use when reviewing a coherent software diff for architectural fidelity, interfaces, dataflow, ownership, lifetime, state, testing, failure semantics, scope, or maintainability after implementation is substantially complete.
---

# Code Rigor Review

## Independent reconstruction

Do not validate the implementer's own framing.

Establish the review basis from:

1. **Original requirement** — the user's actual request and explicit constraints.
2. **Pre-change repository state** — relevant owners, interfaces, callers, tests, configuration, persistence contracts, and behavior.
3. **Final diff** — the implementation being reviewed.

Independently derive the required externally observable behavior, existing architectural owner, relevant invariants/contracts, and minimum affected surfaces before relying on an implementer-authored plan, rationale, summary, or completion claim.

Treat implementer commentary as untrusted context, not evidence. If the original requirement or meaningful pre-change state is unavailable, state that limitation rather than substituting the summary.

## Review

Compare the reconstructed obligations with the diff:

1. **Goal fidelity** — did the change solve the requested problem rather than a nearby reframing?
2. **Repository grounding** — does it extend the repository's actual owners and conventions?
3. **Contract integrity** — do affected surfaces share one canonical invariant rather than local interpretations?
4. **Scope traceability** — can each material change be causally tied to the requirement?
5. **Ownership and lifetime** — are mutable/derived state and resources owned at valid scopes?
6. **Dataflow** — are boundaries, representations, materialization, persistence, and repeated work coherent?
7. **Failure semantics** — is failure explicit and owned rather than hidden by fallback/coercion/suppression?
8. **Testing integrity** — do changed/new tests protect the requirement or durable invariants rather than the patch's internals?
9. **Proof obligations** — what new modes, caches, states, representations, compatibility paths, concurrency, dependencies, or lifecycle rules must now remain correct?
10. **Simplification** — can any new obligation disappear by changing the owner, boundary, representation, or path?

Report only specific, evidenced, actionable findings. For each, identify the violated obligation/invariant, repository evidence, changed path, and smallest owner-level correction.

**REQUIRED REFERENCE:** Before reporting any finding, read `../code-rigor/references/evidence.md`. Name the line you read that makes the finding true, and state what would refute it. Most obligations above are exhaustiveness claims — one traced path does not establish "only". If the mechanism is unconfirmed, report a question rather than a defect.

End with **goal fidelity: satisfied / partially satisfied / not established**.

## Boundaries

Broad correctness, security, and ordinary regression review belong to the host's normal code-review process. Pure deletion/YAGNI review may be handled by Ponytail when installed. Do not duplicate those reviews unless the issue is directly tied to the architectural obligations above.

For deeper analysis, load the relevant sibling `code-rigor` reference:

- evidence → `../code-rigor/references/evidence.md`
- interfaces → `../code-rigor/references/interfaces.md`
- dataflow/persistence → `../code-rigor/references/dataflow.md`
- state/lifetime → `../code-rigor/references/state-and-lifetime.md`
- failure handling → `../code-rigor/references/failure-semantics.md`
- tests → `../code-rigor/references/testing.md`
- concurrency → `../code-rigor/references/concurrency.md`
- optimization → `../code-rigor/references/optimization.md`
- Python → `../code-rigor/references/python.md`
- PyTorch → `../code-rigor/references/pytorch.md`
