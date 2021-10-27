1. I think python evaluates expression in normal order, because the test raise the `RecursionError: maximum recursion depth exceeded`. This only happens when the language evaluates eagerly, since `p()` are evaluated when it is defined, which cause the program to run forever and the maximum recursion depth exceeded.

2. Change the `test` method to 
    ```
    def test(x, y):
        if x == 0:
            return 0
        else:
            return y()
    ```
    I change the second argument from `y()` to `y`, and change the return value from `y` to `y()`.

3. For example, I want to execute a function, `Func()`, which has two arguments, `apple_num` and `buy_apple()`. I want to execute `buy_apple()` only when `num_apple == 0`. In this situation, I want lazy evaluation. Or in some situations, I need the method depends on the previous computation.  

    