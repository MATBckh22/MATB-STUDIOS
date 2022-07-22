# What is Computation?

### Author's Note: concepts are in the first half of the notes, if u wanna skip these go to the lower half of the notes, or skip this chapter entirely. 前言：有写过程式的人可以选择忽略这一部分的笔记，这边是给完全没有写代码经验的萌新，但如果要参考专业用词的也可以扫过一遍。

## What Does a Computer Do?

- fundamentally
    - performs calculations
    - remembers results
- types of calculations
    - built-in to the language
    - defined as the programmer
- computers only know what u tell them

## Types of Knowledge

### Declarative 

Declarative knowledge is a statement of fact. 

Exp: Someone is going to win the lottery.

### Imperative 

Imperative knowledge is a *recipe* or ways to get the statement of fact. 

Exp:
- people sign up for the raffle
- host opens program
- program chooses a number between $1^{st}$ to $n^{th}$ entry
- number found, winner announced!

## What is A Recipe? 

### Algorithms

- sequence of simple steps
- flow of control process that specifies when each step is executed
- deciding when to stop


## Computer are Machines

### Fixed Program

Calculators: Only know how to do basic calculations (addition, multiplication, etc)

### Stored Program

- machine stores and executes instructions
    - sequence of instructions stored inside computer
        - artihmetic and logic
        - simple tests
        - moving data

- special program (interpreter) executes each instruction in order

# Basic Machine Architecture

A basic machine contains four main parts:
- memory
- input 
- output
- ALU: Arithmetic Logic Unit
    - does primitive operations

### Process of Computation

![Basic Machine Architecture](https://scontent.xx.fbcdn.net/v/t1.15752-9/288996051_596253385341886_9132386334258844518_n.png?_nc_cat=103&ccb=1-7&_nc_sid=aee45a&_nc_ohc=dvFdRx1MScQAX9378fi&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVKzm8onLuXSYyU2Tgbw0jfBxnHZdUzVqtQ5s33R8OB3tQ&oe=62FEA6D7)

Memory contains data and sequence of instructions, Control Unit will have a program counter stored. 

Loading said sequence starting with the first instruction in the program counter (stored in control unit) and sends it to the ALU.

ALU comprehends and gets data from the memory, executes some operations and stores the data back to the memory.

When it's done, ALU sends it back to Control Unit, program counter increases by 1. This process is repeated linearly, instruction by instruction in which between each instructions a test is carried out. 

When sequence of instructions is completed, it will show in output.

*Note: whole process may not always be executed in one go, control flow might be involved to skip instructions or resetting it*

## Basic Primitives

- turning showed that u can **compute anything using 6 primitives**

- modern programming languages have more convenient set of primitives

- can **abstract methods to create new primitives**

### Anything computable in one language is computable in any other programming language.

## Creating Recipes

- a programming language provides a set or primitive operations
- expressions are **complex but legal combinations of primitives**
- expressions and computations have **values and meanings**

## Aspects of Languages

### Primitive Constructs

- english: words
- programming language: numbers, strings, simple operators, etc

### `syntax` 

String of expressions has to be synthatically valid for it to give meaning:
- english
    - `"cat dog boy"`: not syntactically valid
    - `"cat hugs boy"`: syntactically valid
- programming language
    - `"hi"*5`: not syntactically valid
    - `3.2*5`: syntactically valid

### Static Semantics

Static Semantics is used to describe synthatically valid strings that have meaning:
- english
    - `"I are hungry"`: syntactically valid but static semantic error
- programming language
    - `"hi"+3`: syntactically valid but static semantic error

Semantics is the meaning associated with a syntactically correct string of symbols with no static semantic errors:
- english
    - can have many meanings: "Flying cars can be dangerous"
- programming languages
    - have only one meaning but may not be what the programmer intended
## Where Things Go Wrong

- **syntactic errors**
    - common and easily caught
- **static semantic errors**
    - some languages check for these before running program
    - can cause unpredictable behavior
- no semantic errors but **different meaning than what programmer intended**
    - program crashes, stops running
    - program runs forever
    - program gives an answer but different than expected

## Python Programs

A program is a sequence of **definitions and commands**, where definitions are evaluated, commands are executed by python interpreter in a shell.

Commands instruct interpreter to do something, this can be typed **directly in a shell/terminal or stored in a file** that is read into shell and evaluated.

## Objects

- programs manipulate **data objects**
- objects have a **type** that defines the kinds of things 
programs can do to them
    - Peter is a human, he can walk, speak english, eat, etc
    - Birds fly, speak bird language, etc
- objects are
    - scalar (cannot be subdivided)
    - non-scalar (have internal structure that can be accessed)

### Scalar Objects

- `int`: integers
- `float`: represent real numbers
- `bool`: boolean (`true` or `false`)
- `NoneType`: **special** value: `None`
- `type()` can see the type of an object:

```
>>>type(5) 
int
```

- type convergions: convert one object to another:

```
>>>int(3.9)
3
```

## Printing to Console

`print()` is a print command to show output:

```
print(3+2)
print("3+2")
```

## Operators: `+-*/`

- `i+j`: $i+j$
- `i-j`: $i-j$
- `i*j`: $i * j$
- `i/j`: $\frac{i}{j}$
- `i%j`: remainder of $\frac{i}{j}$
- `i**j`: $i^j$

## Binding Variables and Values

`=` is used to assign value to a variable name:

```
pi = 3.14159
pi_approx = 22/7

```

Values are stored in memory where assignment binds value to name, retrieve it by typing the variable name.

U can rebind values, in a more detailed explanation, previous value may be stored in memory but we lost the handle for it, u can't get it back, value of area doesn't change unless u do the calculation again.
