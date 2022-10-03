# Codewars Practices 4

## Playing With Digits

Some numbers have funny properties. For example:

```
89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
```

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

> we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.

In other words:

> Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

```
dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
```

### Code

```python
def dig_pow(n, p):
    sum=0
    for i in str(n):
        sum=sum+int(i)**p
        p+=1
    if sum%n==0:
        return(int(sum/n))
    else:
        return(-1)
```

## Counting Duplicates

Count the number of Duplicates

Write a function that will return the count of **distinct case-insensitive** alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example:

```python
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
```

### Code

```python
def duplicate_count(text):
    text = text.lower()
    unique_chars = list(set(text))
    counter = 0
    for i in unique_chars:
        if text.count(i) >= 2:
            counter += 1
    return counter
```

## Find The Parity Outlier

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.

Example:

```
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
```

### Code

```python
def find_outlier(integers):
    odd_counter = []
    even_counter = []
    for i in integers:
        if i%2 == 0:
            even_counter.append(i)
        else:
            odd_counter.append(i)
    if len(odd_counter) == 1:
        return odd_counter[0]
    else:
        return even_counter[0]
```

## Create Phone Number

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:

```python
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```

The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

### Code

```python
def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
```

## Array.diff

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list `a`, which are present in list `b` keeping their order:

```python
array_diff([1,2],[1]) == [2]
```

If a value is present in `b`, all of its occurrences must be removed from the other:

```python
array_diff([1,2,2,2,3],[2]) == [1,3]
```

### Code

```python
def array_diff(a, b):
    for i in b:
        if i in a:
            try:
                while True:
                    a.remove(i)
            except ValueError:
                pass
    return a
```

## Reverse If There's 5 Letters

Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present:

```
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
```

### Code

```python
def spin_words(sentence):
    sentence_break = sentence.split(" ")
    new_sentence = []
    for i in sentence_break:
        if len(i) >= 5:
            new_sentence.append(i[::-1])
        else:
            new_sentence.append(i)
    return " ".join(new_sentence)
```

## Find The Odd Int

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Example:

```
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
```

### Code

```python
def find_it(seq):
    for i in set(seq):
        if seq.count(i) == 1 or (seq.count(i)-1)%2 == 0:
            return i
```

## Sum Of Digits / Digital Root

