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
Functions in python are *immutable*, which cannot be modified directly. **We cannot replace a character in the index just by indexing another word into the string.**

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
`var` iterates over values 0,1,2,3. Expressions inside loop executed with **EACH** value for var.
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
cube = int(input("type a number to begin!"))

for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != cube:
    print("this number doesn't have a perfect cube root!")
else:
    if  cube < 0:
        guess = -guess
    print("cube root of" + str(cube) + "is" + str(guess))
```
We set `abs` as an absolute value variable so the program is only allowed to handle absolute values. Under first condition if the guess in `range(abs(cute)+1)` to the power of 3 is equal or greater than `cube` input, `break` will stop the for loop and skip to `print("cube root of" + str(cube) + "is" + str(guess))`.

Second condition involves the feedback of an imperfect cube root. Given there are no perfect cube roots of the input, a feedback `print("this number doesn't have a perfect cube root!")` will be sent.

The last condition will be to determine if the input is negative. If the input is smaller than 0, `guess` will be replaced with `-guess`, same output will be given for first condition.

# Approximations
approximate solutiions can be programmed into the algorithm to provide a *close enough* answer when the input doesn't have a perfect cube root.

We can start with a guess and increment by small value. Keep guessing `|guess^3-cube| >=epsilon` for a small epsilon.

However, decreasing increment size leads to **slower program but more accurate answer**, increasing epsilon will lead to **less accuracy but faster program.**

```
cube = int(input("start with a number!"))
epsilon = 0.01
guess = 0.0
increment = 0.001
num_guesses = 0

while abs(guess**3-cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('the number of guesses is',num_guesses)
if abs(guess**3-cube) >= epsilon:
    print('failed to solve cube root for',cube)
else:
    print('the close guess of the cube root is',guess)
```
Starting with `guess = 0.0` and `increment = 0.001`, calculation of `guess**3-cube >= epsilon` will be looped over and over, `num_guesses` act as a counter of how many times the operation is looped and calculated to the closest cube root. When the guess is greater than the input, the while loop will break and print the closest number calculated. **This is to prevent the computer to do countless calculations in which the program doesn't stops.** 

# Bisection Search

This method is to eliminate half of the guesses each iteration, getting closer to the desired number.

An example of this concept below:
```
input: 78
0-100, guess:50, output: higher
50-100, guess 75, output: higher
75-100, guess 88, output: lower
...
guess:78, output: correct
```
We can implement this concept into finding the cube root:
```
cube = int(input("type a number to begin!"))
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3-cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses',num_guesses)
print("close cube root of the number is",guess)
```
We set the low and high boundaries to be 0-input. Next, similar to approximation, `abs(guess**3-cube) >= epsilon` is used as the condition. If the guess to the power of 3 is lower than the input, the low boundary will be replaced with `guess`, if it's greater, the high boundary will be replaced with `guess`, `guess` will be replaced again with `(high + low)/2.0` to eliminate half of the guessing space. This whole operation is in a while loop. The search space of this program is lessened by a lot using the method, while sacrificing some accuracy. 

*Author will try to combine these algorithms and code a more feature-rich calculator for cube roots later*

