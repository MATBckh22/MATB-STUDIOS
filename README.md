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

`else`:
    
