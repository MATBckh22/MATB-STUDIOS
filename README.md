# Control Flow, Pointers, Memory Addressing, Arrays, Pointer Arithmetic, Strings and Sorting Algorithms

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

### C doesn't have data type string, strings are represented as **character arrays.** C doesn't restrict the length of the string, end of the string is specified using 0.

### Example

`'Hello'` can be represented using an array: `{'h','e','l','l','\0'}`

Hence, there are several declarations to declare a string:

```C
char str[] = "hello";
char str[10] = "hello"; /* 10 is the size of the array, when using this make sure the array size is enough for the input */
char str[] = {'h','e','l','l','o',0};
```

### Comparing Strings

`<string.h>` provides function `int strcmp(char s[], char t[])` to compare two strings in dictionary order:

- **lower cases come after capitals**
- returns `<0` if s comes before t
- returns 0 is same
- returns `>0` if s comes after t
- **case sensitive**

```C
strcmp("a", "A"); /* returns <0 */
strcmp("SUPERMAN", "BATMAN"); /* returns >0 */
strcmp("a", "a"); /* returns ==0 */
```

### Formatted Input 

- `scanf()`: formatted input function to take analog inputs of `printf`
    - takes variable number of inputs
    - separated by white space when multiple items are to be read
    - returns number of items read or EOF

**Note that** `scanf` **ignores white spaces. Arguments have to be pointers (address of variables).**

- `int sprintf(char str[], char format[], arg1, arg2);`
    - format specification same as `printf`
    - output is written to string (doesn't check size)
    - returns number of character written or negative value on error

- `int sscanf(char str[], char format[], arg1, arg2)`
    - format specification is the same as `scanf`
    - input is read from `str` variable
    - returns the number of items read or negative value on error

## File I/O

C allows us to read data from text/binary files using `fopen()`:

```C
FILE*fopen(char name[], char mode[])
```

- mode can be:
    - `"r"`: read only
    - `"w"`: write only
    - `"a"`: append
    - `"b"`: appended for binary files
- `fopen` returns a pointer to file stream if it exists or `null` otherwise
- `<stdin.h>` and `<stdout.h>` are also **FILE** datatypes
- `stderr` corresponds to standard error output (different from `stdout`)

- `int fclose(FILE*fp)`
    - closes stream
    - `fclose()` is automatically called on all open files when program terminates

### File Input

- `getc(FILE*fp)`
    - reads a single character from stream
    - returns character read or EOF

- `char[] fgets(char line[], int maxlen, FILE*fp)`
    - reads a single line up to maxlen characters from input stream
    - returns a pointer in character array that stores the line
    - return `null` if end of stream

### File Output

- `putc(int c, FILE*fp)`
    - writes a single character c to output
    - returns character returned or EOF

- `int fputs(char line[], FILE*fp)`
    - writes single line to output
    - returns 0 on success, otherwise EOF

- `int fscanf(FILE*fp, char format[], arg1, arg2)`
    - similar to `scanf`, `sscanf`
    - reads items from input

## Pointers and Addresses

Pointers are a memory address of a variable, address can be used to access or modify a variable from anywhere. This is extremely useful for data structures and [obfuscating](https://en.wikipedia.org/wiki/Obfuscation_(software)) code.

### Physical and Virtual Memory

- **Physical Memory: physical resources to store data**
    - cache
    - RAM
    - hard disk
    - removable storage

- **Virtual Memory: abstraction by OS, addressable space accessible by code**

### Physical Memory Considerations

