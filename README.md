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

## Sum of Differences in Array

Your task is to sum the differences between consecutive pairs in the array in descending order.

Example:

```
[2, 1, 10]  -->  9
```

In descending order: `[10, 2, 1]`

Sum: `(10 - 2) + (2 - 1) = 8 + 1 = 9`

If the array is empty or the array has only one element the result should be `0`.

### Code

```python
def sum_of_differences(arr):
    if len(arr) <= 1:
        return 0
    arr = sorted(arr, reverse = True)
    print(arr)
    differences = []
    for i in range(len(arr)):
        if i == len(arr)-1:
            break
        differences.append(arr[i] - arr[i+1])
    return sum(differences)
```

## Sum A List But Ignore Any Duplicates

Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.

### Code

```python
def sum_no_duplicates(l):
    unique_nums = []
    for i in l:
        if l.count(i) == 1:
            unique_nums.append(i)
    return sum(unique_nums)
```

## List Flitering

In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example:

```python
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```

### Code

```python
def filter_list(l):
    a=[]
    for i in l:
        if type(i)==int: a.append(i)
    return a
```

## Split Strings

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Example:

```
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
```

### Code

```python
def solution(s):
    str_split = []
    for i in range(0, len(s), 2):
        if i+2 > len(s):
            str_split.append(''.join(s[i]+'_'))
            return str_split
        str_split.append(''.join(s[i]+s[i+1]))
    return str_split
```

## Highest and Lowest

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

```
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
```

- All numbers are valid `Int32`, no need to validate them.
- There will always be at least one number in the input string.
- Output string must be two numbers separated by a single space, and highest number is first.

### Code

```python
def high_and_low(numbers):
    numbers = numbers.split(" ")
    return f"{max(numbers, key=int)} {min(numbers, key=int)}"
```

## Find The Unique Number

There is an array with some numbers. All numbers are equal except for one. Try to find it!

```python
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

### Code

```python
def find_uniq(arr):
    for i in list(set(arr)):
        if arr.count(i) == 1:
            return i
```

## Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

```python
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
```

### Code

```python
def move_zeros(lst):
    new_lst = []
    zero_count = lst.count(0)
    for i in lst:
        if i != 0:
            new_lst.append(i)
    for counter in range(zero_count):
        new_lst.append(0)
    return new_lst
```

## Detect Pangram

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence `"The quick brown fox jumps over the lazy dog"` is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

### Code

```python
def is_pangram(s):
    s = s.lower()
    alphabets = []
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            alphabets.append(i)
    alphabets = list(set(alphabets))
    return len(alphabets) == 26
```

## Human Readable Duration Format

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns `"now"`. Otherwise, the duration is expressed as a combination of `years`, `days`, `hours`, `minutes` and `seconds`.

It is much easier to understand with an example:

```
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
```

**For the purpose of this Kata, a year is 365 days and a day is 24 hours.**

Note that spaces are important.

### Detailed Rules

The resulting expression is made of components like` 4 seconds,` `1 year`, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space `(", ")`. Except the last component, which is separated by `" and "`, just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, `1 second and 1 year` is not correct, but `1 year and 1 second` is.

Different components have different unit of times. So there is not repeated units like in `5 seconds and 1 second`.

A component will not appear at all if its value happens to be zero. Hence, `1 minute and 0 seconds` is not valid, but it should be just `1 minute`.

A unit of time must be used "as much as possible". It means that the function should not return `61 seconds`, but `1 minute and 1 second` instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

### Code

```python
def format_duration(seconds):
    print(seconds)
    sentence = ''
    if seconds == 1:
        return '1 second'
    elif seconds == 60:
        return '1 minute'
    elif seconds == 3600:
        return '1 hour'
    elif seconds == 6400:
        return '1 day'
    elif seconds == 31536000:
        return '1 year'
    elif seconds == 0:
        return 'now'
    else:
        if 120 <= seconds < 3600 and seconds%60 == 0:
            return f'{seconds//60} minutes'
        if seconds > 31536000:
            if 31536001 <= seconds < 31536000*2:
                sentence = '1 year, '
                seconds = seconds%31536000
            else:
                sentence = f'{seconds//31536000} years, '
                seconds = seconds%31536000
        if seconds > 86400:
            if 86401 <= seconds < 86400*2:
                sentence = sentence + '1 day, '
                seconds = seconds%86400
            else:
                sentence = sentence + f'{seconds//86400} days, '
                seconds = seconds%86400
        if seconds > 3600:
            if 3601 <= seconds < 3600*2:
                sentence = sentence + '1 hour, '
                seconds = seconds%3600
            else:
                sentence = sentence + f'{seconds//3600} hours, '
                seconds = seconds%3600
        if seconds > 60:
            if 61 <= seconds < 120:
                sentence = sentence + '1 minute and '
                seconds = seconds%60
            else:
                if seconds%60 == 0:
                    return sentence[:-2] + f' and {seconds//60} minutes'
                sentence = sentence + f'{seconds//60} minutes and '
                seconds = seconds%60
        if seconds < 60:
            if seconds == 1:
                sentence = sentence + '1 second'
            else:
                sentence = sentence + f'{seconds} seconds'
        return sentence
```

## Bit Counting

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of `1234` is `10011010010`, so the function should return `5` in this case.

### Code

```python
def count_bits(n):
    s = ''
    while n != 0:
        if n%2 == 0:
            n = n/2
            s = s + '0'
        else:
            n = (n-1)/2
            s = s + '1'
    s = s[::-1]
    return s.count('1')
```

## Replace With Alphabet Position

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

`"a" = 1`, `"b" = 2`, etc.

Example:

```
alphabet_position("The sunset sets at twelve o' clock.")
```

Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"` ( as a string )

### Code

```python
def alphabet_position(text):
    text = text.lower()
    alphabets_to_numbers =  ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in text:
        if i in alphabets:
            alphabets_to_numbers = alphabets_to_numbers + f'{str(ord(i)-96)} '
    return alphabets_to_numbers[:-1]
```

## Integer Depth

The `depth` of an integer `n` is defined to be how many multiples of `n` it is necessary to compute before all `10` digits have appeared at least once in some multiple.

Example:

```
let see n=42

Multiple         value         digits     comment
42*1              42            2,4 
42*2              84             8         4 existed
42*3              126           1,6        2 existed
42*4              168            -         all existed
42*5              210            0         2,1 existed
42*6              252            5         2 existed
42*7              294            9         2,4 existed
42*8              336            3         6 existed 
42*9              378            7         3,8 existed
```

Looking at the above table under `digits` column you can find all the digits from `0` to `9`, Hence it required `9` multiples of `42` to get all the digits. So the depth of `42` is `9`. Write a function named `computeDepth` which computes the depth of its integer argument.Only positive numbers greater than zero will be passed as an input.

### Code

```python
def compute_depth(n):
    print(n)
    digits = []
    number = 0
    for i in range(1, 101):
        if len(digits) == 10:
            return i-1
        number = n*i
        for counter in str(number):
            if counter not in digits:
                digits.append(counter)
```

## Does My Number Look Big In This?

A [Narcissistic Number](https://en.wikipedia.org/wiki/Narcissistic_number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcisstic:

```
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
```

and 1652 (4 digits), which isn't:

```
 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
```

The Challenge:

Your code must return **true** or **false** (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10. This may be **True** and **False** in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

### Code

```python
def narcissistic( value ):
    sum=0
    for i in str(value):
        sum = sum+int(i)**len(str(value))
    return sum==value
```

