# PyTorch Specialization

Load this reference only for PyTorch code.

Treat autograd, storage aliasing, device, dtype, layout, module state, synchronization, and device-memory lifetime as extensions of the general ownership and dataflow rules.

## Autograd and storage

For each changed `detach`, `no_grad`, inference-mode, in-place, copy, or view operation, establish:

- whether gradients must flow through the value;
- whether storage is shared;
- whether later mutation is possible;
- whether the consumer requires an independent value.

Do not add or remove these operations by superstition.

## Device, dtype, and layout

Identify where device, dtype, and layout policy is established.

Do not repeatedly convert device, dtype, or layout inside helpers when an owner or canonicalization boundary can establish the required form once.

Add a conversion when a consumer or numerical requirement needs it.

## Module state

For each persistent tensor, choose among a parameter, registered buffer, plain attribute, or local tensor from its semantics.

Identify whether the value:

- is trainable;
- must appear in `state_dict`;
- must follow module device movement;
- is derived and can be recomputed;
- belongs only to one operation.

Do not use module state only because it is convenient storage.

## Memory lifetime

Identify what must exist simultaneously:

- model and optimizer state;
- activations;
- temporary materializations;
- cached tensors;
- logging or history references;
- host and device staging buffers.

Fix unnecessary retention or ownership at its source.

Do not treat cache clearing or arbitrary detaching as a substitute for a defined memory lifetime.

## Checkpoints

Treat checkpoint loading as a persistence boundary.

Define the supported schema and expected key differences.

Validate those differences explicitly.

Do not silently accept broad incompatibility unless backward compatibility is an explicit requirement.
