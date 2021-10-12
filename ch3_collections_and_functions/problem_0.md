## Evaluating the `test` method:

**1. What differences do you notice between the functions that we do test with this method and the ones that we don't test with this method? Why do you think we chose to use it where we did?**


In last homework, we use this method in Problem 3, 4, 5, 7.1, 7.2, and 8. These problem have different output data with different input data. I think the reason we chose to use this method is that there are endless input data and the input data is simple. With the `test` function,We can easily test many data to determine the accuracy of our program. 

We don't use this method in Problem 6 and 7.3. Because the problem itself may not require input data and the solution is unique, as in Problem 6. May also because the input is complex so that we don't need much data to verify our program, as in problem 7.3.  



**2. If you were in charge of writing a Python package to help other programmers write automated tests in Python, what would you want it to do that the test method doesn't do? You can talk about functionalities that you wish it had that it doesn't have such as "I wish I could test stuff about a function besides just its return value", or you can talk about stuff that you wish it did differently such as "I wish the way the variables get passed in were more clear. Something like this...(and then explain how you'd like to see it done)."**

I think the output information of wrong answer should be more clear, now it is 
``
Whoops. For example (input_data, expected_data), the function returned {output_data}.
``. It will be clearer if it changes to 
`
Whoops. The input data is {input_data}, the expected data shouold be {expected_data}, however, the output data of the function is {output_data}. 
`
And add a boolean parameter `verbose` to the funciton, if `verbose = True`, then it should show more information, like the both the information of correct answer and wrong anwser. If `verbose = False`, just input the information of wrong answer.  