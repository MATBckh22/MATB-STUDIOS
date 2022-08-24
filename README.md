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
            c = 255d
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
