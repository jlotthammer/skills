# Failure Semantics

**Do not convert precise failure into ambiguous state.**

Prefer validating at the boundary that owns the requirement, then let internal code rely on the established contract.

Challenge:

- broad recovery returning `None`, zero, empty values, or defaults;
- catch/log/continue when the operation is actually required;
- retry without a modeled transient failure;
- deep coercion "just in case";
- compatibility fallbacks distributed through the system;
- suppressions or weakened checks added to accommodate the implementation.

Defaults, coercion, degradation, and retry can be correct when they are explicit product/runtime behavior. Keep them at the layer that owns that policy and preserve original error context where useful.
