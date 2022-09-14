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