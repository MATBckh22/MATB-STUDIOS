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
def get_data(aTuple):
    nums = ()    # empty tuple
    words = ()
    for t in aTuple:
        # concatenating with a singleton tuple
        nums = nums + (t[0],)   
        # only add words haven't added before
        if t[1] not in words:   
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)
```
**Multiple data can be collected simultaneously** using tuples. With this example we initially set nums and words as an empty tuple. Inside the for loop **both tuples are replaced with new tuples that corresponds to a certain set of data.** In this case nums always collects the `(t[0],)` position of the input, which is the int; words will always collect `(t[1],)` position, which is the string. 

Do note function `min()` and `max()` select the minimum and maximum value given from the input.

`unique_words` is a variable to collect the total number of **unique** words (defined as `if t[1] not in words:`)

Thus, the function returns three variables.

```
    def get_data(aTuple):
        nums = ()    # empty tuple
        words = ()
        for t in aTuple:
            # concatenating with a singleton tuple
            nums = nums + (t[0],)   
            # only add words haven't added before
            if t[1] not in words:   
                words = words + (t[1],)
        min_n = min(nums)
        max_n = max(nums)
        unique_words = len(words)
        return (min_n, max_n, unique_words)
# apply to any data you want!
tswift = ((2014,"Katy"),
          (2014, "Harry"),
          (2012,"Jake"), 
          (2010,"Taylor"), 
          (2008,"Joe"))    
(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year, 
        "Taylor Swift wrote songs about", num_people, "people!")
```
This is an example given from the lecture where data can be sorted to count how many people Taylor Swift has written songs about.

## Lists

Lists contains elements to create an ordered sequence, accessible by index. similar to tuples, a list is denoted by [ ].

### **Lists are mutable objects**
U can change elements in a list **directly**, this is not allowed in strings and tuples.
```
>>> L = [2,'a',4,[1,2,3]]
>>> len(L)
4
>>> L[0] = 1
>>> print(L)
[1, 'a', 4, [1, 2, 3]]
```
Similar operations can be done:
```
>>> len(L)
4
>>> L[2]
4
>>> L[3]
[1, 2, 3]
```
A variable can be given values to subtract from other values in `L[]` to print an element:
```
[1, 'a', 4, [1, 2, 3]]
>>> i = 3
>>> L[i-1]
4
```
## Iterating Over a List

This is a common pattern to compute the **sums of elements:**
```
total = 0
L = [1,2,3,4,5]
for i in range(len(L)):
    total += L[i]
print(total)
```
`total` will be printed 15 in the terminal.

We can modify this for a slightly more readable code:
```
total = 0
L = [1,2,3,4,5]
for i in L:
    total += i
print(total)
```
## Operations On Lists: Add/Remove

Since lists are mutable, we can add and remove elements from it. 
### Adding Elements
Here we use `append` to add elements on the end of the list:
```
>>> L = [1,2,3]
>>> L.append(5)
>>> print(L)
[1, 2, 3, 5]
>>>
```
Operator `+` can be used to make a new list combining multiple existing lists:
```
>>> L1 = [1,2,3]
>>> L2 = [4,5,6]
>>> L3 = L1+L2
>>> print(L3)
[1, 2, 3, 4, 5, 6]

