# Evidence

**Search locates candidates. It does not establish behavior.**

## Establish a finding

Before you report a finding:

1. Identify the implementation that controls the behavior.
2. Read the implementing line or block.
3. State the claim that the implementation supports.
4. State what evidence would refute the claim.
5. Look for that refuting evidence.

Do not use caller-side evidence to establish callee behavior. Read the callee.

If you cannot establish the mechanism, report a question rather than a defect.

## Exhaustiveness claims

Treat words such as “only,” “all,” “the existing owner,” and “redundant” as exhaustiveness claims.

Do not establish an exhaustiveness claim from a sample.

Enumerate every relevant site with a scope-aware tool such as LSP `findReferences` or `ast-grep`.

Compare the enumeration against a text search.

If semantic search finds fewer sites than text search, treat the disagreement as a tool failure until you resolve it. A cold or incomplete index can return too few results without an error.

## Existing machinery

When you need to establish why existing machinery exists, inspect its history.

For a retry, lock, copy, compatibility path, cache, synchronization step, or similar mechanism:

1. use `git blame` to identify the change;
2. use `git log -S <symbol>` or the relevant history to find the introducing commit;
3. identify the requirement or failure that the change addressed.

Do not remove existing machinery only because its current purpose is not obvious.

## Refutation

Search for evidence that would make your claim false.

Examples:

- A canonicalization at function entry refutes “internal code repeatedly defends against flexible input.”
- A second real caller can refute “this generic interface has no requirement.”
- A mutation after cache construction can refute “this cached value is valid for the object lifetime.”

Matching a symptom to an anti-pattern name is a hypothesis. Establish the mechanism before you report it as a finding.
