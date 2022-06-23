
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

a programming technique where a **function aclls itself**

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
