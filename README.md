# Codewars Practices 3

## Thinkful - Number Drills: Blue and Red Marbles

You and a friend have decided to play a game to drill your statistical intuitions. The game works like this:

You have a bunch of red and blue marbles. To start the game you grab a handful of marbles of each color and put them into the bag, keeping track of how many of each color go in. You take turns reaching into the bag, guessing a color, and then pulling one marble out. You get a point if you guessed correctly. The trick is you only have three seconds to make your guess, so you have to think quickly.

You've decided to write a function, `guessBlue()` to help automatically calculate whether you should guess "blue" or "red". The function should take four arguments:

- the number of blue marbles you put in the bag to start
- the number of red marbles you put in the bag to start
- the number of blue marbles pulled out so far (always lower than - the starting number of blue marbles)
- the number of red marbles pulled out so far (always lower than - the starting number of red marbles)

`guessBlue()` should return the probability of drawing a blue marble, expressed as a float. For example, `guessBlue(5, 5, 2, 3)`should return `0.6`.

### Code

```python
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start-blue_pulled)/(blue_start-blue_pulled+red_start-red_pulled)
```

## Square(n) Sum

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for `[1, 2, 2]` it should return `9` because `1^2 + 2^2 + 2^2 = 9`.

### Code

```python
def square_sum(numbers):
    s = 0
    for i in numbers:
        s = s + i**2
    return s
```

## Merge Two Sorted Arrays Into One

You are given two sorted arrays that both only contain integers. Your task is to find a way to merge them into a single one, sorted in asc order. Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.

Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers. Remove duplicated in the returned result.

Examples:

```
* [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

* [1, 3, 5, 7, 9], [10, 8, 6, 4, 2] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

* [1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12] -> [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]
```

Happy coding!

### Code

```python
def merge_arrays(arr1, arr2):
    return sorted(set((arr1 + arr2)))
```

## Get Character From ASCII Value

Write a function `get_char()` / `getChar()` which takes a number and returns the corresponding ASCII char for that value.

Example:

```
get_char(65)
```

should return:

```
'A'
```

For ASCII table, you can refer to [here](http://www.asciitable.com/)

### Code

```python
def get_char(c):
    return chr(c)
```

## Volume of a Cuboid

Bob needs a fast way to calculate the volume of a cuboid with three values: the `length`, `width` and `height` of the cuboid. Write a function to help Bob with this calculation.

### Code

```python
def get_volume_of_cuboid(length, width, height):
    return int(length*width*height)
```

## String Repeat

Write a function that accepts an integer `n` and a string `s` as parameters, and returns a string of `s` repeated exactly `n` times.

Examples:

```
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
```

### Code

```python
def repeat_str(repeat, string):
    return string*repeat
```

## Is This My Tail?

Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.

The arguments will always be non empty strings, and normal letters.

### Code

```python
def correct_tail(body, tail):
    return tail == body[-1]
```

