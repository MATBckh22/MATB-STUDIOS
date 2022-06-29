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

## Error Messages

| Reason of Error  | Example | Error Output |
| ------------- | ------------- | ------------- |
| trying to access beyond list limits  | `test = [1,2,3]` then `test[4]`  | `IndexError`
| trying to convert inapproriate types  | `int(test)`  | `TypeError`
| referencing a non-existing variable  | `a`  | `NameError`
| mixing data types without approriate coercion  | `'3'/4 `  | `TypeError`
| forgetting to close parenthesis, quotation, etc  | `a = len([1,2,3]` then `print(a)`  | `SyntaxError`
