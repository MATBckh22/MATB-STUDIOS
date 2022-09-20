# The C Programming Language

### Author's Note: The notes on this page will not only include current lecture's, but also other resources to give a more comprehensive study on C. Some examples will be compared with similar code but written in Python as well.

## Setting Up a C/C++ Compiler 

Before going to the actual part of writing code, C is very different compared to Python, u cannot run programs as straight-forward as Python. Hence, take note on this section how to set up a compiler for C/C++.

Here author will be using vscode to compile. The C/C++ extension doesn't include a compiler or debugger tool. Thus, u will have to install these tools to ur computer ([GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) or [Clang](https://en.wikipedia.org/wiki/Clang) specifically).

There may already be a C/C++ compiler and debugger provided by ur academic instructor. Check with ur instructors for guidance on how to install and use those compilers instead.

Otherwise, refer to [this complete guide on how to install and use C/C++ compiler on vscode](https://code.visualstudio.com/docs/languages/cpp) instead.

## Compiling and Executing C Programs

To make sure u have installed the compiler, execute this command line in the terminal:

- GCC:

```
g++ --version
```

- Clang:

```
clang --version
```

Follow these steps to know how to compile, we will be using the `Hello World` example mentioned above:

- open a text editor like vscode and add the example code
- save the file as `hello.c`
- open the terminal and type `gcc hello.c` and enter to compile the code
- if there are no errors in the output, terminal will generate an `a.out` executable file
- type `a.out` to execute the program
- `Hello, World!` expected to be in output

[Reference](https://www.tutorialspoint.com/cprogramming/c_program_structure.htm)

There are more commands to control workflow and file directories, see [here](https://ftp.kh.edu.tw/Linux/Redhat/en_6.2/doc/gsg/ch-doslinux.htm#:~:text=Many%20Linux%20commands%20you%20type,fact%2C%20some%20commands%20are%20identical.)

## Commands 

Commands are used in terminal, powershell or command prompt to configure file directories and edit files in your computer:
| Commands | Usage |
| - | - |
| `dir` | Directory listing
| `ren` | Rename a file
| `copy` | Copying a file 
| `move` | Moving a file
| `cls` | Clear screen
| `del` | Delete file
| `find` | Search for a string in file
| `time` | Displays time
| `cd` | Change the current directory
| `md` | Create a new directory/folder 
| `echo` | Print 
| `rmdir` | Delete a directory

For more commands, see this [reference](https://www.geeksforgeeks.org/linux-vs-windows-commands/)

## Basic Syntax

### `printf`

Printing a string in C will look like this:

```C
printf("hello world");
```

The `f` in `printf` refers to a formatted string. 

### Identifiers

C identifier is a name to identify a variable, function, or any other user-defined item. Note that a C identifier:
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

## Data Types

Data types are indicators of what kind of data they represent when we program our code:

### Basic Data Types

| Type | Usage |
| - | - |
| `bool` | boolean values, `true` or `false` 
| `char` | single character
| `float` | real numbers
| `int` | integers
| `string` | string of characters

[More references](https://www.tutorialspoint.com/cprogramming/c_data_types.htm)

### Integer Types

| Type | Value Range |
| - | - |
| `char` | -128 to 127 or 0 to 255
| `unsigned char` | 0 to 255
| `signed char` | -128 to 127
| `int` | -32,768 to 32,767 or -2,147,483,648 to 2,147,483,647
| `unsigned int` | 0 to 65,535 or 0 to 4,294,967,295
| `short` | -32,768 to 32,767
| `unsigned short` | 0 to 65,535
| `long` | -9223372036854775808 to 9223372036854775807
| `unsigned long` | 0 to 18446744073709551615

- `unsigned` values start from 0
- `signed` values start from 

### Floating-Point Types

Different float values have different precisions, in which they have more decimal places:

| Type | Percision | Value Range |
| - | - | - |
| `float` | 6 decimal places | 1.2E-38 to 3.4E+38
| `double` | 15 decimal places | 2.3E-308 to 1.7E+308
| `long double` | 19 decimal places | 3.4E-4932 to 1.1E+4932

### Void Types

Similar to `None` in python, `void` is a special value that represents the absence of a value. This is used in 3 different situations:

- function returns as void
   - no value is returned will return `void`
- function arguments as void
   - function with no parameters, exp: `int rand(void);`
- pointers to void
   - represents the address of an object but not it's type
      - memory allocation function returns a pointer to void so it can be casted to any data type

## Program Structure

A C program consists of the following parts:
- Preprocessor Commands
- Functions
- Variables
- Statements & Expressions
- Comments

### Example

We will be using a `Hello World` example to explain the program structure written in C:

```C
#include <stdio.h>

int main() {
   /* my first program in C */
   printf("Hello, World! \n");
   
   return 0;
}
```

### Preprocessor Command

`#include <stdio.h>` is a preprocessor command, also called as a **header file**, it tells the C compiler to include stdio.h libraries before going to the actual compilation.

- `#define`
   - definition of a constant (can be strings or ints)
   - can take arguments and be treated like a function
   - **parentheses ensure order of operations**
   - **not suitable for recursion**

```C
#define msgs "test"

int main(){
   printf(msgs)
}
```

- `#if`, `#ifdef`, `#ifndef`, `#else`, `#elif` , `#endif`
   - control which lines are compiled 

- `#pragma`
   - preprocessor directive

- `#error`, `#warning`
   - trigger a custom compiler error warning
   - exception handling

- `#undef`
   - remove definition of a variable at compile time

### Function

Similar to python `def` functions, C uses the `int main` function where the program execution begins.

### Comments

`/*` and `*/` are used as additional comments to explain what the program does, similar to python's docstring. Whatever is in the comment lines will be ignored by the compiler.

### Statements & Expressions

`printf` is a method to print `Hello World!` in the terminal. **The** `/n` **at the end of the string tells the compiler to get a new line after printing.**

Compared to python, semicolon `;` must be at **the end of every operation to indicate that this is the end of statement.**

### Return Values

`return 0` terminates the `main()` function and returns the value 0. This is useful to indicate that the program has executed successfully, it is good practice to include this at the end of the function.

## Format Specifiers

As previously discussed, `printf` is a method to print formatted strings. Format specifiers define what kind of data to be printed on output. It is **mandatory** to include this with `printf` or `scanf` inputs.

| Specifier | Data Type |
| - | - |
| `%c` | `char`
| `%s` | `string`
| `%f` | `float`
| `%n` | prints nothing
| `%i` | decimal integer (assumes base 10)
| `%d` | decimal integer (auto-detects)
| `%p` | pointer
| `%u` | int unsigned decimal
| `%e` or `%E` | float values with scientific notation
| `%%` | % symbol
| `%hi` | short (signed)
| `%hu` | short (unsigned)
| `%Lf` | `long double`

[More specifiers](https://www.freecodecamp.org/news/format-specifiers-in-c/)

## Binding Variables

Unlike in python where data types are automatically detected when assigning values to variables like:

```python
counter = 5
service_payment = 12.39
service_type = 'a'
service_code = 'A25MiR'
service_name = 'John'
```

However, in C, u will need to tell the program which data type the variable ur going to assign the value.

## Variable Definition and Declaration

### Declaration and Initialization 

Variable declaring takes more steps than the conventional approach used in python. If u want to use variables u will have to define them first:

```C
int n;
float phi;
```

Ensure that the variables defined are linked correctly to their respective data types.

However, u may also initialize a variable declaration like:

```C
float phi = 1.6180339887; 
int a = 0;
```

For handling multiple declarations u can do:

```C
int a, b, c = 2, d = 5;
```

This is to say that `a` and `b` are declared as integer variables, while `c` and `d` are declared with **integer values assigned.** 

## Arithmetic Expressions

Binary arithmetics using the four basic principles of calculations are allowed in C:

```C
x+y //x += y
x-y //x -= y
x*y // x *= y
x/y // x %= y
```

U could do simple expressions and statements using this example:

```C
y = (x+3)/2;
```

### Example

Assume that $x = 2.0$ and $y = 3.0$, evaluate the statement:

$$m = \frac {x+2y} {2x+3 \frac{3x}{5y}}$$

```C
float m = (x+2*y)/(2*x+3*((3*x)/(5*y)))
```

## Function prototypes

Declarations are also called function prototypes, it is a must to declare functions first before using:

```C
int multiplication (int);
```

or 

```C
int multiplication (int n);
```

- `<stblib.h>` has many common functions for prototypes as well
    - [Library for functions in C](https://www.ibm.com/docs/en/i/7.3?topic=extensions-standard-c-library-functions-table-by-name)

## About `main`

### `int main()` or `int main(void)`

- simplest version
    - no inputs, outputs `0` when successful
    - non-zero to signal error

```
Function declaration
{
declare variables;
program statements;
}
```

 ### `int main(int argc, char **argv)`

- two-argument form of `main()`

##  Printing

### Printing with `puts()`

```C
int main(){
   puts("hello!");
   return 0;
}
```

The difference between `printf()` and `puts()` is that `puts()` output text to console and **ends the line. This is done without** `\n`**.**

### Printing String Variables

Alternatively, string variables can be assigned using `const char`. 

- `const`: qualifies variable as constant
- `char`: data type representing a single character

Together, `const char msg[]` will be a constant array of characters.

## Console I/O

`stdout` and `stdin` are streams for console input and output.

- `puts(string)`: prints string 
- `putchar(char)`: print character
- `char = getchar()`: return character input from `stdin`
- `string = gets(string)`: return string input from `stdin`


