# Failure Semantics

**Do not convert precise failure into ambiguous state.**

Validate a requirement at the boundary that owns it. After that boundary, let internal code rely on the established contract.

Do not:

- replace an error with `None`, zero, an empty value, or a default unless the API contract defines that result;
- catch, log, and continue when the operation is required to succeed;
- retry unless you can identify a transient failure that the retry can resolve;
- coerce internal values “just in case” when the repository controls their representation;
- distribute compatibility fallbacks across internal code;
- add a suppression or weaken a check only to make the implementation pass.

Defaults, coercion, degradation, retry, and fallback can be correct product or runtime behavior.

When the requirement needs one of them:

1. define the policy at the layer that owns it;
2. preserve the original error context when it is needed for diagnosis;
3. keep the policy out of lower layers that do not own the decision.

Do not make downstream code infer whether an ambiguous value means success, absence, degradation, or failure.
