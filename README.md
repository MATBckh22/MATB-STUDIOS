# Tuples, Lists, Aliasing, Mutability, and Cloning

## Tuples
Ordered sequence of elements, **can mix element types**, *immutable*
```
>>> t = (2,"something",3)
>>> t[0]
2
>>> tuples = t + ("here",21)
>>> print(tuples)
(2, 'something', 3, 'here', 21)
>>> tuples[1:5]
('something', 3, 'here', 21)
>>> len(tuples)
5
>>> tuples[1]=5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
Tuples are similar to strings, they contain elements where `t[start,stop,step]` is used to slice tuples. They are also immutable, u can't change an element directly in a tuple.

U can also mix existing tuples with other elements. 

## Applying Tuples 

- used to conveniently swap variable values

```
#this is not allowed
x = y
y = x

#this is allowed
temp = y
y = x
x = temp

#this is more readable
(x,y) = (y,x)
```
Applying this in a function, u can **return more than one value:**
```
def quotient_and_remainder(x,y):
    q = x//y
    r = x%y
    return(q,r)
(quot,rem) = quotient_and_remainder(4,5)
```
`(quot,rem) = quotient_and_remainder(4,5)` calls the function, mapping 4 and 5 into the function. Function runs through the operations and returns the values back.

`x//y` is the product of a division rounded to the nearest whole number.

## Manipulating Tuples
Iterating over tuples:
```
