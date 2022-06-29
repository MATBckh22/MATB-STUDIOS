# Testing, Debugging, Exceptions, and Assertions

## Defensive Programming

- write specifications for functions
- modularize programs
- check conditions on inputs/outputs

### Testing/Validation

- compare input/output
- *it's not working*
- *how can I break my program?*

### Debugging

- study events that leads up to an error
- *why is it not working?*
- *how can I fix my program?*

## Pre-test Prep

- **ensure code runs** (*removing syntax and static semantic errors*)

- have a set of **expected results** (*an input set where each input returns the expected output*)

## Classes of Tests

### Unit Testing

- validate each piece of program
- **testing each function separately** 

### Regression Testing

- **add test for bugs as u find them**
- **catch reintroduced errors** that were previously fixed

### Integration Testing

- **does overall program work?**
- tend to rush to do this

## Testing Approaches

- intuition

```
def is_bigger(x, y): #natural boundaries to the problem
    """ Assumes x and y are ints
    Returns True if y is less than x, else False """
```

### **Black Box Testing**

This is a method known to **explore paths through specification:**
```
def sqrt(x, eps):
    """ Assumes x, eps floats, x >= 0, eps > 0
    Returns res such that x-eps <= res*res <= x+eps """
```
- designed **without looking at the code**
- can be done by someone else to **avoid implementer biases**
- can be reused
- **paths** through specification:
    - *build test cases* in different natural space partitions
    - consider boundary conditions *(empty lists, singleton list, large and small numbers, extreme situations)*

### **Glass Box Testing**

Glass box is known for using code directly to guide design of test cases. It is called **path-complete** if every potential path through code is tested at least once. 

 - ### drawbacks
    - excessive amount of loop tests
    - missing paths
 
-  ### guidelines
    - **branches**
    - **for and while loops**

Test:
- branches
    - all parts of a conditional
- for loops
    - loop not entered, loop going exactly once and more than once
- while loops
    - cases that catch all ways to exit loop

```
def abs(x):
    """ Assumes x is an int
    Returns x if x>=0 and –x otherwise """
    if x < -1:
        return –x
    else:
        return x
```

- path-complete test could **miss a bug**
- path-complete test: 2 and -2
- but `abs(-1)` incorrectly returns -1
- should still test boundary cases

## Debugging

- steep learning curve
- goal: bug-free program

### Tools

- IDLE and Anaconda
- Python Tutor
- `print`
- be systematic in ur hunt

## `print` Statements

### Testing Hypothesis

- **when to print**
    - enter function
    - parameters
    - function results
- **bisection** method
    - put print halfway in code
    - decide where bug may be depending on values

## Debugging Steps

- study program code
    - don't ask what is wrong
    - ask how did I get the unexpected result
    - is it part of a family?

- **scientific method**
    - study available data
    - form hypothesis
    - repeatable statements
    - pick simplest input to test 

## Error Messages (easy)

| Reason of Error  | Example | Error Output |
| ------------- | ------------- | ------------- |
| trying to access beyond list limits  | `test = [1,2,3]` then `test[4]`  | `IndexError`
| trying to convert inapproriate types  | `int(test)`  | `TypeError`
| referencing a non-existing variable  | `a`  | `NameError`
| mixing data types without approriate coercion  | `'3'/4 `  | `TypeError`
| forgetting to close parenthesis, quotation, etc  | `a = len([1,2,3]` then `print(a)`  | `SyntaxError`

## Logic Errors (hard)

- **think** before writing new code
- **draw** pictures, take a break
- **explain** the code to 
    - someone else
    - rubber ducky (explain it as detailed as u can)

## Don'ts vs Dos (Case 1)

### Don'ts 

- Write entire program
- Test entire program
- Debug entire program

### Dos

- Write a function
- Test the function, debug the function
- Write a function
- Test the function, debug the function
- ***Do integration testing***

## Don'ts vs Dos (Case 2)

### Don'ts

- Change code
- Remember where bug was
- Test code
- Forget where bug was or what change
you made
- Panic

### Dos

- Backup code
- Change code
- Write down potential bug in a
comment
- Test code
- Compare new version with old
version

## Exceptions and Assertions

When a procedure execution hits an unexpected condition, we get an exception to what we expected:

```
>>> test = [1,2,3]
>>> test[1]
2
>>> test[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
```
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```
### Others

| Error | Cause |
| - | - |
| `SyntaxError` | Python can’t parse program 
| `NameError` | local or global name not found 
| `AttributeError` | attribute reference fails 
| `TypeError` | operand doesn’t have correct type 
| `ValueError` | operand type okay, but value is illegal 
| `IOError` | IO system reports malfunction (e.g. file not found)

## Dealing with Exceptions

- handlers (python)

```
try: #try block
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
except: #except block
    print("Bug in user input.")
```
`except` statement handles the error. Any exceptions raised in `try` block are handled by the `except` statement. **Execution continues with the body of the** `except` **statement.**

### Without `try` and `except`

```
a = int(input("type a number"))
b = int(input("type another number"))
print(a/b,a+b,a-b,a*b,a%b)

1st run:
type a number3
type another number4
0.75 7 -1 12 3

2nd run:
type a number3
type another numberhi
Traceback (most recent call last):
  File "c:\Users\Chong Kar Hing\Downloads\algorithms.py", line 2, in <module>
    b = int(input("type another number"))
ValueError: invalid literal for int() with base 10: 'hi'
```
A long exception error message is outputted, **it is not caught manually by the programmer.**

### With `try` and `except`

```
try:
    a = int(input("type a number"))
    b = int(input("type another number"))
    print(a/b,a+b,a-b,a*b,a%b)
except: 
    print("Bug in user input")

