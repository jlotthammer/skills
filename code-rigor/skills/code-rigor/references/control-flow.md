# Control Flow

**Keep the normal execution path visible. Minimize the conditions and states a reader must track at one time.**

An invariant established elsewhere removes local branching and adds to what a
reader must already know. Prefer the non-local invariant when a named owner
establishes it and the reader can reach that owner. Prefer a local condition
when the reader would otherwise reconstruct the invariant from call sites.
See `dataflow.md`.

## Branching and nesting

For a function with substantial branching:

1. Identify the normal execution path.
2. Identify nested conditions that hide that path.
3. Identify conditions that are tested more than once.
4. Identify independent state dimensions that are nested together.
5. Identify booleans or sentinel values that encode an implicit state model.
6. Determine whether an earlier boundary can establish a condition once.

Use an early return, `continue`, or another guard when it removes unnecessary nesting and keeps required cleanup and state changes explicit.

Do not invert a condition only to reduce indentation when the inverted condition is harder to understand.

Do not combine unrelated decisions into a dense boolean expression only to reduce branch count.

## State transitions

When behavior depends on valid transitions between states, represent those states and transitions explicitly.

Do not encode a state machine as an undocumented combination of booleans, sentinels, exception paths, and repeated conditionals.

Prefer a representation in which an illegal state cannot be constructed. A state
that cannot exist needs no branch to defend against it.

Keep a direct `match`, dispatcher, parser branch, protocol case, or algorithmic case split when the cases are part of the domain and the explicit form is easier to inspect.

## Decomposition

Extract a helper when the helper owns a coherent operation, contract, transformation, or lifecycle.

Do not extract helpers only to reduce nesting, line count, cyclomatic complexity, or cognitive complexity.

Do not distribute one cohesive algorithm across helpers when a reader must reconstruct all of them to understand the operation.

Cohesion is the property that everything inside a unit serves one purpose. Judge
a helper by its cohesion, not by its length.

## Mechanical complexity checks

Treat a cyclomatic-complexity or cognitive-complexity failure as a request to inspect the control flow. Do not treat the score as proof that the design is wrong.

When a complexity tool reports a violation:

1. inspect boundaries, state representation, repeated conditions, and nesting;
2. refactor when the change makes the behavior easier to understand;
3. do not refactor only to lower the score;
4. use the repository's approved suppression only when the branching is intrinsic and the clearer implementation still exceeds the configured threshold.

Keep numeric thresholds, scoring rules, and tool configuration in repository tooling. Do not duplicate them in this reference.
