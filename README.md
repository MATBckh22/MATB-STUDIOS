# Codewars Practices

Welcome to [Codewars](https://www.codewars.com/) Archive Katas! This is a section specifically for MATB members to post their own exercises (katas) of code, here we will be using mainly practices from codewars, though other platforms or homework are welcomed!

## Duplicate Encoder

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Example:

```python
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
```

### Code

```python
def duplicate_encode(word):
    x = word.casefold()
    output = ''
    for char in x:
        if x.count(char) > 1:
            output = output + ")"
        else:
            output = output + "("
    return output
```
## Pyramid Height 

Your task is to calculate the maximum possible height of a perfectly square pyramid (the number of complete layers) that we can build, given n number of cubes as the argument.

- The top layer is always only 1 cube and is always present.
- There are no hollow areas, meaning each layer must be fully populated with cubes.
- The layers are thus so built that the corner cube always covers the inner 25% of the corner cube below it and so each row has one more cube than the one below it.
- If you were given only 5 cubes, the lower layer would have 4 cubes and the top 1 cube would sit right in the middle of them, where the lower 4 cubes meet.

*If you were given 14 cubes, you could build a pyramid of 3 layers, but 13 wouldn't be enough as you would be missing one cube, so only 2 layers would be complete and some cubes left over!*

What is the tallest pyramid possible we can build from the given number of cubes? Simply return the number of complete layers.

Example:

```python
4  -->  1
 5  -->  2
13  -->  2
14  -->  3
```

### Code

```python
def pyramid_height(n):
    m = 0
    counter = 0
    deduction = n - m**2
    while deduction > 0:
        m += 1
        deduction = deduction - m**2
        counter += 1
    if deduction < 0:
        return counter - 1
    return counter
```

## RGB To Hex Conversion

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

```python
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
```

### Code

```python
def rgb(r, g, b):
    def rgb_out_of_range_values(a):
        if a < 0:
            a = 0
            return a
        elif a > 255:
            a = 255
            return a
        else:
            return(int(a/16))
    def rgb_out_of_range_values2(c):
        if c < 0:
            c = 0
            return c
        elif c > 255:
            c = 255
            return c
        else:
            return(int(c%16))
    Hex1 = rgb_out_of_range_values(r)
    Hex3 = rgb_out_of_range_values(g)
    Hex5 = rgb_out_of_range_values(b)
    Hex2 = rgb_out_of_range_values2(r)
    Hex4 = rgb_out_of_range_values2(g)
    Hex6 = rgb_out_of_range_values2(b)
    RGB = [Hex1,Hex2,Hex3,Hex4,Hex5,Hex6]
    Hex = []
    Hexdecimal_alphabets = "ABCDEF"
    def Hex_helper(y):
        if y >= 0 and y <10:
            return str(y)
        elif y >= 10 and y <= 16:
            y = y - 10
            x = Hexdecimal_alphabets[y]
            return x
        elif y < 0:
            x = min(Hexdecimal_alphabets)
            return x
        else:
            x = max(Hexdecimal_alphabets)
            return x
    for s in range(6):
        Hex.append(Hex_helper(RGB[s]))
    return("".join(Hex))
```

## URL Extraction

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

```
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
```

### Code

```python
def domain_name(url):
    #tried way too many times for this, can the author of this kata specify more on the test cases in the instructions section, the required 'domain' is not even a domain to begin with.
    #this is just a practice of trial and error tbh, it doesn't take subdomains into account, and i'm surprised the amount of test cases that are not included in instructions.
    print(url)
    domain = ""
    numbers = '1234567890'
    def domain_helper(loop):
        new_domain = ""
        for s in range(len(domain)):
            if domain[s] == '.':
                return new_domain
            else:
                new_domain = new_domain + domain[s]
                s += 1
    if url[4] == 's' and url[0] == 'h' and url[11] != '.':
        domain = url.split("https://")
        domain = domain[1]
        return domain_helper(domain)
    elif url[0] == 'w' and url[1] == 'w' and url[2] == 'w':
        domain = url.split("www.")
        domain = domain[1]
        return domain_helper(domain)
    elif url[4] == ':' and url[0] == 'h' and url[10] != '.':
        domain = url.split("http://")
        domain = domain[1]
        return domain_helper(domain)
    elif url[0] == 'h' and url[7] not in numbers and url[10] == '.':
        domain = url.split("http://www.")
        domain = domain[1]
        return domain_helper(domain)
    elif url[0] == 'h' and url[8] not in numbers and url[11] == '.':
        domain = url.split("https://www.")
        domain = domain[1]
        return domain_helper(domain)
    else:
        if len(url) <= 9:
            domain = url
            return domain_helper(domain)
        elif url[9] in numbers and len(url) <= 15:
            domain = url.split("https://")
            domain = domain[1]
            return domain_helper(domain)
        else:
            domain = url
            return domain_helper(domain)
```

## Coefficients of the Quadratic Equation

In this Kata you are expected to find the coefficients of quadratic equation of the given two roots (x1 and x2).

Equation will be the form of $ax^2 + bx + c = 0$

Return type is a Vector (tuple in Rust, Array in Ruby) containing coefficients of the equations in the order (a, b, c).

Since there are infinitely many solutions to this problem, we fix a = 1.

Remember, the roots can be written like $(x-x_1)(x-x_2) = 0$

- example:

```
quadratic(1,2) = (1, -3, 2)
```

This means $(x-1)(x-2) = 0$; when we do the multiplication this becomes $x^2 - 3x + 2 = 0$

Notes:

- Inputs will be integers
- When `x1 == x2`, this means the root has the multiplicity of two

### Code

```python
def quadratic(x1, x2):
    return(1, -(x1 + x2), (x1 * x2))
```

## Factorial

In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 

$5! = 5 * 4 * 3 * 2 * 1 = 120$ 

By convention, $0! = 1$

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type `ArgumentOutOfRangeException` (C#) or `IllegalArgumentException` (Java) or `RangeException` (PHP) or throw a `RangeError` (JavaScript) or `ValueError` (Python) or `return -1` (C).

### Code

```python
def factorial(n):
    def fact_helper(k):
        if k == 1:
            return k
        else:
            return k * factorial(k-1)
    if n > 0 and n <= 12:
        return fact_helper(n)
    elif n == 0:
        return 1
    else:
        raise ValueError
```