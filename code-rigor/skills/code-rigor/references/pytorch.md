# PyTorch Specialization

Load only for PyTorch code.

Treat autograd, storage aliasing, device, dtype/layout, module state, synchronization, and device-memory lifetime as extensions of the general ownership/dataflow rules.

## Autograd and storage

For detach/no-grad/inference/in-place/copy/view operations, establish the intended gradient and aliasing semantics. Do not add or remove them by superstition.

## Device, dtype, and layout

Repeated device/dtype/layout conversion deep inside helpers usually indicates an unclear boundary. Establish policy at an owner or canonicalization boundary where possible.

## Module state

Choose deliberately among parameters, registered buffers, plain attributes, and local tensors according to training, persistence, and device semantics.

## Memory lifetime

Reason about what must exist simultaneously: persistent model/optimizer state, activations, temporary materializations, cached tensors, logging/history references, and host/device staging. Fix retention/ownership rather than treating cache clearing or arbitrary detaching as memory management.

## Checkpoints

Checkpoint loading is a persistence boundary. Validate expected schema/key differences explicitly rather than silently accepting broad incompatibility.
