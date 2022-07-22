# Branching and Iteration

## String

Enclosed in quotation marks or single quotes, exp:
`hi = "hello there"`

notice `" "` is defined as space, exp:

```
name = ABC
greeting = hi + " " + name
print(greeting)
```

Difference in printing , and + between objects
```
>>> print("hi","chong")
hi chong
>>> print("hi"+"chong")
hichong
```

## Input: `input("")`
prints whatever is in the quotes, the string user types next will be binded as a variable (input into memory), exp:
```
>>> text = input("type something down below")
type something down below
hello
>>> print(text)
hello
```
## Cast: Input For Numbers
binding numbers (only when ur working with numbers):

```
>>> num = int(input("type a number"))
type a number25
>>> print(5*num)
125
```

## Comparisons
Only variables, evaluate to a boolean:

```
i > j
i >= j
i < j
i <= j
i == j  #equality test, True if i is the same as j
i != j  #inequality test, True if i not the same as j
```

Test:

```
>>> i = 5
>>> j = 6
>>> i<j
True
>>> i>j
False
```

## Logic Operators on `boolean`

Assume `a` and `b` are variable names with Boolean values:

| A | B | A and B | A or B |
| - | - | - | - |
| `True` | `True` | `True` | `True`
| `True` | `False` | `False` | `True`
| `False` | `True` | `False` | `True`
| `False` | `False` | `False` | `False`

Logic operators can be used in code to connect variables:
- `not a`
    - `True` if `a` is `False`
    - `False` if `a` is `True`
- `a and b`
    - `True` if both are `True`
- `a or b`
    - `True` if either one is `True` or both are `True`

```
pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)
derive = True
drink = False
both = drink and derive
print(both)
```

## if else vs elif else (Control Flow and Branching)

```
if <condition>:
<expression>
<expression>
...
else:
<expression>
<expression>
```

Decision is made from the condition under if that is true or false, expressions is evaluated or executed when condition is true.

```
if <condition>:
<expression>
<expression>
...
elif <condition>:
<expression>
<expression>
...
else:
<expression>
<expression>
```
`elif` is made for a separate condition if the first condition is not `True`. If all are `False`, the last expression under `else` is executed

*see how multiple conditions can have shorter strings of code using elif vs if*

### `if else` 
```
x = float(input("type a number to compare"))
y = float(input("type another number to compare"))
if x > y:
    print("x is bigger")
    print("y is smaller")
if y > x:
    print("y is bigger")
    print("x is smaller")
if x == y:
    print("they're the same!")
```

### `elif`
```
x = float(input("type a number to compare"))
y = float(input("type another number to compare"))
if x > y:
    print("x is bigger")
    print("y is smaller")
elif y > x:
     print("y is bigger")
     print("x is smaller")
else:
     print("they're the same!")
```

# `while` loops

`if else` infinite loops can be turned into `while` loops:

```
while <condition>:
  <expression>
<expression>
```

`<condition>` evaluates to a Boolean. If <condition> is `True`, do all the steps inside the `while` code block. Check `<condition>` again, repeat until <condition> it's `False`.

# `for` loops
    
Acts as a $n = n+1$ loop shortcut, `while` vs `for` below:
    
```
n = 0
while n < 5:
print(n)
n = n+1
```

`for` loop shortcut:

```
for n in range(5):
print(n)
```
            
Each time through the loop, `<variable>` takes a value, first time, `<variable>` starts at the smallest value, next time, `<variable>` gets the prev value + 1
etc. `range()` **creates a sequence from 0 to whatever number u set, in this case it's 0-5**

## Controlling `range()` 

`range(start, stop, step)`, default: start = 0, step = 1:
    
```
mysum = 0
for i in range(7, 10):
mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2):
mysum += i
print(mysum)
```

*note: doesn't include stop values*

## `break`
    
`break` acts as an immediate exit from the `while` loop when a condition is met and skips the remaining expressions after, but only exits it's innermost loop:

```
while <condition_1>:
  while <condition_2>:
    <expression_a>
    break
        <expression_b>
    <expression_c>
```
        
Example: 
        
```
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
      break
    mysum += 1
print(mysum)
```

Since `i` is 5 inside the for loop, when `mysum += i` occurs `mysum` will equal to 5 as well.

Notice that because `mysum` is 5 so it fits the if block's condition, hence the for loop will break.
        
## `for` vs `while` loops

| `for` | `while` |
| - | - |
| **know** number of iterations | iterations are **unbounded**
| end early via `break` | end early via `break`
| uses a **counter** | **uses a counter but must initialize before loop and increment it inside loop**
| can rewrite a `for` loop using a `while` loop | may not be able to rewrite a `while` loop using a `for` loop
