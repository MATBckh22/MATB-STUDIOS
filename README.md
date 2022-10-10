# Codewars Practices 5

## The Wide-mouthed Frog!

The wide-mouth frog is particularly interested in the eating habits of other creatures.

He just can't stop asking the creatures he encounters what they like to eat. But, then he meets the alligator who just LOVES to eat wide-mouthed frogs!

When he meets the alligator, it then makes a tiny mouth.

Your goal in this kata is to create complete the `mouth_size` method this method takes one argument animal which corresponds to the animal encountered by the frog. If this one is an `alligator` (case-insensitive) return `small` otherwise return `wide`

### Code

```python
def mouth_size(animal): 
    return 'small' if animal.lower() == 'alligator' else 'wide'
```

## Convert String to Camel Case

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Example:

`"the-stealth-warrior"` gets converted to `"theStealthWarrior"`
`"The_Stealth_Warrior"` gets converted to `"TheStealthWarrior"`

### Code

```python
def to_camel_case(text):
    text = text.replace("-","_")
    text = text.split("_")
    for i in range(1, len(text)):
        text[i] = text[i].capitalize()
    return ''.join(text)
```

## Disemvowel Trolls!

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata `y` isn't considered a vowel.

### Code

```python
def disemvowel(string_):
    vowels = 'aeiou'
    new_str = ''
    for i in string_:
        if i.lower() not in vowels:
            new_str = new_str + i
    return new_str 
```

## Get The Middle Character

You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

Example:

```
Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
```

A word (string) of length 0 < str < 1000. You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

### Code

```python
def get_middle(s):
    return s[len(s)//2-1:len(s)//2+1] if len(s)%2 == 0 else s[len(s)//2]
```

## Descending Order

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Example:

Input: `42145` Output: `54421`

Input: `145263` Output: `654321`

Input: `123456789` Output: `987654321`

### Code

```python
def descending_order(num):
    num_list = list(str(num))
    return int(''.join(sorted(num_list, reverse = True)))
```

## Is a Number Prime?

Define a function that takes an integer argument and returns a logical value `true` or `false` depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than `1` that has no positive divisors other than `1` and itself.

Requirements:

- You can assume you will be given an integer input.
- You can not assume that the integer will be only positive. You may be given negative numbers as well ( or `0` ).
- NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to $2^{31}$ ( or similar, depending on language ). Looping all the way up to `n`, or `n/2`, will be too slow.

### Code

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            return False
    return True
```

## Mexican Wave

The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal rhythm achieved in a packed stadium when successive groups of spectators briefly stand, yell, and raise their arms. Immediately upon stretching to full height, the spectator returns to the usual seated position.

The result is a wave of standing spectators that travels through the crowd, even though individual spectators never move away from their seats. In many large arenas the crowd is seated in a contiguous circuit all the way around the sport field, and so the wave is able to travel continuously around the arena; in discontiguous seating arrangements, the wave can instead reflect back and forth through the crowd. When the gap in seating is narrow, the wave can sometimes pass through it. Usually only one wave crest will be present at any given time in an arena, although simultaneous, counter-rotating waves have been produced.

**Task**

In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 

**Rules**

- The input string will always be lower case but maybe empty.
-  If the character in the string is whitespace then pass over it as if it was an empty seat

**Example**

```
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
```

### Code

```python
def wave(people):
    waves = []
    for i in range(len(people)):
        if people[i] == " ":
            pass
        else:
            waves.append(people[:i] + people[i].upper() + people[i+1:])
    return waves
```

## Break CamelCase

Complete the solution so that the function will break up camel casing, using a space between words.

Example:

```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```

### Code

```python
def solution(s):
    new_str = ''
    for i in s:
        if i.isupper():
            new_str = new_str + " " + i
        else:
            new_str = new_str + i
    return new_str
```

## Sum of Digits Raised To Their Consecutive Powers

The number `89` is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: `89 = 8^1 + 9^2`

The next number in having this property is `135`.

See this property again: `135 = 1^1 + 3^2 + 5^3`

We need a function to collect these numbers, that may receive two integers `a`, `b` that defines the range `[a, b]` (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases (input -> output):

```
1, 10 -> [1, 2, 3, 4, 5, 6, 7, 8, 9]

1, 100 -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
```

If there are no numbers of this kind in the range [a, b] the function should output an empty list:

```
90, 100 --> []
```

Enjoy it!!

### Code

```python
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    results = []
    for i in range(a, b+1):
        sum = 0
        s = str(i)
        for counter in range(len(s)):
            sum = sum + int(s[counter])**(counter+1)
        if sum == i:
            results.append(i)
    return results
