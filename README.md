# String Manipulation, Guess and Check, Approximations, Bisection

## Strings
function `len()` **retrieves the length of the string**

```
>>> s = "abc"
>>> len(s)
3
>>>
```
**indexing:** using square brackets to get the value in a string at a certain position
```
s = "abc"
>>> s[0]
'a'
>>> s[1]
'b'
>>> s[2]
'c'
>>> s[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>>
```
Index `s[3]` is out of bounds bc function `len(s)` evaluates to 3

*note: **negative integrals** can be used as well*
```
>>> s[-1]
'c'
>>> s[-2]
'b'
>>> s[-3]
'a'
```
## String Slicing

similar to `range()`, : is used to slice strings `[start:stop:step] [start:stop]` (default: step = 1)
```
>>> s = "abcdefgh"
>>> s[3:7]
'defg'
>>> s[4:8]
'efgh'
>>> s[0:2:2]
'a'
>>> s[0:6:2]
'ace'
```
step as negative number(s)
```
>>> s[::-1]
'hgfedcba'
>>> s[::-2]
'hfdb'
>>> s[0:7:-1]
''
```
`s[::]` same as `s[0:len(s):1]`

## String Substitution 
functions in python are *immutable*, which cannot be modified directly. **We cannot replace a character in the index just by indexing another word into the string.**

Though we can do this by replacing the entire string or recreating a string using the `new character + previous string:`
```
>>> s = "stringtest"
>>> s[0] = "a"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> s = "a" + s[1:len(s)]
>>> print(s)
atringtest
```

## Writing For loops with variable count
For loops have a loop variable that iterates over a set of values
```
for var in range(4): 
  <expressions> 
```
`var` iterates over values 0,1,2,3. expressions inside loop executed with **EACH** value for var.
```
for var in range(4,6)
  <expressions>
```
`var` iterates over values 4,5
*note: While `range()` can iterate over numbers, a for loop variable can iterate **any set of numbers**, not just values!*

## Application of string loops
`s[index]` can be replaced with `char` to make it more readable:
```
s = "abcdefgh"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")
        
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")
```
The difference between `s[index]` and `char` is `s[index]` is used to **index the element from the string** whereas `char` acts as a variable to do the same thing, but more efficiently.

In general, `s[index] = char (variable).`

*Author coded a cheering program with the help of this tutorial, check source code on MIT6 Lec3 Homework.*

# Algorithms

## guess-and-check/exhaustive enumeration
Here is a simple code for solving the cube root of a number
```
cube = int(input("type a number for me to guess"))

for guess in range(cube+1):
    if guess**3 == cube:
        print("the cube root of",cube,"is",guess)
```
Though this code is flawed, it doesn't have any output for cube inputs that have cube roots of non-integrals. We can improve this by adding some details.
```

