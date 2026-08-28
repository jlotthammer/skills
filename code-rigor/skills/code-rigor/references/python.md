# Python Specialization

Load this reference only for Python code.

Apply the general ownership, interface, dataflow, state, failure, and control-flow rules to Python's dynamic runtime.

Do not compensate for an unclear internal contract with defensive flexibility.

## Interfaces and typing

Use typing to make an owned contract explicit.

Do not use broad `Any`, shapeless dictionaries, runtime `getattr` or `hasattr` cascades, or optional parameters when the repository controls a more specific shape.

Use broad types only when the contract is broad.

Let the repository's linter and type checkers enforce mechanically decidable hygiene. Use Code Rigor to decide the semantic correction when tooling reports a problem.

Do not silence a type error with `Any`, a cast, or a suppression when the real defect is an incorrect ownership or interface contract.

## Iteration and objects

Treat generators and iterators as stateful one-shot values.

Do not consume them during logging, validation, or inspection unless the operation owns that consumption or explicitly reconstructs the iterator.

In repeated data-heavy paths, keep data in structured or bulk form when object identity and per-object behavior are not required.

Do not create large numbers of Python objects only to feed a computation that can operate on the existing bulk representation.

## Imports and initialization

Treat import-time side effects, environment reads, global caches, and singleton initialization as process-lifetime state.

Use explicit ownership when behavior, ordering, invalidation, or cleanup matters.

Do not hide runtime policy in import side effects when a normal owner can establish it explicitly.

## Exceptions and context managers

Use a context manager when a resource lifetime follows lexical scope.

Catch an exception only where the code can add policy, recovery, or meaningful context.

Do not catch an exception only to replace it with an ambiguous value or to continue a required operation.
