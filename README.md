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

This is why it's good programming practice to name human-readable variables and functions to briefly specify the purpose of the identifiers.

A readable variable looks like this:

```
Calculator_helper
Calc_help
```

Do not take shortcuts like this:

```
c_help
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
- `signed` values (`signed char`) start from -128

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

## About Data Size (Practices)

### Manipulating Out of Range Data Sizes

```C
#include <stdio.h>

int main(){
   char c = 125;
   c = c+10; //notice for data type signed char the range is 0-127
   printf("%d", c);
} 
```

Since by default, declared `char` variables are `signed char`. The range for `signed char` is -128 to 127, `c` for `135` here is out of this range:

- `125`'s binary counterpart is `01111101`
- `10`'s binary counterpart is `1010`
- adding `125` and `10` together we get `10000111`
- get the most significant bit of `10000111` which is `1`, **this represents a negative number**
- finding 2's complement of `10000111`: `01111000` + `1` = `01111001`: `121` in decimal system
- considering the most significant bit, `-121` is returned

### `sizeof()` and Signed Values

`sizeof()` is a function that computes the size of the operand:

```C
printf("%d\n",sizeof(char)); //prints 1
printf("%d\n",sizeof(int)); //prints 4

int a = 20;
char b = 'b';
printf("%d\n%d\n",sizeof(a),sizeof(b)); //prints 4 and 1
```

Comparing `sizeof()` values with unsigned values and prioritizing the order of evaluations:

```C
#include <stdio.h>

int main(){
   if (sizeof(int) > -1)
      printf("Yes");
   else
      printf("No"); //desired output
   return 0;
} 
```

- `sizeof(int)` is 4 which is an `unsigned int`
- `-1` here is an `signed int`

From the order of evaluations in C, **when integer values are compared with unsigned values, the int is promoted to unsigned.** In this case, when `-1` is promoting to `unsigned`, **negative numbers are stored in 2's complement form,** so the unsigned value of `-1` is significantly higher than `sizeof(int)`, which in result prints `No`.

### Dividing between Ints

```C
#include <stdio.h>

int main(){
   float c = 5.0;
   printf ("Temperature in Fahrenheit is %.2f", (9/5)*c + 32);
   return 0;
}
```

Since `9/5` is expressed as int divided by int, it will be expressed as `9//5`. A fix for this can be expressed as `9.0/5.0` or `1.0*9/5` (floating point precedence).

### Using *Inaccurate* Format Specifiers

Be careful when printing formatted strings, using `printf` with incorrect specifiers will return incorrect values:

```C
#include <stdio.h>
int main(){
   char a = '1';
   printf("%d", a); //prints 49
   return 0;
}
```

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

## C Preprocessor

Preprocessors are not included in the compiler, they're used solely for a text substitution tool to reduce repetitive code. It instructs the compiler pre-process before compilation.

![c preprocessors](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Preprocessor-In-C.png)

### Types of Preprocessors

| Preprocessor | Description |
| - | - |
| `#define` | substitutes macro
| `#include` | inserts header files
| `#undef` | undefines macro
| `#ifdef` | returns true if macro is **defined**
| `#ifndef` | return true if macro is **not defined**
| `#if` | tests if compile time condition is true
| `#else` | alternative for `#if`
| `#elif` | `#if` and `#else` in one statement
| `#endif` | ends conditional macro
| `#error` | prints error message on stderr
| `#pragma` | standardized method to issue special commands to compiler

### Macros for `#define`, `#undef` and `#include`

`#define` **can replace certain variables that are used often:**

```C
#include <stdio.h>

// macro definition
#define LIMIT 5
int main()
{
	for (int i = 0; i < LIMIT; i++) {
		printf("%d \n",i);
	}

	return 0;
}
```

Output:

```
0
1
2
3
4
```

You could use `#undef` to undefine the macro.

**Macro for simple function:**

```C
#include <stdio.h>

// macro with parameter
#define AREA(l, b) (l * b)
int main()
{
	int l1 = 10, l2 = 5, area;

	area = AREA(l1, l2);

	printf("Area of rectangle is: %d", area);

	return 0;
}
```

Similar to functions, the macro find for `AREA(l, b)` and passes `l` and `b` values to the macro and replace with `(l * b)`.

**Include either header files or files from system libraries:**

- program to calculate factorial:

