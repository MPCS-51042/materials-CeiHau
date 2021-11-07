**1. What exception do you get**

I get `RecursionError: maximum recursion depth exceeded in comparison`

**2.Look up this exception online. What would you have to do in Python to make the line of code run without hitting that exception?**

Set a larger aximum recursion depth, using the following code:
```
import sys 
sys.setrecursionlimit(50001)
```

**3.Why might it be a bad idea to do what you suggested in #3?** 

Because it may lead to the death of kernel, at least on my machine. Also a really excessively deep recursion may cause stack overflow.

