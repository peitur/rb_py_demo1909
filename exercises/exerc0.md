
# Basics

## Variables

0. Print hello world.

1. Create different variable types and print their types. Skip list and dict here.

```
./solutions0.1.py
123 : int
1.2 : float
hello : str
True : bool
```

2. Create a list of different types, loop through it and print the type names with their indexes.
TIP: Use the enumerate builtin function.

```
./solutions0.2.py
0 : int
1 : float
2 : str
3 : bool
4 : list
5 : dict
6 : function
```

3. Create a list of numbers (float and integers) and calculate the average value.

3.1. Modify 3 with type checks. Check for int and float tpyes. Anything else should be just ignored.
Note: Remember that this changes the average item count.

4. Create a list of simple mathematical (lambda) functions operating on integer pairs ( +, -, /, *, ** ).
Create a function that takes two numbers processing them with each operation in the list. Sum all results and return it.
Print each element using a loop and the sum.

```
a: 3
b: 2

5
1
1.5
6
9

sum: 22.5
```

5. Create a dict that stores the results of each operation in 3. Key is a operation indicator.
Print each element using a loop.

6. Use list comprehension for list processing. Create a list of strings (different length).
Return all the string items longer then 3 characters.
