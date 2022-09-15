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

## Is He Gonna Survive?

A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

Return `True` if yes, `False` otherwise.

### Code

```python
def hero(bullets, dragons):
    return dragons*2 <= bullets
```

## Sum Without Highest and Lowest Number

Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example:

```
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
```

**Input Validation**

If an empty value ( `null`, `None`, `Nothing` etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return `0`.

### Code

```python
def sum_array(arr):
    if arr == None or len(arr) <= 1:
        return 0
    else:
        return sum(sorted(arr)) - sorted(arr)[0] - sorted(arr)[-1]
```

## Find The Position

When provided with a letter, return its position in the alphabet.

Input: `"a"`

Output: `"Position of alphabet: 1"`

### Code

```python
def position(alphabet):
    return "Position of alphabet: " + str(ord(alphabet)-96)
```

## Are They Opposite?

Give you two strings: `s1` and `s2`. If they are opposite, return `True`; otherwise, return `False`. Note: The result should be a boolean value, instead of a string.

The `opposite` means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string. Also take note of the edge case - if both strings are empty then you should return `false`/`False`.

**Examples:**

```
"ab","AB"     -> true
"aB","Ab"     -> true
"aBcd","AbCD" -> true
"AB","Ab"     -> false
"",""         -> false
```

### Code

```python
def is_opposite(s1,s2):
    return s1.swapcase() == s2 if len(s1) > 0 else False
```

## How Good Are You Really?

There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return `True` if you're better, else `False`!

**Note:**

Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

### Code

```python
def better_than_average(class_points, your_points):
    return your_points > int(sum(class_points)/len(class_points)) 
```

## Jenny's Secret Message

Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

Can you help her?

### Original Code

```python
def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"
```

### Debugged Code

```python
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
```

## Online RPG player to qualifying stage?

Let's imagine we have a popular online RPG. A player begins with a score of 0 in class E5. A1 is the highest level a player can achieve.

Now let's say the players wants to rank up to class E4. To do so the player needs to achieve at least 100 points to enter the qualifying stage.

Write a script that will check to see if the player has achieved at least 100 points in his class. If so, he enters the qualifying stage.

In that case, we return, `"Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."`.

Otherwise return, `False`/`false` (according to the language in use).

### Code

```python
def playerRankUp(pts):
     return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." if pts >= 100 else False
```

## Beginner Series #4: Cockroach

The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

For example:

```
1.08 --> 30
```

Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

### Code

```python
def cockroach_speed(s):
    return s // 0.036
```

## Well of Ideas - Easy Version

For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return `'Publish!'`, if there are more than 2 return `'I smell a series!'`. If there are no good ideas, as is often the case, return `'Fail!'`.

### Code

```python
def well(x):
    counter = 0
    for i in x:
        if i == 'good':
            counter += 1
    if counter == 1 or counter == 2:
        return "Publish!"
    elif counter > 2:
        return "I smell a series!"
    else:
        return "Fail!"
```

## Capitalization and Mutability

Your coworker was supposed to write a simple helper function to capitalize a string (that contains a single word) before they went on vacation.

Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works as intended (i.e. make the first character in the string "word" upper case).

Don't worry about numbers, special characters, or non-string types being passed to the function. The string lengths will be from 1 character up to 10 characters, but will never be empty.

### Code

```python
def capitalize_word(word):
    return word[0].upper() + word[1:]
```

Simplified Code:

```python
def capitalize_word(word):
    return word.capitalize()
```

## Alternating Case

Define `String.prototype.toAlternatingCase` (or a similar function/method such as `to_alternating_case`/`toAlternatingCase`/`ToAlternatingCase` in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. 

For example:

```python
"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"
"hello WORLD".toAlternatingCase() === "HELLO world"
"HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
"12345".toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
"1a2b3c4d5e".toAlternatingCase() === "1A2B3C4D5E"
"String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
```

As usual, your function/method should be pure, i.e. it should not mutate the original string.

### Code

```python
def to_alternating_case(string):
    print(string)
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in string:
        if i in s:
            result = result + i.lower()
        else:
            result = result + i.upper()
    return result
```

Simplified Code:

```python
def to_alternating_case(string):
    return string.swapcase()
```

## Quarter of The Year

Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

### Code

```python
def quarter_of(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    else:
        return 4
```

## Remove String Spaces

Simple, remove the spaces from the string, then return the resultant string.

### Code

```python
def no_space(x):
    return x.replace(" ", "")
```

## Find The Smallest integer in The Array

Given an array of integers your solution should find the smallest integer.

For example:

- Given `[34, 15, 88, 2]` your solution will return `2`
- Given `[34, -345, -1, 100]` your solution will return `-345`

You can assume, for the purpose of this kata, that the supplied array will not be empty.

### Code

```python
def find_smallest_int(arr):
    return min(arr)
```

## Fake Binary

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

### Code

```python
def fake_bin(x):
    s = ''
    for i in x:
        if int(i) < 5:
            s = s + '0'
        else:
            s = s + '1'
    return s
```