```C
#include <stdio.h>

int fact(int a){
    double mult = 1;
    for (int i = 1; i <= a; i++){
        mult *= i;
    }
    return mult;
}

int fact_without_value(){
    int a;
    scanf("%d",&a);
    double mult = 1;
    for (int i = 1; i <= a; i++){
        mult *= i;
    }
    return mult;
}
    
```

- program to calculate basic arithmetic operations:

```C
#include <stdio.h>

int addition(int a, int b){
    return a+b;
}

int subtraction(int a, int b){
    return a-b;
}

int multiplication(int a, int b){
    return a*b;
}

float division(int a, int b){
    if (b == 0){
        return 0;
    }
    float c = a/(b*1.0);
    return c;
}

int remainders(int a, int b){
    if (b == 0){
        return 0;
    }
    int c = a % b;
    return c;
}

int arithmetics(int a){
    for (int i = 0; i <= a; i++){
        printf("sum: %d subtract: %d multiplication: %d division: %f remainder: %d\n",addition(a,i), subtraction(a,i), multiplication(a,i), division(a,i), remainders(a,i));
    }
}
```

- using `#include` to include the previous two files from system:

```C
#include <stdio.h>
#include "factorial.c"
#include "arithmetic.c"

int main(){
    int n1;
    scanf("%d",&n1);
    printf("arithmetics of %d\n", arithmetics(n1));
    arithmetics(n1);
    printf("Factorial of %d is %d\n", n1, fact(n1));
    return 0;
}
```

Output:

```
5
sum: 5 subtract: 5 multiplication: 0 division: 0.000000 remainder: 0
sum: 6 subtract: 4 multiplication: 5 division: 5.000000 remainder: 0
sum: 7 subtract: 3 multiplication: 10 division: 2.500000 remainder: 1
sum: 8 subtract: 2 multiplication: 15 division: 1.666667 remainder: 2
sum: 9 subtract: 1 multiplication: 20 division: 1.250000 remainder: 1
sum: 10 subtract: 0 multiplication: 25 division: 1.000000 remainder: 0
arithmetics of 6
sum: 5 subtract: 5 multiplication: 0 division: 0.000000 remainder: 0
sum: 6 subtract: 4 multiplication: 5 division: 5.000000 remainder: 0
sum: 7 subtract: 3 multiplication: 10 division: 2.500000 remainder: 1
sum: 8 subtract: 2 multiplication: 15 division: 1.666667 remainder: 2
sum: 9 subtract: 1 multiplication: 20 division: 1.250000 remainder: 1
sum: 10 subtract: 0 multiplication: 25 division: 1.000000 remainder: 0
Factorial of 5 is 120
```

### Conditional Directives

Conditional directives are a type of macros that helps to compile specific portions of the program based on some conditions:

```c
#ifdef macro_name
    statement1;
    statement2;
    statement3;
    .
    .
    .
    statementN;
#endif
```

**Using** `#if` and `#endif`:

```C
#include <stdio.h>
#if !defined (MESSAGE)
    #define MESSAGE "You wish!"
#endif

int main(){
    printf("Here is the message: %s\n", MESSAGE);
    return 0;
}
```

`!defined (MESSAGE)` here means that when `MESSAGE` is not defined, `#define MESSAGE "You wish!"` will be executed.

### Macro Continuation `\` and Stringize `#` Operator

```C
#include <stdio.h>

#define message_for(a, b) \
    printf(#a " and " #b ": We love you!\n")
    
int main(){
    message_for(Alpha, Delta);
    return 0;
}
```

Output:

```
Alpha and Delta: We love you!
```

`\` operator is used as an indicator that the macro is continued. This is done so to provide better readability for long macros.

`#` operator replaces `a` and `b` with the strings `Alpha` and `Delta` to the `printf` macro ***enclosed with double quotes.* Note that all other strings have to be enclosed with double quotes when using this type of macro.**

### Token Pasting `##`

`##` allows two separate tokens in the macro definition to be joined (concatenated) into a single token:

```C
#include <stdio.h>

#define tokenpaster(n) printf("token" #n " = %d", token##n)

int main(){
    int token34 = 40;
    tokenpaster(34);
    return 0;
}
```

`##n` substitutes 34 to `token` as `token34` which is the same as the variable initialized in `main` function. **Since they're the same variables, the output can be printed out correctly:**

```
token34 = 40
```
