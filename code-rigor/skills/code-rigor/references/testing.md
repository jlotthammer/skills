# Testing

**Tests protect durable contracts, not the current implementation.**

A useful test answers:

> What plausible wrong implementation would this reject?

If the answer is mainly "one that changes helper names, source layout, internal call order, mock choreography, or the current absence of code," the test is probably pinning implementation.

## Regression tests

For a bug fix, prefer the narrowest stable boundary that reproduces the actual failure. Verify the broken behavior would fail the test when practical.

Do not add a test merely to memorialize that an internal helper, path, feature, or compatibility layer was removed. Test the meaningful behavior or invariant that made removal correct. Absence tests are justified only when absence itself is a durable product, security, or compatibility contract.

## Existing tests

When a patch makes an existing test fail, first determine whether the implementation broke the contract or the contract genuinely changed. Do not weaken assertions, enlarge tolerances, add skips/xfails, or make mocks vacuous merely to obtain green tests.

## Mocking

Mock real external or expensive boundaries when needed. Avoid mocking internals merely so the current decomposition is easy to assert. Prefer real collaborators, fakes, or integration tests when interaction between components is the behavior under test.

## TDD

Tests-first is useful only when the test independently states desired behavior. Derive the test from the requirement and existing contract, not from the implementation you already intend to write.

Keep a new test only if it protects a durable contract after the patch is complete. More tests are not automatically more confidence.
