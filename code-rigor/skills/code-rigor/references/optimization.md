# Optimization

Use this order:

1. eliminate work that does not need to happen;
2. move invariant work to the correct lifetime;
3. remove unnecessary representation changes, copying, I/O, allocation, and synchronization;
4. improve algorithmic complexity;
5. improve locality, batching, or use of existing optimized primitives;
6. add concurrency, caching, specialized fast paths, or custom low-level machinery only when evidence justifies them.

Do not skip directly to step 6 because it is easier to benchmark locally.

Before you add performance complexity:

1. identify the boundary whose performance matters;
2. measure that boundary. Where you cannot measure it directly, establish the dominant cost from the structure of the code, and state that the cost is structural rather than measured;
3. separate major cost categories. If you cannot separate them, state which costs the measurement combines;
4. identify why the proposed owner or boundary is the correct place for the optimization;
5. name each new state or proof obligation the optimization introduces;
6. define how you will verify the result.

Prefer an optimization that improves correctness, simplicity, and performance through the same representation or ownership decision.

Do not retain a faster path when its added complexity does not pay for a measured or required benefit.

Keep the clear implementation as a test oracle when an optimized path replaces it. Verify the optimized path against the oracle on the same inputs. The oracle maps the readable form to the fast form. Do not expose the oracle as a callable path in production code.

Report a measured speedup with its uncertainty and the number of runs. A single run is not a result.
