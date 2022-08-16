# The C Programming Language

### Author's Note: The notes on this page will not only include current lecture's, but also other resources to give a more comprehensive study on C. Some examples will be compared with similar code but written in Python as well.

## Program Structure

A C program consists of the following parts:
- Preprocessor Commands
- Functions
- Variables
- Statements & Expressions
- Comments

### Example

We will be using a `Hello World` example to explain the program structure written in C:

```
#include <stdio.h>

int main() {
   /* my first program in C */
   printf("Hello, World! \n");
   
   return 0;
}
```

### Preprocessor Command

`#include <stdio.h>` is a preprocessor command, it tells the C compiler to include stdio.h file before going to the actual compilation.

### Function

Similar to python `def` functions, C uses the `int main` function where the program execution begins.

### Comments

`/*` and `*/` are used as additional comments to explain what the program does, similar to python's docstring. Whatever is in the comment lines will be ignored by the compiler.

### Statements & Expressions

`printf` is a method to print `Hello World!` in the terminal. **The** `/n` **at the end of the string tells the compiler to get a new line after printing.**

Compared to python, semicolon `;` must be at **the end of every operation to indicate that this is the end of statement.**

### Return Values

`return 0` terminates the `main()` function and returns the value 0. This is useful to indicate that the program has executed successfully, it is good practice to include this at the end of the function.

## Basic Syntax

### `printf`

Printing a string in C will look like this:

```
printf("hello world");
```

The `f` in `printf` refers to a formatted string. 

### Identifiers

C identifier is a name to identify a variable, function, or any other user-defined item. Note that C identifier:
- doesn't allow punctuation characters (@,$,etc)
- is **case-sensitive**
- can include underscores

This is why it's good programming practice to name human-readable variables and functions to briefly specify the purpose of the indentifiers.

A readable variable looks like this:

```
Calculator_helper
```

Do not take shortcuts like this:

```
calc_help
```

### Keywords

Keywords are reserved words in C, these special words must not be used as constants or variables or any other identifier names. Refer to [here](https://www.ibm.com/docs/en/developer-for-zos/14.2.0?topic=programs-c-reserved-keywords)

## Variables