[Digital root](https://brilliant.org/wiki/digital-root/) is the recursive sum of all the digits in a number.

Given `n`, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Example:

```
 16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
```

### Code

```python
def digital_root(n):
    if n < 10: return n
    n_str = str(n)
    while int(n_str) >= 10:
        sum = 0
        for i in str(n_str):
            sum += int(i)
        n_str = sum
    else:
        return sum
```

## Take a Ten Minute Walk

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return `true` if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return `false` otherwise.

> Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

### Code

```python
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        x = 0
        y = 0
        for i in walk:
            if i == 'n': y += 1
            elif i == 's': y -= 1
            elif i == 'e': x += 1
            elif i == 'w': x -= 1
        return x == 0 and y == 0
```

## Persistent Burger

Write a function, `persistence`, that takes in a positive parameter `num` and returns its multiplicative persistence, which is the number of times you must multiply the digits in `num `until you reach a single digit.

Example:

```
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
```

### Code

```python
def persistence(n):
    print(n)
    if n < 10: return 0
    n_str = str(n)
    counter = 0
    while int(n_str) >= 10:
        mult = 1
        for i in str(n_str):
            mult *= int(i)
        n_str = mult
        counter += 1
    else:
        return counter
```

## Find The First Non-consecutive Number

Your task is to find the first element of an array that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the array.

E.g. If we have an array `[1,2,3,4,6,7,8]` then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

If the whole array is consecutive then return `None`.

### Code

```python
def first_non_consecutive(arr):
    counter = arr[0]
    for i in arr:
        if counter != i:
            return i
        counter += 1
    return None
```

## Snail Sort

Given an `n x n` array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

```
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
```

For better understanding, please follow the numbers of the next array consecutively:

```
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
```

This image will illustrate things more clearly:

![Snail Sort](https://miro.medium.com/max/640/1*f3yEq5LHQIq0Vk2K_9kuRw.png)

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The `0x0` (empty matrix) is represented as en empty array inside an array `[[]]`.

### Code

```python
def snail(snail_map):
    if snail_map == [[]]:
        return []
    elif snail_map == [[1]]:
        return [1]
    sorted_list = []
    cloned = snail_map[:]
    def snail_mapper(snail_array):
        sorted_first = []
        sorted_last = []
        snail_helper_last = []
        snail_helper_first = []
        sorted_first = snail_array[0]
        print(sorted_first)
        cloned.remove(cloned[0])
        sorted_last = (snail_array[-1])[::-1]
        print(sorted_last)
        cloned.remove(cloned[-1])
        for i in cloned:
            snail_helper_last.append(i[-1])
            del i[-1]
        print(snail_helper_last)
        for i in cloned:
            snail_helper_first.append(i[0])
            del i[0]
        snail_helper_first = snail_helper_first[::-1]
        print(snail_helper_first)
        z = sorted_first + snail_helper_last + sorted_last + snail_helper_first
        return z
    while len(cloned) > 0:
        if len(cloned) == 1:
            sorted_list = sorted_list + cloned[0]
            break
        sorted_list = sorted_list + snail_mapper(cloned)
    return sorted_list
```

## Thinkful - Logic Drills: Traffic light

You're writing code to control your town's traffic lights. You need a function to handle each change from green, to `yellow`, to `red`, and then to `green` again.

Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

For example, when the input is `green`, output should be `yellow`.

### Code

```python
def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    else:
        return 'green'
```

## The Maximum Sum Value of Ranges - Simple Version

```python
Given arr = [1,-2,3,4,-5,-4,3,2,1], 
       range = [[1,3],[0,4],[6,8]]
 should return 6
 
 calculation process:
 range[1,3] = arr[1]+arr[2]+arr[3] = 5
 range[0,4] = arr[0]+arr[1]+arr[2]+arr[3]+arr[4] = 1
 range[6,8] = arr[6]+arr[7]+arr[8] = 6
 So the maximum sum value is 6
```

- `arr` always has at least 5 elements
- `range` always has at least 1 element
- All inputs are valid

Example:

```python
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,3],[0,4],[6,8]]) === 6
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,3]]) === 5
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,4],[2,5]]) === 0
```

### Code

```python
def max_sum(arr,ranges): 
    sums = []
    for i in ranges:
        range_sum = 0
        for s in range(i[0],i[1]+1):
            if i[1]+1 > len(arr):
                continue
            range_sum = range_sum + arr[s]
        sums.append(range_sum)
    return max(sums)
```

## The Maximum Sum Value of Ranges - Challenge Version

>When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process -myjinxin2015

Given a list of integers `A`, for each pair of integers `(first, last)` in list `ranges`, calculate the sum of the values in `A` between indices `first` and `last` (both inclusive), and return the greatest resulting sum.

```
A = [1, -2, 3, 4, -5, -4, 3, 2, 1]
ranges = [(1, 3), (0, 4), (6, 8)]

result = 6
```

Notes:

- The list of ranges will never be empty
- This is a challenge version, you should implement an efficient algorithm to avoid timing out

**About random testcases:**

- Small tests: 100 testcases
    - each integers-list : 5-20 elements
    - each ranges-list : 1-6 elements
- Big tests: 50 testcases
    - each integers-list : 100000 elements
    - each ranges-list : 10000 elements

### Code

```python
from itertools import accumulate

def max_sum(a, ranges):
    new = list(accumulate(a)) + [0]
    return max(new[j] - new[i-1] for i, j in ranges)
```