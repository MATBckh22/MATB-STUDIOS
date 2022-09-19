# C - Lec 1

## Why C?

- widely used in OS, embedded, eeal-time systems and communication systems
- rich libraries
- efficiently work on entreprise and industrial applications

## Program Structure

A C program consists of the following parts:
- Preprocessor Directive
- Functions
- Variables
- Statements & Expressions
- Comments

### Example

We will be using a `Hello World` example to explain the program structure written in C:

```C
#include <stdio.h>

int main(void) {
   /* my first program in C */
   printf("Hello, World! \n");
   
   return 0;
}
```

`void` *is optional.*

### `<stdlib.h>`

`<stblib.h>` - standard library

### Comments

`/*` and `*/` are used as additional comments to explain what the program does, similar to python's docstring. Whatever is in the comment lines will be ignored by the compiler.

## Preprocessor Directive

`#` is a preprocessor directive, also called as a **header file**, it tells the C compiler to run what's inside the block.

## `;` - Statement

Semicolon `;` must be at **the end of every operation to indicate that this is the end of statement.**

### `\` - Escape Character

Compiler looks ahead at the next character and combines it with the backslash to form an escape sequence.

```C 
int main(){
printf("Hello Friend\n"); //\n is an escape sequence
printf("Hello Sara");
printf("Hello")
}
```
Here are some examples of escape sequences:

![escape sequence](https://cdn.educba.com/academy/wp-content/uploads/2020/01/Escape-Sequence-is-C.png)