```
`extend` can be used to mutate a list:
```
>>> L = [1,2,3]
>>> L.extend([4,5,6])
>>> print(L)
[1, 2, 3, 4, 5, 6]
```
### Removing Elements

U can use `L.remove()` to remove a specific element, python looks for the element from the parentheses and deletes it from the list, two rules to keep note:

- if element occurs multiple times, removes first occurrence
- if element is not on list, error feedback is given

```
>>> L = [1,2,3,4,5,6]
>>> L.remove(2)
>>> print(L)
[1, 3, 4, 5, 6]
```
```
>>> L = [1,2,3,3,4,5]
>>> L.remove(3)
>>> print(L)
[1, 2, 3, 4, 5]
```
```
>>> L = [1,2,3,4,5]
>>> L.remove(6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```
U can also delete a specific index using `del(L[index])`:
```
>>> L = [1,2,3,4,5]
>>> del(L[2])
>>> print(L)
[1, 2, 4, 5]
```
`L.pop()` deletes the element on the end of the list and returns it:
```
>>> L = [1,2,3,4,5]
>>> L.pop()
5
>>> print(L)
[1, 2, 3, 4]
```
*Note: Use it cautiously in functions, it might return* `None`

## Converting Lists - Strings

### Strings to Lists

After setting a string variable, u can convert it to a list using `list()` *including spaces*:
```
>>> s = "python cool"
>>> list(s)
['p', 'y', 't', 'h', 'o', 'n', ' ', 'c', 'o', 'o', 'l']
```
Python returns the list with it's individual elements back after converting it.
**However, s will remain as a string. Printing s will still display it's string form:**
```
>>> s = "python cool"
>>> list(s)
['p', 'y', 't', 'h', 'o', 'n', ' ', 'c', 'o', 'o', 'l']
>>> print(s)
python cool
>>> print(list(s))
['p', 'y', 't', 'h', 'o', 'n', ' ', 'c', 'o', 'o', 'l']
```
`s.split` can be used to split a string on a character, splits on spaces if called without a parameter:
```
>>> s.split("p")
['', 'ython cool']
```
*note that characters are not individually separated, comparing to* `list()`
```
>>> s = "phyton cool"
>>> s.split()
['phyton', 'cool']
```

### Lists to Strings

Use `''.join()` to turn a list of characters into a string:
```
>>> L = ["1","2","3"]
>>> ''.join(L)
'123'
```
adding characters in between quotes will result in the characters be placed between every element:
```
>>> L = ["1","2","3"]
>>> "add".join(L)
'1add2add3'
```
## Other List Operators

### `sort()` vs `sorted()` vs `reverse()`

`sort()` and `sorted()` can be used to sort elements in an ascending order:
```
>>> L = [4,2,3,1]
>>> sorted(L)
[1, 2, 3, 4]
>>> print(L)
[4, 2, 3, 1]
```
`sorted()` **returns the sorted list but doesn't mutate it**
```
>>> L = [4,2,3,1]
>>> L.sort()
>>> print(L)
[1, 2, 3, 4]
```
`sort()` **doesn't return the sorted list but does mutate it**

`reverse()` mutates the lists as well:
```
>>> L = [1,4,2,3]
>>> L.reverse()
>>> print(L)
[3, 2, 4, 1]
```
*note:* `reverse()` *only reverse the positions of elements,* ***it doesn't sort the elements in a descending order mathematically***

### Other operations can be seen here:

https://docs.python.org/3/tutorial/datastructures.html

## Lists in Memory and Aliases

*Minor warning for using lists*
- lists are mutable
- behave differently than immutable types
- is an object in memory
- variable name points to object

Any variable pointing to that object is **affected**, so working with lists might have **side effects**

Example below:
```
>>> warm = ['red','yellow','orange']
>>> hot = warm
>>> hot.append('pink')
>>> print(hot)
['red', 'yellow', 'orange', 'pink']
>>> print(warm)
['red', 'yellow', 'orange', 'pink']
```
**Assigning a variable to another variable, changing either one will affect the other.** This is the distinct difference between strings and lists. List is special for it's mutability.

## Cloning Lists

We can use this speciality to clone lists. `[:]` is used to copy a list from a variable to another:
```
>>> coding_language = ['python','java','html']
>>> programming_language = coding_language[:]
>>> programming_language.append('C')
>>> print(programming_language)
['python', 'java', 'html', 'C']
>>> print(coding_language)
['python', 'java', 'html']
```
`[:]` can be seen as `[0:len()]`. This method is desirable to prevent the side effect. Cloning a list allows python to **create a copy from the existing list onto a new list**, so changing a variable won't affect the other.

## Sorting Lists

example is given at `sort()` vs `sorted()` vs `reverse()`. Here we will be specifically talking about `sort()` vs `sorted()`:
```
>>> warm = ['orange','yellow','red']
>>> sortedwarm = warm.sort()
>>> print(warm)
['orange', 'red', 'yellow']
>>> print(sortedwarm)
None
```
`sort()` returned nothing because it already mutated the list, so `sortedwarm` prints out `None`.
```
>>> cool = ['blue','aqua','green']
>>> sortedcool = sorted(cool)
>>> print(cool)
['blue', 'aqua', 'green']
>>> print(sortedcool)
['aqua', 'blue', 'green']
```
`sorted()` returns the sorted list but doesn't mutate it, so `sortedcool` can be printed out.

## Lists of Lists of Lists of...

Nested lists are allowed but side effects may be prevalent after mutation.

```
>>> warm = ['yellow','orange']
>>> hot  = ['red']
>>> brightcolors = [warm]
>>> brightcolors.append(hot)
>>> print(brightcolors)
[['yellow', 'orange'], ['red']]
>>> hot.append('pink')
>>> print(hot)
['red', 'pink']
>>> print(brightcolors)
[['yellow', 'orange'], ['red', 'pink']]
```
This test begins with two variables `warm` and `hot`. We then assign `brightcolors` variable to contain elements in `warm`. so `brightcolors` has `[['yellow','orange']]`.

Adding `hot` into `brightcolors` makes `brightcolors` a variable containing elements from `warm` and `hot`.

What if we add elements to existing variables like `hot`? Answer: `brightcolors` will be affected as well.

### Be cautious when adding or removing elements from variables, especially when handling lists in for loops. Use the clone operator when necessary to avoid side effects.
