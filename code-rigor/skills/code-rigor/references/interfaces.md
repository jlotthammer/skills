# Interfaces

**One concept should normally have one owner and one canonical interface.**

This reference owns the interface half of that invariant. For the authoritative-state
half, see `state-and-lifetime.md`.

Before you add or change an interface, identify:

- the current owner;
- every relevant caller;
- the current contract;
- the requirement that the interface change must satisfy.

Add genericity only when at least one of these requires it:

- a current caller;
- a public contract;
- a supported environment;
- a second real implementation.

Do not add genericity for a hypothetical future caller.

## Reject unsupported interface complexity

Do not introduce these forms unless a requirement needs them:

- parallel legacy, new, or fast APIs for one operation;
- wrappers that own no policy, transformation, or lifecycle;
- generic maps, `kwargs`, registries, factories, strategies, or modes that postpone a concrete interface decision;
- deep runtime type, shape, or representation branching over data the repository controls;
- compatibility aliases or version paths without an explicit support requirement.

Flexible external input is valid at a real boundary. Canonicalize it once. Keep internal contracts specific.

## Abstraction test

An abstraction must do at least one concrete job:

- remove duplicated behavior or duplicated policy that you can name; or
- establish an ownership, lifecycle, or contract boundary that callers rely on.

If deleting the abstraction makes the operation clearer and does not recreate required duplication or break a durable boundary, the abstraction does not own enough to justify its existence.
