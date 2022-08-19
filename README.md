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
```python
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
```python
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

```python
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

```python
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

Arguments can take on any type, even functions: [Visualization](https://pythontutor.com/render.html#code=def%20func_a%28%29%3A%0A%20%20%20%20print%28'inside%20func_a'%29%0Adef%20func_b%28y%29%3A%0A%20%20%20%20print%28'inside%20func_b'%29%0A%20%20%20%20return%20y%0Adef%20func_c%28z%29%3A%0A%20%20%20%20print%28'inside%20func_c'%29%0A%20%20%20%20return%20z%28%29%0A%20%20%20%20%0Aprint%28func_a%28%29%29%0Aprint%285%20%2B%20func_b%282%29%29%0Aprint%28func_c%28func_a%29%29&cumulative=false&curInstr=14&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
def func_a():
    print('inside func_a')
def func_b(y):
    print('inside func_b')
    return y
def func_c(z):
    print('inside func_c')
    return z()
    
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))
```

### `print(func_a())`

When `func_a()` is called, it takes no parameters since there's the parantheses of the caller is left blank. And given there's no return argument, this prints `None`.

### `print(5 + func_b(2))`

`func_b()` takes one parameter overall, in this case it's 2. Notice when it returns 2, the print method adds it up with 5, so 7 will be printed in output.

### `print(func_c(func_a))`

This is a nested function call, where it calls one function that's inside of the other. Just like functions, it goes from the outer to inner layer, so `func_c()` is considered first.

In `func_c()`, value `z()` is returned but it stays on hold while waiting for `func_a` to return something. Note that because `z()` is still waiting for `func_a` value, `z()` **is not the final return value to the function caller.**

Going to `func_a`,as previously discussed, this returns `None`. `None` goes back to `z()`, however knowing that inside `z()` parameter is `None`, `func_c` **finally returns** `None`.

## Scope Example

- inside functions, variable that's defined outside can be accessible
- however, variable defined outside cannot be modified inside a function
    - workaround: use global variables, but not recommended

```python
def f(y):
    x = 1 #x is re-defined in scope of f
    x += 1
    print(x)
    return x

x = 5 #outside function
f(x) 
print(x)
```

[Visualization](https://pythontutor.com/render.html#code=def%20f%28y%29%3A%0A%20%20%20%20x%20%3D%201%20%23x%20is%20re-defined%20in%20scope%20of%20f%0A%20%20%20%20x%20%2B%3D%201%0A%20%20%20%20print%28x%29%0A%20%20%20%20return%20x%0A%0Ax%20%3D%205%20%23outside%20function%0Af%28x%29%20%0Aprint%28x%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

`f(x)` and x that's a global variable are two different x objects. One major mistake in this code is that it uses variable names that are completely the same.

x is global scope is defined as 5, when `f(x)` is called, 5 is mapped into function, so y in scope f is 5. x is re-defined in scope of f as 1, thus the print method in the function prints 2.

However, when x is returned as 2, the last print method in the global scope still prints 5. Why? This is because both variables are in different scopes. **Different print methods resort to variables in their respective scopes.**

The solution to this is replace the global print method `print(x)` to `print(f(x))`.

```python
def g(y):
    print(x) #x from outside g (global scope)
    print(x + 1)
    return x

x = 5
g(x)
print(x) #x inside g is picked up from scope g
```

In this case, function `g(y)` grabs x from the global scope, thus `print(x)` prints 5, and `print(x + 1)` prints 6. This is due to the function not having a re-defined x variable. x will still be returned 5. 

The last print method in global scope will still print 5, as previously mentioned.

```python
def h(y):
    x += 1
    return x

x = 5
h(x)
print(x)
```

[Visualization](https://pythontutor.com/render.html#code=def%20h%28y%29%3A%0A%20%20%20%20x%20%2B%3D%201%0A%20%20%20%20return%20x%0A%0Ax%20%3D%205%0Ah%28x%29%0Aprint%28x%29&cumulative=false&curInstr=5&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

This may be the most common mistake done when starting to learn variable binding in functions. This code will show:

```
UnboundLocalError: local variable 'x' referenced before assignment
```

This basically says since x is not defined in the function, python cannot find x to add 1 to. Remember that when mapping x = 5 to `h(x)`, ur essentially mapping y to 5 in scope f. So y is 5 instead. The proper solution to this is to change `x += 1` to `y += 1` and return y instead.

## Scope details

We will be looking at nested functions: [Visualization](https://pythontutor.com/render.html#code=def%20g%28x%29%3A%0A%20%20%20%20def%20h%28%29%3A%0A%20%20%20%20%20%20%20%20x%20%3D%20'abc'%0A%20%20%20%20x%20%3D%20x%20%2B%201%0A%20%20%20%20print%20%28'g%3A%20x%20%3D',%20x%29%0A%20%20%20%20h%28%29%0A%20%20%20%20return%20x%0A%0Ax%20%3D%203%0Az%20%3D%20g%28x%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
def g(x):
    def h():
        x = 'abc'
        return x
    x = x + 1
    print ('g: x =', x)
    print(h())
    return x

x = 3
z = g(x)
print(x)
```

`g(x)` is called, mapping 3 to the function. x is then re-defined as 4 in scope g, thus the print method after prints `g: x = 4`. **Through this whole process** `h()` **is ignored until it is called.**

Once `h()` is called, it looks back to it's definition, where x is re-defined as a string `abc` in scope h. `abc` is printed afterwards. However, instead of `abc`, 4 is returned instead.

Again, the last print method still prints what's x is defined in the global scope, which is 3.
