# Interfaces

**One concept should normally have one owner and one canonical interface.**

This reference owns the interface half of that invariant. For the authoritative-state
half, see `state-and-lifetime.md`.

Before you add or change an interface, identify:

- the current owner;
- every caller, enumerated as `evidence.md` requires;
- the current contract, as defined under Terms in `../SKILL.md`;
- the requirement that the interface change must satisfy.

Add genericity only when at least one of these requires it:

- a current caller that needs a different type or behavior;
- a public contract that already promises the variation;
- a supported environment that behaves differently;
- a second implementation that exists today.

Do not add genericity for a hypothetical future caller.

Coupling is what a caller must know to use an interface correctly. Each
precondition, ordering rule, and shared representation adds coupling. Reduce
what the caller must know before you add machinery to manage what it knows.

## Reject unsupported interface complexity

Do not introduce these forms unless a requirement needs them:

- parallel legacy, new, or fast APIs for one operation;
- wrappers that own no policy, transformation, or lifecycle;
- generic maps, `kwargs`, registries, factories, strategies, or modes that postpone a concrete interface decision;
- deep runtime type, shape, or representation branching over data the repository controls;
- compatibility aliases or version paths without an explicit support requirement.

Flexible external input is valid at an owned boundary. Keep internal contracts specific. See `dataflow.md` for how to canonicalize at that boundary.

## Abstraction test

An abstraction must do at least one concrete job:

- remove duplicated behavior or duplicated policy that you can name; or
- establish an ownership, lifecycle, or contract boundary that callers rely on.

If deleting the abstraction makes the operation clearer and does not recreate required duplication or break a durable boundary, the abstraction does not own enough to justify its existence.

That conclusion is a hypothesis. Establish why the abstraction exists, as
`evidence.md` requires, before you remove it.

## Changing a contract that has callers

A public contract cannot change in one step without breaking a consumer you do
not control.

1. Expand. Add the new form beside the old one. Both work.
2. Migrate. Move every caller you own to the new form.
3. Contract. Remove the old form once no caller you must support depends on it.

Each step is separately reversible, and step 3 needs the enumeration that
`evidence.md` requires for a removal.

Do not keep the expanded state after migration completes. Two forms with no
support requirement is the parallel API this reference rejects.
