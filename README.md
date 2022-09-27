# Control Flow

## `goto` - Unconditional Code Jumping

`goto` enables the ability to jump to an arbitary part of ur code unconditionally within the same function.

- location is identified using a label
- label is the named location in the code
    - same form as a variable followed by `:`

```C
start:
{
    if (cond)
        goto outside;
    goto start
}
outside:
<expression>
```

## Spaghetti Code

Spaghetti code refers to phrases of code that are harder to maintain and debug. This type of code is extremely unstable in terms of performance and lacks essential programming rules.

**Note that excess use of** `goto` **creates spaghetti code, it also makes code harder to debug and read. Any code that can be written with** `goto` **can be written without one.**

### Error Handling

However, despite it's drastic consequences when used excessively, `goto` provides a convenient way to exit from nested blocks:

```C
for (...){
    for (...){
        if (error_cond)
            goto error;
    }
}
error:
```

## Input and Output (I/O)

### Preliminaries

`<stdio.h>` provides basic input and output libraries, not the language itself. 

- text stream consists of a series of lines ending with `\n`, `<stdlib.h>` takes care of conversion from `'\r\n'−'\n'` 
    - binary stream consists of a series of raw bytes
    - streams provided by standard library are buffered

### `int putchar()`

- puts the character `c` on the standard output
- automatically `\n` or line breaks to the next line
- returns character printed or EOF on error

### `int getchar()`

- returns the next character from standard input or returns EOF on error

## Digression: Character Arrays

### C doesn't have data type string, strings are represented as **character arrays. C doesn't restrict the length of the string, end of the string is specified using 0**
