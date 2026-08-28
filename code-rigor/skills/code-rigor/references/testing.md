# Testing

**Tests protect durable contracts, not the current implementation.**

A useful test rejects a plausible implementation that violates required behavior.

Before you keep a test, identify the durable behavior, contract, invariant, or demonstrated regression that the test protects.

Do not keep a test whose main purpose is to freeze:

- helper names;
- source layout;
- internal call order;
- mock choreography;
- the current absence of internal code.

An absence test is valid when absence itself is a durable product, security, or compatibility contract.

## Regression tests

For a bug fix:

1. reproduce the failure at the narrowest stable boundary that exposes the required behavior;
2. verify the test fails against the broken behavior when practical;
3. fix the implementation;
4. verify the test passes;
5. keep the test only if it protects a durable contract after the patch is complete.

Do not add a test only to record that an internal helper, path, feature, or compatibility layer was removed.

## Existing tests

When a patch makes an existing test fail, establish which of these changed:

- the implementation violated an existing contract; or
- the contract itself changed as part of the requirement.

Do not weaken an assertion, enlarge a tolerance, add a skip or `xfail`, or make a mock vacuous only to obtain a passing suite.

If the contract changed, update the test to state the new durable behavior.

## Mocking

Mock a real external or expensive boundary when isolation requires it.

Do not mock internals only to make the current decomposition easy to assert.

Use real collaborators, fakes, or integration tests when interaction between components is the behavior under test.

## TDD

Use tests-first when the test can state desired behavior independently of the implementation.

Derive the test from the requirement and existing contract.

Do not derive the test from the implementation structure you already intend to write.

More tests do not automatically provide more confidence. Keep tests that reject meaningful wrong behavior.
