 # Decomposition, Abstraction, and Functions

## Programming Ethnics
- more code is not necessarily a good thing
- measure good programmers by the amount of functionality
- functions
- decomposition and abstraction

exp: **projector**
### ABSTRACTION IDEA: 
#### **Do not need to know how projector works to use it**
- a projector is a black box
- don’t know how it works
- know the interface: input/output
- connect any electronic to it that can communicate
with that input
- black box somehow converts image from input source to a wall, magnifying it

### DECOMPOSITION IDEA: 
#### **Different devices work together to achieve an end goal**

- projecting large image for Olympics decomposed into
separate tasks for separate projectors
- each projector takes input and produces separate
output
- all projectors work together to produce larger image

*Applying these concepts is crucial to become a good programmer*

## Decomposition (Create Structure)

In programming, divide code into modules

- are self-contained
- used to break up code
- intended to be reusable
- keep code organized
- keep code coherent

*Decomposition can be achieved with functions and classes (advanced)*

## Abstraction (Supress Details)

In programming, think of a piece of code as a black box

- cannot see details
- do not need to see details
- do not want to see details
- hide tedious coding details

*Abstraction can be achieved with function specifications or docstrings*

## Functions

Functions are not run in a program until they are *called* or *invoked*.

Characteristics:
- has a name
- has parameters (0 or more)
- has a docstring (optional but recommended)
- has a body
- returns something

### Refer function structure in slide 12
```
#def function_name(parameters of arguments):
def is_even( i ):
    """
    Input: i, a positive int,
    Returns True if i is even 
    """
#what happens in """here""" will be the docstring
    print("inside is even")
    return i%2 == 0
#this is the body
is_even(3)
#calling the function using it's name and values for parameters
```
Parameters are the inputs of the function. Docstring is the specification of the abstraction. It's a multi-line text for explanation purposes. Last line is to call the function.

Function body is a mini program that does things.

```return i%2 == 0``` is a crucial keyword to evaluate value.

## Variable Scope
```
#the first parentheses will be the formal parameters, this doesn't have value yet, ur assuming x has value later
#below will be ur function definition
def f(x):
    x = x + 1
    print("in f(x): x=",x)
    return x
#beyond this will be the ur main program code
x = 3
z = f(x) #here is ur function call

```
Function definitions will be stored in the computer **until u call it with the values into the function.** The following action will be the **actual parentheses** in which u mapped values into x for the function to work. In this case ur mapping `x = 3`. Return of function will be assigned to variable z.

### Visualising function operations is in slide 15-18

## No `return` Warning
If the function definition is missing a return statement, python automatically returns `None` value, a special type of value that represents the absence of the value.

*Note: `None` is not a string*

## `return` vs `print`

| `return` | `print` |
| - | - |
| return only has meaning **inside** a function | print can be used **outside** functions
| only one `return` can be executed inside a function | many `print` statemtents can be executed
| code after `return` statement will not be executed | can be executed after `print`
| has a value associated with it, given to **function caller** | has a value associated with it but outputted to console 

### With `return`

Here we have a function that can identify even positive integers:

```
def is_even_with_return( i ):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    remainder = i % 2
    return remainder == 0

is_even_with_return(3) 
print(is_even_with_return(3) )
```

Notice the statement `return remainder == 0`, that is to say if there are no remainders after division, `True` is returned to the function caller, otherwise print `False`.

However, as previously discussed, the boolean values that are returned will not be showed in console unless a `print` statement is carried out, like `print(is_even_with_return(3) )`.

[Visualization](https://pythontutor.com/render.html#code=def%20is_even_with_return%28%20i%20%29%3A%0A%20%20%20%20%22%22%22%20%0A%20%20%20%20Input%3A%20i,%20a%20positive%20int%0A%20%20%20%20Returns%20True%20if%20i%20is%20even,%20otherwise%20False%0A%20%20%20%20%22%22%22%0A%20%20%20%20print%28'with%20return'%29%0A%20%20%20%20remainder%20%3D%20i%20%25%202%0A%20%20%20%20return%20remainder%20%3D%3D%200%0A%0Ais_even_with_return%283%29%20%0Aprint%28is_even_with_return%283%29%20%29&cumulative=false&curInstr=13&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

### Without `return`

```
def is_even_without_return( i ):
    """ 
    Input: i, a positive int
    Does not return anything
    """
    print('without return')
    remainder = i % 2

is_even_without_return(3)
print(is_even_without_return(3) )
```

This function has the same goal, however it doesn't work like it's supposed to be. This is because the function doesn't have a  `return` statement. 

As previously discussed, since this function is missing a `return` statement, there are no operations to get back to the function caller.

[Visualization](https://pythontutor.com/render.html#code=def%20is_even_without_return%28%20i%20%29%3A%0A%20%20%20%20%22%22%22%20%0A%20%20%20%20Input%3A%20i,%20a%20positive%20int%0A%20%20%20%20Does%20not%20return%20anything%0A%20%20%20%20%22%22%22%0A%20%20%20%20print%28'without%20return'%29%0A%20%20%20%20remainder%20%3D%20i%20%25%202%0A%0Ais_even_without_return%283%29%0Aprint%28is_even_without_return%283%29%20%29&cumulative=false&curInstr=10&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

### Thus, `None` will be returned to address this issue, the following `print` statement will also print `None`.

## Function as Arguments

