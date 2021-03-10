# getmaxfnlen
Returns the length of the longest function name in the module (.py file) that it is called from

Could be useful for aligning logging output into columns, such as:

```
print(
    inspect.currentframe().f_code.co_name,
    " " * (f() - len(inspect.currentframe().f_code.co_name)),
    path.basename(__file__)
    )
```
