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

```
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
    Hex = ""
    Hexdecimal_alphabets = "ABCDEFG"
    Hex1 = int(r/16)
    Hex3 = int(g/16)
    Hex5 = int(b/16)
    Hex2 = int(r%16)
    Hex4 = int(g%16)
    Hex6 = int(b%16)
    Hex_converted1 = ""
    Hex_converted2 = ""
    Hex_converted3 = ""
    Hex_converted4 = ""
    Hex_converted5 = ""
    Hex_converted6 = ""
    if Hex1 >= 10 and Hex1 <= 255:
        hexdecimal1 = Hex1 - 10
        Hex_converted1 = Hexdecimal_alphabets[hexdecimal1]
        Hex = Hex + Hex_converted1
    elif Hex1 < 0:
        Hex1 = 0
        Hex = Hex + str(Hex1)
    elif Hex1 > 255:
        Hex1 = 255
        Hex = Hex + str(Hex1)
    else:
        Hex = Hex + str(Hex1)
    if Hex2 >= 10 and Hex2 <= 255:
        hexdecimal2 = Hex2- 10
        Hex_converted2 = Hexdecimal_alphabets[hexdecimal2]
        Hex = Hex + Hex_converted2
    elif Hex2 < 0:
        Hex2 = 0
        Hex = Hex + str(Hex2)
    elif Hex2 > 255:
        Hex2 = 255
        Hex = Hex + str(Hex2)
    else:
        Hex = Hex + str(Hex2)
    if Hex3 >= 10 and Hex3 <= 255:
        hexdecimal3 = Hex3 - 10
        Hex_converted3 = Hexdecimal_alphabets[hexdecimal3]
        Hex = Hex + Hex_converted3
    elif Hex3 < 0:
        Hex3 = 0
        Hex = Hex + str(Hex3)
    elif Hex3 > 255:
        Hex3 = 255
        Hex = Hex + str(Hex3)
    else:
        Hex = Hex + str(Hex3)
    if Hex4 >= 10 and Hex4 <= 255:
        hexdecimal4 = Hex4 - 10
        Hex_converted4 = Hexdecimal_alphabets[hexdecimal4]
        Hex = Hex + Hex_converted4
    elif Hex4 < 0:
        Hex4 = 0
        Hex = Hex + str(Hex4)
    elif Hex4 > 255:
        Hex4 = 255
        Hex = Hex + str(Hex4)
    else:
        Hex = Hex + str(Hex4)
    if Hex5 >= 10 and Hex5 <= 255:
        hexdecimal5 = Hex5 - 10
        Hex_converted5 = Hexdecimal_alphabets[hexdecimal5]
        Hex = Hex + Hex_converted5
    elif Hex5 < 0:
        Hex5 = 0
        Hex = Hex + str(Hex5)
    elif Hex5 > 255:
        Hex5 = 255
        Hex = Hex + str(Hex5)
    else:
        Hex = Hex + str(Hex5)
    if Hex6 >= 10 and Hex6 <= 255:
        hexdecimal6 = Hex6 - 10
        Hex_converted6 = Hexdecimal_alphabets[hexdecimal6]
        Hex = Hex + Hex_converted6
    elif Hex6 < 0:
        Hex6 = 0
        Hex = Hex + str(Hex6)
    elif Hex6 > 255:
        Hex6 = 255
        Hex = Hex + str(Hex6)
    else:
        Hex = Hex + str(Hex6)
    return Hex

rgb(-20,275,0)
```