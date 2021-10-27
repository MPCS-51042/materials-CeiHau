Function-based approach focuses on the output we want, the result, and doesn't pay much attention to how to get the result and the state during process. Object-based approach focuses on how to perform the task and manage the state. 

For implementation likes the matchers, we only care about the result when we check in our tests and we don't need to record processing status, so we focused our efforts on independent functions.

For implementation likes the test runner, we need to focus on how to test our program with multiple examples and record the number of test passed and failed, so we chose objected-based approach.      