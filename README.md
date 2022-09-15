# Codewars Practices 2

## Ones and Zeros

Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: `[0, 0, 0, 1]` is treated as `0001` which is the binary representation of `1`.

Examples:

```
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
```

However, the arrays can have varying lengths, not just limited to `4`.

### Code

```python
def binary_array_to_number(arr):
    value = 0
    arr.reverse()
    for i in range(len(arr)):
        value = value + arr[i] * 2**i
    return value
```

## Consecutive Strings

You are given an array(list) `strarr` of strings and an integer `k`. Your task is to return the **first** longest string consisting of k **consecutive** strings taken in the array.

Examples:
```
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
```

n being the length of the string array, if `n = 0` or `k > n` or `k <= 0` return "" (return `Nothing` in Elm, "nothing" in Erlang).

**Notes:**

consecutive strings : follow one after another without an interruption

```python
def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""
    else:
        consec = []
        for i in range(len(strarr)):
            if i+k > len(strarr):
                break
            else:
                consec.append("".join(strarr[i:(i+k)]))
        return max(consec, key=len)
```

## Will There Be Enough Space?

**The Story:**

Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.

**Task Overview:**

You have to write a function that accepts three parameters:

- `cap` is the amount of people the bus can hold excluding the driver.
- `on` is the number of people on the bus excluding the driver.
- `wait` is the number of people waiting to get on to the bus excluding the driver.

If there is enough space, return `0`, and if there isn't, return the number of passengers he can't take.

**Usage Examples:**

```
cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting
```

### Code

```python
def enough(cap, on, wait):
    return - (cap - (on + wait)) if cap - (on + wait) < 0 else 0
```

## Counting Sheep

Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

Example:

```
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
```

The correct answer would be `17`.

Hint: Don't forget to check for bad values like `null/undefined`

### Code

```python
def count_sheeps(sheep):
    return sheep.count(True)
```

## Sum Arrays

Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return `0`.

Examples:

Input: `[1, 5.2, 4, 0, -1]`

Output: `9.2`

Input: `[]`

Output: `0`

Input: `[-2.398]`

Output: `-2.398`

**Assumptions**

- You can assume that you are only given numbers.
- You cannot assume the size of the array.
- You can assume that you do get an array and if the array is empty, return `0`.

**What We're Testing**

We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
Advanced users may find this extremely easy and can easily write this in one line.

### Code

```python
def sum_array(a):
    return sum(a) if len(a) >= 1 else 0
```

