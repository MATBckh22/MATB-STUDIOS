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

