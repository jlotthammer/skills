# Interfaces

**One concept should normally have one owner and one canonical interface.**

Before adding an interface, identify the repository's current owner, callers, and contract. Add genericity only for a current caller, public contract, supported environment, or second real implementation.

Challenge:

- parallel legacy/new/fast APIs for one operation;
- wrappers that own no policy, transformation, or lifecycle;
- generic maps, `kwargs`, registries, factories, strategies, or modes used to postpone interface design;
- deep runtime type/shape/representation branching over data the repository already owns;
- compatibility aliases or version paths without an explicit support requirement.

External flexibility is legitimate at real boundaries. Canonicalize once and keep internal contracts specific.

An abstraction should remove named duplicated complexity or establish a durable ownership boundary. If deleting it makes the operation clearer without creating duplication, it probably did not own enough to exist.
