<<<<<<< HEAD
=======
# getmaxfnlen
How to find the length of the longest function name in a python module (.py file)

Could be useful as a lightweight method to align debug output into columns, such as:

```
# Placed within a function, print the current function name and filename in two columns
print(
    inspect.currentframe().f_code.co_name,
    " " * (f() - len(inspect.currentframe().f_code.co_name)),
    path.basename(__file__)
    )
```
>>>>>>> 9316330746a875c05058305b7e06dfed5d6d8d0c
