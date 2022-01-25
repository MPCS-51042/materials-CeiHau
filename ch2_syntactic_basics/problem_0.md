## Explaining the `test` method:

**1. What are the arguments and what types do these arguments need to have for this function to work?**

function: the function that need to be tested, the type need to be ``function``

examples: the test data and truth value, the type need to be ``list``

**2. Walk us through the code line by line. What is happening here?**
```python
def test(function, examples):   # the defines of the function called test
    passed = 0                  # the argument that record the number of tests passed
    run = 0                     # the argument that record the number of tests ran
    
    for example in examples:    # for statement, steps through evert example in the examples list 
        run += 1                # the number of tests ran plus one
        expected = example[-1]  # the expected value in current example
        actual = function(*example[:-1])    # the actual value in current example, the * operator can unpack the arguments out of a tuple

        if expected == actual:  # if statement, if the expected value equal to actual value, then the number of tests passed plus one
            passed += 1         
        else:                   # else, display the information of this error example and actual value 
            print(f"Whoops. For example {example}, the function returned {actual}.")

    print(f"\n{passed} out of {run} examples worked as expected.")  # display the the summary of all example
```
**3. Does this function have a return value? How do you know?**

Yes the return value is ``None``, we can use `print(test(function=find_twos, examples=find_twos_examples))`
and a `None` will show
