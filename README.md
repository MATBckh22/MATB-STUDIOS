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

