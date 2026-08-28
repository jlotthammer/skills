# Failure Semantics

**Do not convert precise failure into ambiguous state.**

Validate a requirement at the boundary that owns it. After that boundary, let internal code rely on the established contract.

Do not:

- replace an error with `None`, zero, an empty value, or a default unless the API contract defines that result;
- catch, log, and continue when the operation is required to succeed;
- retry unless you can identify a transient failure that the retry can resolve,
  and the operation is idempotent or the caller can tolerate repeated effects;
- coerce internal values “just in case” when the repository controls their representation;
- distribute compatibility fallbacks across internal code;
- add a suppression or weaken a check only to make the implementation pass.

Defaults, coercion, degradation, retry, and fallback can be correct product or runtime behavior.

When the requirement needs one of them:

1. define the policy at the owner of that decision;
2. preserve the original error context when it is needed for diagnosis;
3. keep the policy out of code on the other side of that owner's boundary.

Do not make downstream code infer whether an ambiguous value means success, absence, degradation, or failure.

## Runtime failure

The rules above concern a failure the code can observe. A dependency can also
fail by not answering, or by answering for only part of the work.

For each call that leaves the process, or that waits on another task, identify:

- the time limit after which the caller stops waiting;
- what the caller does when that limit expires;
- whether the operation is idempotent, and therefore safe to repeat;
- which work has already committed when the call fails part way.

Define a time limit for every wait that a remote system, a subprocess, or
another task can extend. A wait with no limit converts a slow dependency into a
stopped system.

Identify which operations continue when a dependency is unavailable, and which
cannot. Do not let one unavailable dependency stop work that does not need it.

Do not report a partial failure as a total failure when the completed work is
durable. State what completed.
