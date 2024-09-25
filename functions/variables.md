# Variable in Python Don't hold data directly they hold the reference to the value stored at a memory location

In Python, variables are references to values held at memory locations and do not hold the data themselves. In Python, variables act as labels or pointers that refer to a specific location in memory where the value is stored.

When you assign a value to a variable in Python, you are actually creating a reference to the value at a particular memory location.

For example:

```python
x = 42
```

In this case, x is a variable that references a value of 42 stored at a specific memory location. If you then assign a new value to x, the variable is updated to reference the new value:

```python
x = "Hello, world!"
```

Now, x references a new value, which is a string "Hello, world!" stored at a different memory location.
