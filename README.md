
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

## Mathematical Induction