1st run:
type a number3
type another number4
0.75 7 -1 12 3

2nd run:
type a number3
type another numberhi
Bug in user input
```
**Value of exception is written to catch errors, nicer and simplified error message outputted.**

## Handling Specific Exceptions

Multiple `except` clauses can be used to deal with particular errors:

```
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError: #only catches ValueError
    print("Could not convert to a number.")
except ZeroDivisionError: #only catches ZeroDivisionError
    print("Can't divide by zero")
except: #otherwise do this
    print("Something went very wrong.")
```

These can be seen as if-else blocks to catch certain errors, the last `except` block is to catch any input errors that are otherwise not in the previous blocks.

## Other Exceptions

### `else`

Executed when execution of associated `try` body **completes with no exception**

### `finally`

**This block is always executed** after any `try`, `else`, `except`, etc clauses, even after an error is raised or `break`, `continue` or `return` is executed. This is incredibly useful to clean up code that **should be run no matter what happened.**

## Usage of Exceptions

What to do when encounter an error?

- fail silently: **not recommended, do not do this**
    - substitute default or just continue
    - no warning output

- return an error value: **not recommended too**
    - *what values to choose?*
    - complicates code having to check for special values

### **Recommended method:**

- stop execution, signal error condition:
    - raising an exception: `raise Exception("descriptive string")`

## Exceptions as Control Flow

### Flow

- raise an exception when unable to produce a result consistent with function's specifications:

`raise <exceptionName>(<arguments>)`

 This is followed by a keyword, the name of error to be raised and a string of message describing the exception (optional)

 ## Example of Raising Exceptions 1

 ```
 def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
    try:
        ratios.append(L1[index]/L2[index])
    except ZeroDivisionError:
        ratios.append(float('nan')) #nan = not a number
    except:
        raise ValueError('get_ratios called with bad arg')
    return ratios
```
This function is used to calculate a set of ratios of numbers. We begin by setting an empty list `ratio = []`. Under the for loop, when a number is indexed in, `try` block is executed when the index is in the correct boundary that we want. 

In cases where there is a `ZeroDivisionError` error, `nan` is added into the list indicating that it is not a number. 

Otherwise, when any error left is detected, `ValueError` is raised instead. 

## Example of Raising Exceptions 2

- Class list of each subject: each is a list of two parts:
    - first and last name of a student
    - grades on assignments

```
test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
[['bruce', 'wayne'], [100.0, 80.0, 74.0]]]
```
- create a **new class list** with names, grades and an average

```
[[['peter', 'parker'], [80.0, 70.0, 85.0], 78.33333],
[['bruce', 'wayne'], [100.0, 80.0, 74.0], 84.666667]]]
```

### Without `try` and `except`

```
def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

def avg(grades):
    return sum(grades)/len(grades)
```

Here we begin with defining the first function `get_stats()` to setup a new list containing a name with the associated grade and average. 

`avg()` is called to calculate the average of the student's grades: `return sum(grades)/len(grades)`

However, this system is flawed. It doesn't take account into students that don't have a grade:

```
test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
[['bruce', 'wayne'], [10.0, 8.0, 74.0]],
[['captain', 'america'], [8.0,10.0,96.0]],
[['deadpool'], []]] #<-- here
```

`ZeroDivisionError: float division by zero` will be raised because `return sum(grades)/len(grades)` is being executed.

We have two options to solve this problem:

### Option 1: Flag the error by printing a message

- **notify something** when it goes wrong:

```
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
```

The output will look like this:

```
warning: no grades data #error flagged
[[['peter', 'parker'], [10.0, 5.0, 85.0], 15.41666666],
[['bruce', 'wayne'], [10.0, 8.0, 74.0], 13.83333334],
[['captain', 'america'], [8.0, 10.0, 96.0], 17.5],
[['deadpool'], [], None]] #notice None
```

Even though the error is raised and flagged, `None` will still be printed because **there is no return program under** `except` **block.**

### Option 2: Change the policy

- decide that a **student with no grades gets a zero:**

```
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
        return 0.0
```
Now it will print zero:

```
warning: no grades data
[[['peter', 'parker'], [10.0, 5.0, 85.0], 15.41666666],
[['bruce', 'wayne'], [10.0, 8.0, 74.0], 13.83333334],
[['captain', 'america'], [8.0, 10.0, 96.0], 17.5],
[['deadpool'], [], 0.0]] #zero is printed
```

## Assertions

- want to be sure that **assumptions on state of
computation are as expected**
- use an assert statement to **raise an
AssertionError exception if assumptions not met**
- an example of **good defensive programming**

### Asserting

```
def avg(grades):
    assert len(grades) != 0, 'no grades data'
    return sum(grades)/len(grades)
```
`assert len(grades) != 0, 'no grades data'` is an assertion. It is a pre-condition where the **function ends immediately if this assertion is not met.** 

It raises `AssertionError` if it is given an empty list of grades. 

This is good practice that it prevents the program from outputting bad values. The program stops when something went wrong, so it's easier to trace the error and where exactly the bug came from.

## Assertions as Defensive Programming

- assertions don’t allow a programmer to control
response to unexpected conditions
- ensure that **execution halts** whenever an expected
condition is not met
- typically used to **check inputs** to functions, but can be
used anywhere
- can be used to **check outputs** of a function to avoid
propagating bad values
- can make it easier to **locate a source of a bu**g

## Where To Use Assertions

- goal is to **spot bugs as soon as introduced and make
clear where they happened**
- use as a **supplement to testing**
- raise **exceptions** if users supplies **bad data input**
- use assertions to
    - check **types of arguments or values**
    - check that **invariants** on data structures are met
    - check **constraints on return values**
    - check for **violations of constraints** on procedure (e.g. no duplicates in a list)
