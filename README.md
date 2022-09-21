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
a
## Execution Flow

![execution flow](https://i.imgur.com/Vu9w7d8.png)

## Process of Computation

Memory contains data and sequence of instructions, Control Unit will have a program counter stored.

Loading said sequence starting with the first instruction in the program counter (stored in control unit) and sends it to the ALU.

ALU comprehends and gets data from the memory, executes some operations and stores the data back to the memory.

When it's done, ALU sends it back to Control Unit, program counter increases by 1. This process is repeated linearly, instruction by instruction in which between each instructions a test is carried out.

When sequence of instructions is completed, it will show in output.

*Note: whole process may not always be executed in one go, control flow might be involved to skip instructions or resetting it*

## Printing and Prompting an Input

### Python Prompt

```python
integer1 = int(input("type a number!\n"))
```

### C Equivalent

```C
int integer1;
printf("type a number!\n");
scanf(%d, &integer1);
```

In C, handling integer inputs takes more lines than python:

- `int integer1;` declares an `integer1` variable
- `printf("type a number!\n");` outputs the user prompt
- `scanf(%d, &integer1);` reads the next user input
   - note that u must use the correct format specifier to prompt user inputs

### Addition Program

This is an example of writing an addition program in C:

```C
#include <stdio.h>

int main()
{
    int integer1;
    int integer2;

    printf("Type a number!\n");
    scanf("%d", &integer1);

    printf("Type a number!\n");
    scanf("%d", &integer2);

    int sum;
    sum = integer1 + integer2;
    printf("The sum for integer1 and integer2 is %d\n", sum);
    return 0;
}
```

**Notice:**

- `scanf` reads the user input, it expects a type `int` which is it's respective format specifier `%d`, it reads the input and assigns it with `integer1` using `&` operator
- however, `printf` doesn't use the `&` operator to print `sum`

