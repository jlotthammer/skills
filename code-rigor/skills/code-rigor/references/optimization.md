# Optimization

**Prefer removing work over building machinery to perform unnecessary work faster.**

Use this order:

1. eliminate work that need not happen;
2. move invariant work to the correct lifetime;
3. remove unnecessary representation changes, copying, I/O, allocation, or synchronization;
4. improve algorithmic complexity;
5. improve locality, batching, or use of existing optimized primitives;
6. add concurrency, caching, specialized fast paths, or custom low-level machinery only with evidence.

Measure the boundary that matters before introducing performance complexity. Separate major cost categories when possible so an optimization addresses the actual bottleneck.

A performance change should identify:

- the measured or structurally evident source of cost;
- why the chosen owner/boundary is appropriate;
- what additional state or proof obligations the optimization introduces;
- how the result will be verified.

Prefer optimizations where correctness, simplicity, and performance improve from the same representation or ownership decision.
