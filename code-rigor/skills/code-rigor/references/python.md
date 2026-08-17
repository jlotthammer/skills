# Python Specialization

Load only for Python code.

Apply the general ownership/interface/dataflow rules to Python's dynamic runtime rather than compensating for unclear contracts with defensive flexibility.

## Interfaces and typing

Use typing to make owned contracts explicit, not to manufacture abstraction. Avoid broad `Any`, shapeless dictionaries, runtime `getattr`/`hasattr` cascades, or optional parameters when the repository controls the concrete shape.

Let Ruff/type checkers own mechanically decidable hygiene. Use Code Rigor for semantic questions they cannot answer.

## Iteration and objects

Remember that generators/iterators are stateful and one-shot. Avoid accidental consumption during logging/validation.

In repeated data-heavy paths, avoid converting structured/bulk data into large numbers of Python objects unless object semantics are actually required.

## Imports and initialization

Import-time side effects, environment reads, global caches, and singleton initialization create hidden process-lifetime state. Prefer explicit ownership when behavior or cleanup matters.

## Exceptions and context managers

Use context managers for resources whose lifetime follows a lexical scope. Catch exceptions only where the code can add policy, recovery, or meaningful context.
