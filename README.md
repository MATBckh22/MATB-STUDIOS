# Codewars Practices

Welcome to [Codewars](https://www.codewars.com/) Archive Katas! This is a section specifically for MATB members to post their own exercises (katas) of code, here we will be using mainly practices from codewars, though other platforms or homework are welcomed!

## Duplicate Encoder

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Example:

```
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
