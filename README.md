*Author's Note: concepts are in the first half of the notes, if u wanna skip these go to line:50.
前言：有写过程式的人可以选择忽略这一部分的笔记，这边是给完全没有刷过程式科普视频或写代码经验的萌新，跳到第50行。但如果要参考专业用词的也可以扫过一遍。*


# Basic Concepts of Computer:
```-Calculations: built in or defined by the programmer
-Types of knowledge: Declarative and imperative
```

## DECLARATIVE: 
statement of fact, the result

## IMPERATIVE: 
steps to getting the result 


## Fixed program: calculator

## stored program: machine stores and executes operations
```sequence of instructions stored inside computer
-artihmetic and logic
-simple tests
-moving data
```

special program (interpreter) executes each instruction in order

# Basic Machine Architecture notes:
```ALU: Arithmetic Logic Unit
Control unit will have a program counter stored
Memory contains data and sequence of instructions
Loading said sequence starting with the first instruction in the program counter (stored in control unit) sends it to the ALU
ALU comprehends and gets data from the memory, uses some operations and stores it back to the memory
When it's done, ALU sends it back to Control Unit, program counter increases by 1
When sequence of instructions is completed, it will show in output
```

*Note: whole process may not be linear, manual control might be involved to skip instructions or resetting it*

## basic primitive contructs:
```aspects of languages:
syntax: string(s) of expressions that is synthatically valid
static semantics: synthatically valid strings that have meaning
semantics: have only one meaning but may not be what the programmer intended
```
## PYTHON PROGRAMS:
```program: sequence of definitions and commands
definitions evaluated, commands executed in a shell
```
# Objects: (very important)
```-scalar
int: 宣告 integers
float: represent real numbers
bool: boolean (true or false)
NoneType: special value: none
```
*Note: type() can see the type of an object, exp*
>>>type(5) 
int

*TYPE convergions: convert one object to another,exp*
>>>int(3.9)
3
```
-non-scalar
internal structure that can be accessed

Printing to Console
show output: print command
```
## Operators: +-*/
```i%j: remainder (i/j的余数)
i**j: i^j
```
## Binding Variables and Values
```= equal sign: assign value to a variable name
exp:
pi = 3.14159
pi_approx 22/7
Values are stored in memory where assignment binds value to name, retrieve it by typing the variable name
```
*U can rebind values, in a more detailed explanation, previous value may be stored in memory but we lost the handle for it, u can't get it back
value of area doesn't change unless u do the calculation again (废话 敲过码的不需要看这一行 只是记录一下)*
