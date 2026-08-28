# Evidence

**Search locates candidates. It does not establish behavior.**

Matching a symptom to an anti-pattern name is a hypothesis. Establish how the
behavior arises before you act on it or report it.

## Establish a claim

Before you act on a claim, or report one:

1. Identify the implementation that controls the behavior.
2. Read the implementing line or block.
3. State the claim that the implementation supports.
4. State what evidence would refute the claim.
5. Look for that refuting evidence.

Do not use caller-side evidence to establish callee behavior. Read the callee.

If you cannot establish how the behavior arises, ask a question. Do not report a defect,
and do not change the code, on a hypothesis.

A passing test establishes that the tested contract holds for the tested inputs.
It does not establish behavior that the test does not exercise.

## Exhaustiveness claims

Treat words such as “only,” “all,” “never,” “unused,” “dead,” “no caller,” “the
existing owner,” and “redundant” as exhaustiveness claims.

Do not establish an exhaustiveness claim from a sample.

Enumerate every site that the claim covers, with a scope-aware tool such as LSP `findReferences` or `ast-grep`.

Compare the enumeration against a text search.

If semantic search finds fewer sites than text search, treat the disagreement as a tool failure until you resolve it. A cold or incomplete index can return too few results without an error.

### References a search cannot find

A reference can exist that neither search finds. Before you make an
exhaustiveness claim, identify whether the symbol can be reached by name at
runtime:

- attribute lookup from a string;
- a registry, a plugin table, or an entry point;
- configuration;
- serialized data;
- a template;
- a database column or a query.

Where any of these applies, enumeration does not establish exhaustiveness.
Establish the reachable set from the registry or the configuration that holds the
names, or state the claim as unverified.

### Match the evidence to what the claim licenses

Identify what the claim licenses, and match the evidence to it.

- Where the claim licenses a removal, or a change to a public contract,
  enumerate with a scope-aware tool. Where no such tool is available, do not
  remove and do not change the contract. State the claim as unverified and ask.
- Otherwise enumerate by text search across the repository, and state what that
  method cannot see.

Do not present an unverified claim as established.

## Existing machinery

When you need to establish why existing machinery exists, inspect its history.

For machinery of the kinds listed under Change discipline in `../SKILL.md`:

1. use `git blame` to identify the change;
2. use `git log -S <symbol>` or the relevant history to find the introducing commit;
3. identify the requirement or failure that the change addressed.

Do not remove existing machinery only because its current purpose is not obvious.

## Refutation

Search for evidence that would make your claim false.

Examples:

- A canonicalization at function entry refutes “flexible input reaches internal code.”
- An existing second caller can refute “this generic interface has no requirement.”
- A mutation after cache construction can refute “this cached value is valid for the object lifetime.”