```

## A Needle in The Haystack

Can you find the needle in the haystack?

Write a function `findNeedle()` that takes an `array` full of junk but containing one `"needle"`

After your function finds the needle it should return a message (as a string) that says:

`"found the needle at position "` plus the index it found the needle, so:

Example:

```
["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
```

### Code

```python
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'
```
## WeIrD StRiNg CaSe

Write a function `toWeirdCase` that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(`' '`). Spaces will only be present if there are multiple words. Words will be separated by a single space(`' '`).

Example:

```python
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
```

### Code

```python
def to_weird_case(words):
    words = words.split(" ")
    new_str = ''
    for i in words:
        for counter in range(len(i)):
            if counter == 0:
                new_str = new_str + i[0].upper()
            elif counter%2 == 0:
                new_str = new_str + i[counter].upper()
            else:
                new_str = new_str + i[counter].lower()
        new_str += " "
    return new_str[:-1]
```

## Will You Make It?

You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is `50` miles away! You know that on average, your car runs on about `25` miles per gallon. There are `2` gallons left.

Considering these factors, write a function that tells you if it is possible to get to the pump or not.

Function should return `true` if it is possible and `false` if not.

### Code

```python
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left >= distance_to_pump
```

## Chicken Sexing

Bob is a chicken sexer. His job is to sort baby chicks into a Male(M) and Female(F) piles. When bob can't guess can throw his hands up and declare it with a '?'.

Bob's bosses don't trust Bob's ability just yet, so they have paired him with an expert sexer. All of Bob's decisions will be checked against the expert's choices to generate a correctness score.

**Scoring Rules**

- When they agree, he gets 1 point.
- When they disagree but one has said '?', he gets 0.5 points.
- When they disagree completely, he gets 0 points.

### Code

```python
def correctness(bobs_decisions, expert_decisions): 
    points = 0
    for i in range(len(bobs_decisions)):
        if bobs_decisions[i] == expert_decisions[i]:
            points += 1
        elif bobs_decisions[i] == "?" or expert_decisions[i] == "?":
            points += 0.5
    return points
```

## Are You Playing Banjo

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

```
name + " plays banjo" 
name + " does not play banjo"
```

Names given are always valid strings.

### Code

```python
def are_you_playing_banjo(name):
    return f'{name} plays banjo' if name.lower()[0] == 'r' else f'{name} does not play banjo'
```

## Sum Of Intervals

Write a function called `sumIntervals`/`sum_intervals()` that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

**Intervals**

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: `[1, 5]` is an interval from 1 to 5. The length of this interval is 4.

**Overlapping Intervals**

List containing overlapping intervals:

```
[
   [1,4],
   [7, 10],
   [3, 5]
]
```

The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:

```
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ) => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ) => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ) => 19

sumIntervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ) => 100000030
```

```
sum_of_intervals([(1, 4), (7, 10), (3, 5)]) should get [2, 3, 4, 5, 8, 9, 10] and returns the length of it which is 7
```

**Test With Large Intervals**

Your algorithm should be able to handle large intervals. All tested intervals are subsets of the range `[-1000000000, 1000000000]`.

### Code

**Note that this is not the final solution due to performance issues:**

$O(n^2)$ Solution:

```python
def sum_of_intervals(intervals): 
    list_result = [] #empty list
    def interval_helper(tuple_test): 
        interval = []
        for i in range(tuple_test[0]+1, tuple_test[1]+1):
            if i not in list_result: #adds the intervals that doesn't overlap with existing ones in list
                interval.append(i)
        return interval
    for i in range(len(intervals)):
        list_result = list_result + interval_helper(intervals[i]) #calls the function and inputs a tuple in
    return len(list_result)
```

This kata only accepts $O(n \log n)$, $O(n)$ or below solutions.

## Pythagorean Triple

Given an array of 3 non-negative integers `a`, `b` and `c`, determine if they form a pythagorean triple.

A pythagorean triple is formed when:

$$c^2 = a^2 + b^2$$

where `c` is the largest value of `a`, `b`, `c`.

For example: `a = 3`, `b = 4`, `c = 5` forms a pythagorean triple, because $5^2 = 3^2 + 4^2$

**Return Values**

- `1` if `a`, `b` and `c` form a pythagorean triple
- `0` if `a`, `b` and `c` do not form a pythagorean triple
- For Python: return `True` or `False`

### Code

```python
def pythagorean_triple(integers):
    integers = sorted(integers)
    return int((integers[0])**2) + int((integers[1])**2) == int((integers[2]**2)) if integers[0] > 0 and integers[1] > 0 and integers[2] > 0 else 0
```

## Reversed Sequence

Build a function that returns an array of integers from n to 1 where `n>0`.

Example : `n=5` --> `[5,4,3,2,1]`

### Code

```python
def reverse_seq(n):
    return list(i for i in range(1, n+1))[::-1]
```

Shortened:

```python
def reverseseq(n):
    return list(range(n, 0, -1))
```

## Name Shuffler

Write a function that returns a string in which firstname is swapped with last name.

Example:

```
"john McClane" --> "McClane john"
```

### Code

```python
def name_shuffler(str_):
    return ' '.join(str_.split(" ")[::-1])
```

## Double Char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Example:

```
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
```

Good luck!

### Code

```python
def double_char(s):
    double = ''
    for i in range(len(s)):
        double = double + s[i]*2
    return double
```

## Invert Values

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```

You can assume that all values are integers. Do not mutate the input array/list.

### Code

```python
def invert(lst):
    return list(-lst[i] for i in range(len(lst)))
```