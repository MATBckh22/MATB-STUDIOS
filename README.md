# C Notes 2

## Operators

## Logical Operators

| Operator | Meaning | Examples |
| - | - | - |
| `&&` | and | `('A' == 'a') && (3 == 3);` evaluates to 0
| `||` | or | `2 == 3 || 'A' == 'a';` evaluates to 1
| `!` | not | `!(3 == 3);` evaluates to 0

### Increment and Decrement Operators

| Normal Arithmetic Expressions | Shortcut |
| - | - |
| `x += 1` | `x++` 
| `x -= 1` | `x--` 
| `y = x; x += 1` | `y = x++`
| `y = x; x -= 1` | `y = x--`

**Note for 3rd and 4th expressions, `x` is evaluated before it is decremented. Switching the positions will also switch their order of evaluation.**

### Assignment Operators 

Common expressions that can be found while programming is of the type:

```
variable = variable (operator) expression
```

C provides compact assignment operators that can be used instead, this is also known as **syntatic sugar**:

```
x += 1 --> x = x + 1
x -= 1 --> x = x - 1
x *= 5 --> x = x * 5
x %= 10 --> x = x % 10
x /= 2 --> x = x / 2
```

### Conditional Expressions

If else blocks can be declared similarly to python:

```C
if (condition){
    expression;
}
else{
    expressions;
}
```

**Using tenary operators to provide syntatic sugar for this particular statement:**

```
variable=(condition)?(expressions if true):(expressions if false)
```

```C
if (x>=0){
    s = 1
}
else{
    x = -1
}

//simplified:

s=x>=0?1:-1
```

## Blocks and Compound Statements

## Simple Blocks

- simple statement ends with semicolon `;`:
    - `z = foo(x+y);`
- multiple statements using `foo`:

```C
temp = x+y;
z = foo(temp);
```

`foo()` provides ease of use to replace expressions with variables without reassigning.

- block can substitute for simple statement
    - compiled as a single unit
    - variables can be declared inside
    - semicolons not needed

```C
{
    int temp = x+y;
    z = foo(temp);
}
```

Block can be empty too: `{}`

### Nested Blocks 

```C
{
    int temp1 = x-y;
    z = foo(temp);
    {
        float temp2 = x*y;
        z += bar(temp2);
    }
}
```

`bar()` is used to create bar tables.

## Control Flow

Unlike C++, Java, Python etc that has `boolean` values (can include `<stdbool.h>`). **In C, condition is an expression or a series of expressions.**

- if expression is non-zero - **Condition is true**x
- expression must be numeric (or a pointer)

```C
const char str[] = "this is a series of characters";
if (str) /* string is not null */
    return 0;
```

## Conditional Statements

### C's Equivalent of `elif` 

`Else if` is C's equivalent to python's `elif` function, it adds alternative control paths so in order, the program will look into else if blocks before going to the else statement when the previous if condition is not met.

```C
if (a>0)
    x++;
else if (a==0)
    x--;
else
    x = 1
```

This can be written with nested if blocks too:

```C
if (a>0)
    x++;
    if (a==0)
        x--;
else
    x = 1;
```

### `switch` Statement

`switch` is used to iterate an alternative conditional statements. It can be used for `int` and `char` input. 

- consider cases for value of variable:

```C
char s;

printf("Type a character from a-d:\n")
scanf("%c", &s);

switch (s){
    case 'a':
        printf("U typed a");
        break;
    case 'b':
        printf("U typed b");
        break;
    case 'c':
        printf("U typed c");
        break;
    case 'd':
        printf("U typed d");
        break;
    default: /*otherwise or else*/
        printf("error");
        break
}
```

`switch` is a more tidy approach to store multiple test cases in a block. **It is a must to include** `break` **statement to conclude a case.**

### Multiply Case

- compare variable to each case in order
- inner code starts to execute when match found until `break;`
- execution "falls through" if `break;` not included (not recommended)

```C
switch (s){
    case 'a':
    case 'b':
    /* expression starts when either case 'a' or case 'b' is met */
        break;
}
```

`break` vs no `break`:

With `break` every case can be treated individually:

```C
switch (s){
    case 'a':
        printf("U typed a"); /* do print method when case 'a' is reached until break; */
        break;
    case 'b':
        printf("U typed b"); /* do print method when case 'b' is reached and case 'a' is not met, until break */
        break;
```

Without `break`, cases are joined similarly to `or` statements:

```C
switch (s){
    case 'a':
        printf("U typed a"); /* do print method when case 'a' is reached */
    case 'b':
        printf("U typed b"); /* do print method when either case 'a' or case 'b' is met */
        break;
}
```

## Loop Statements

### `while` Loops

Similar to python, `while` loop in C is written with almost the same syntax:

```C
while (/* condition */)
    /* expressions */
```

### `for` Loops

The loop with a counter, or called *counting* loops, 