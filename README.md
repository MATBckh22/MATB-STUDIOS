
# Recursion and Dictionaries

## Recursion

Process of repeating items similarly:
*mise en abyme* or *Droste effect*

Example: **A Recursive Light Bulb Joke**

Q: How many twists does it take to screw in a light bulb?

A: is it already tightly screwed in? Then zero. If not, twist it once, ask me again, and add 1 to my answer.

### Algorithmically

designing solutions to problem by	**divide-and-conquer** or **decrease-and-conquer**
- reduce a problem to simpler versions repeatedly so it can be solved directly afterwards

### Semantically

a programming technique where a **function calls itself**

- the goal here: **no infinite recursion**
- **must have 1 or more base cases that are easy to solve**
- solve the same problem on **some other input** or simplifying the larger problem input

## Multiplication -  Iterative Solution

Using an iterative solution to calculate a multiplication will look like this:
```
a*b = a + a + a + ... (up to b-th times)
```
We then capture state by an iteration number `i` starts at b:

```
i --> i-1 --> ... --> 0
```
and a current value of computation:
```
result --> result + a
```
Applying these concepts, we get:
```
def mult_iter (a,b):
    result = 0
    while b > 0: #iteration
        result += a #current value of computation
        b -= 1 #current value of iteration variable
    return result

```
## Multiplication - Recursive Solution

Applying basic recursion concepts, we can simplify multiplication by a lot:
```
a*b = a + a + a + ... (up to b-th times)
    = a + a(b-1)
    = a + a +a(b-2)
    ...
```
- Recursive step: reducing a problem to a smaller version of a same problem
- Base case: keep reducing it until it can be solved directly   

```
when b = 1, a*b = a
```
Simplified code:
```
def mult_recur (a,b):
    if b == 1:
        return a
    else:
        return a + mult(a,b-1)
```
## Factorial
Factorial equation:
```
n! = n(n-1)(n-2)...(1)
```
Base case for factorial: 
`n = 1`
```
if n == 1: 
    return n
```
Reducing the problem using recursive steps: `n*(n-1)!`
```
else:
    return n*factorial(n-1)
```
Combining this will result in:
```
def fact(n):
    if n == 1:
        return n
    else: 
        return n*fact(n-1)
print(fact(4))
```
Copy this code to https://pythontutor.com/ for a more detailed visualization of what's going on.

### Observations

- each recursive call to a function **creates it's own scope**
- bindings of variables in a scope are **not changed by recursive call**
- flow of control **passes back to previous scope once function call returns value**

## Inductive Reasoning

How to prove recursive code works:
```
def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

```
vs 
```
def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a , b-1)
```
-  `mult_iter` terminates because b is initially positive (b > 0), decreasing it's value by 1 each return around loop and eventually becomes less than 1

- `mult` called with b = 1 has no recursive call when stops, which we call base case

- `mult` called with b > 1 will initialize the recursive call and makes a smaller version of b, eventually reaching to base case (b = 1)

## Mathematical nduction
	
To prove a statement indexed on integers is true for all values of n *(learnt in high school, author will skip)*

## Towers of Hanoi

Story:
*A temple in Hanoi has 3 spikes, one of which has a stack of 64 different sized discs. The stack of discs need to move to another spike. 2 rules:*
- only move one disc at a time
- larger disc cannot cover up a smaller disc

**Think Recursively**
- take a stack of n-1 discs and move it to another spike
- move the bottom one to another spike
- stack and repeat
```
def printMove(fr, to):
 print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
 if n == 1:
    printMove(fr, to)
 else:
    Towers(n-1, fr, spare, to)
    Towers(1, fr, to, spare)
    Towers(n-1, spare, to, fr)

```
## Fibonacci Numbers
Story:
*Newborn pairs of rabbits are put in a pen, they mate at age of one month. They also have one month of gestation period (pregnancy). Assume rabbits never die, female rabbit always produces one new pair of newborn rabbits every month from it's second month on.*

**Q: How many female rabbits are there at the end of one year?**

| Month  | Females |
| ------------- | ------------- |
| 0  | 1  |
| 1  | 1  |
| 2  | 2  |
| 3  | 2  |
| 4  | 4  |
| 5  | 4  |


## Recursion on Non-numerics

### Palindrome String

Reads the same forwards and backwards, exp: `Able was I, ere I saw Elba`

How do we solve this recursively?
**Convert the string to just characters and converting upper case to lower case**

- Base case: string of 0-1 is a palindrome
- Recursive step: first character matches last character, palindrome proved if middle is also a palindrome

```
def ispalindrome(s):
    def toChars(s):
        s = s.lower() #mutates the string and reduces any character to lower case
        ans = "" #set empty string
        for c in s: #adds the characters into a string
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
```
`toChars(s)` function basically acts as a string manipulator to remove any spaces and turns all chacracters to lower cases.
```
def isPal(s):
        if len(s) <= 1: #base case
            return True
        else: 
            return s[0] == s[-1] and isPal(s[1:-1]) #recursive step
        return isPal(toChars(s))
```
`isPal(s)` function will have two blocks:
- base case: if the entire string has only one or less than one character, all instances will be returned true
- recursive step: takes the first and last character from the string and returns true, while reducing the length of the string using `isPal(s[1:-1])`, calls the function again and repeats the process over and over until it reaches base case 

*Revise string manipulation and functions thoroughly to get the idea*

## Divide And Conquer

This is a practice used to solve a hard problem by breaking it into a set of sub-problems:

- sub-problems are easier to solve than the original
- solutions of sub-problems can be combined to solve the original

## Dictionaries

### Storing Student Info

Here is an example of student info containing names, their grades and cgpa:
```
names = ["John","Adam","Morty"]
grade = ["A+","B+","A"]
course = [3.0,4.0,3.7]
```
For what we've learnt so far, this is the process to store it:
- separate list for each item
- each list has the same length 
- each index refers to info for a different person
```
def get_grade(student, name_list, grade_list, course_list):
 i = name_list.index(student)
 grade = grade_list[i]
 course = course_list[i]
 return (course, grade)
```
This will work, but it's messy, not friendly to large amount of data, must maintain each lists and keep track of them, index should also be in integers.

### Cleaner and More Efficient Way - Dictionary

- index item of interest directly
- one data structure, no separate lists

**List vs Dictionary**

#### List
| index  | element |
| ------------- | ------------- |
| 0  | Elem 1  |
| 1  | Elem 2  |
| 2  | Elem 3  |
| 3  | Elem 4  |
| 4  | Elem 5  |
| 5  | Elem 6  |

#### Dictionary
| custom index by label  | element |
| ------------- | ------------- |
| Key 1  | Val 1  |
| Key 2  | Val 2  |
| Key 3  | Val 3  |
| Key 4  | Val 4  |
| Key 5  | Val 5  |
| Key 6  | Val 6  |

### Dictionary 

Store pairs of data with it's corresponding **key** and **value**
```
my_dict = {}
grades = {"John":"A+","Adam":"B+","Morty":"A"}
```
Similar to indexing, python looks up the key and returns the value associated to the key. If the key isn't found, error output will be printed:
```
>>> grades = {"John":"A+","Adam":"B+","Morty":"A"}
>>> grades["John"]
'A+'
>>> grades["Adam"]
'B+'
>>> grades["Shaun"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Shaun'
```
## Dictionary Operations
