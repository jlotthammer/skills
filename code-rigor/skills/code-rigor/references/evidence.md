# Evidence

**Search locates candidates. It does not establish behavior.**

Before reporting a finding, name the line you read that makes it true.
Caller-side evidence never establishes callee behavior — go read the callee.

Most invariants in this skill are **exhaustiveness** claims: "the only writer",
"*the* existing owner", "this conversion is redundant". Sampling cannot support
"only". Enumerate every site, using a tool that resolves scope
(`find_referencing_symbols`, LSP `findReferences`, `ast-grep`) rather than text
matching.

**Cross-check the count; disagreement means tool failure, not absence.** Text
search over-matches, which is safe — you discard the noise. Semantic tools
under-match when the index is cold or the file sits outside the project, and
they return fewer results with no error, which is unsafe: absence looks proven.
If the semantic tool finds one reference and grep finds six, the tool is cold.

For a claim about why existing machinery is there — a retry, a lock, a copy —
the evidence is `git log -S <symbol>` and `git blame`: find the commit and the
failure it answered.

State what would refute the finding, then look for that. A single
canonicalization at a function's entry refutes "repeated internal defense".

If you did not confirm the mechanism, report a question rather than a defect.
Matching a symptom to an anti-pattern name is a hypothesis, not evidence.
