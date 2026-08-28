# Testing

**Tests protect durable contracts, not the current implementation.**

A useful test rejects a plausible implementation that violates required behavior.

For each test you add, name the wrong implementation that the test rejects. If
you cannot name one, do not add the test.

A test is vacuous when it cannot fail for the reason it claims to test. An
assertion that a mock was called, in a test that called it, is vacuous. So is an
assertion that restates the implementation instead of the contract.

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
2. verify that the test fails against the broken behavior. If you cannot reproduce
   the broken state, record that the test was never observed to fail;
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

## Mechanical coverage checks

Treat a coverage report as a map of what the tests do not exercise. Do not treat
a coverage number as evidence that the tested behavior is correct. A suite can
execute every line and assert nothing about any of them.

When coverage falls below a configured threshold:

1. identify the uncovered behavior;
2. add a test where that behavior has a durable contract;
3. do not add a test only to raise the number;
4. remove unreachable code rather than cover it.

Keep numeric thresholds and tool configuration in repository tooling. Do not
duplicate them in this reference.
