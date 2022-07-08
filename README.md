# Understanding Program Efficiency Part 1

### Author's Note: This section will include a large amount of paragraphs of words, expect a tedious reading. You have been warned.

## Understanding Efficiency on Programs

- efficiency matters:
    - data sets being incredibly massive
    - exp:

    ```
    In 2014, Google served 30,000,000,000,000 pages, covering 100,000,000 GB 
    – how long to search brute force?
    ```

- separate **time and space efficiency** of a program
    - tradeoff between them:
        - can sometimes pre-compute results are stored; then use "lookup" to retrieve (exp: dictionaries on Fibonacci)

### **This part we will be focusing on time efficiency**

Challenges in understanding efficiency of a solution to a computational problem:
- a program can be implemented in many different ways
- problem can be solved using only some algorithms 
- separating choices of implementation from choices of more abstract algorithm

## Evaluating Efficiency on Programs

- **measure** with a timer
- **count** operations
- abstract notion of **order of growth** **(recommended)**

## Timing a Program

- time module `import time`
- recall module and bring it to class:

```
def c_to_f(c):
    return c*9/5 + 32
```

- start clock

```
t0 = time.clock()
```

- call function

```
c_to_f(100000)
```

- stop clock

```
t1 = time.clock() - t0
Print("t =", t, ":", t1, "s,”)
```

## Timing Programs is Incosistent

Although counting time and evaluate efficiency between different algorithms is good, there are a few setbacks, it would be **not reliable and accurate** for:

- different implementations
- differnet computers
- large scale programs:
    - not predictable based on small inputs

Timing varies on a lot of factors, so this can't really express a relationship between inputs and time.

## Counting Operations

Assuming these steps take constant time:

- mathematical operations
- comparisons
- assignments
- accessing objects in memory

Example code:

```
def c_to_f(c):
    return c*9.0/5 + 32 #3 ops
def mysum(x):
    total = 0 #1 op
    for i in range(x+1): #loop x times
        total =+ 1 #1 op
    return total #2 ops
```

`mysum` will have 1+3x+2 operations in total. This will count the number of operations executed as function of size of input.

## Counting Operations is Still Incosistent

Counting operations still depends on algorithms, and it's independent on any computer that runs, meaning that since these sets of operations are pre-defined, it doesn't matter which computer runs it, the counts will still be the same. However:

- implementations varies
- no clear definition of which operations to count

Counting operations can still be reliable to some extent, a relationship between inputs and counts can be established.

### We still need a better way to also **evaluate implementations, scalability and input size.**

## Different Inputs Change How The Program Runs

here is a function that searches an element from a list:

```
def search_for_elmt(L,e):
    for i in L;
        if i == e
            return True
    return False
```

Different kinds of inputs affect efficiency greatly. For this instance, if `e` is the first element on the list, the program only needs to run once to return `True`, this is the **best case scenario**.

If `e` is not on the list, the program needs to loop multiple times until it doesn't find the element and returns `False`, this is the **worst case scenario**.

When `e` is in the middle of the list, the program has to look halfway through the elements to find `e`. This is the **average case scenario**.

**The point of this function is to measure the behaviour of how a program runs in a certain way.**

## Best, Average, Worst Cases

Suppose a list `L` with a length `len(L)`, we divide cases over **all possible inputs of** `len(L)`:

- **best case: minimum running time:**
    - constant for `search_for_elmt`
    - first element in any list
- **average case: average running time:**
    - practical measure
- **worst case: maximum running time:**
    - linear in length of list of `search_for_elmt`
    - **must search entire list and not find it**

## Orders of Growth

We want to achieve these:
- evaluate program efficiency with **very large inputs**
- express **growth of program's run time**
- putting **upper bound** of growth
- emphasizing **order** and **not exact**
- tighting upper bound on growth as function of size of input in worst case

## Measuring Order of Growth: Big "Oh" Notation: $O()$

- used to describe worst case:
    - worst case occurs often and is the bottleneck when a program runs
    - express rate of growth of program relative to input size
    - **evaluate algorithm only**

## Exact Steps vs $O()$

Code to calculate a factorial:

```
def fact_iter(n):
    ""assumes n an int >= 0"""
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
 ```

The number of steps for the code to run will be 1+6n+1. However, as this was previously said, this method is incosistent. It would be better to evaluate the [asymptotic complexity](https://www.tutorialspoint.com/asymptotic-complexity) of a program, in this case it's $O(n)$. 

### Asymptotic Complexity with The Big O Notation

The Big O Notation is about **ignoring multiplicative and additive constants. It's focused on considering the largest term that grows the most rapidly.** It is the expression to compute asymptotic behaviour of an algorithm as input size grows.

Focus on **dominant terms:**

$O(n^2) : n^2 + 2n + 2$

- Since $n^2$ is the largest term here, the asymptotic behavior of this is $O(n^2)$.

$O(n^2) : n^2 + 100000n + 3^{1000}$

- Even when $100000n$ is considered very large in the beginning, when n input grows to an incredibly large amount, $n^2$ will still be the dominant term.

$O(n) : \log n + n + 4$

- n grows much faster than $\log n$, so the order of growth here will be $O(n)$.

$O(n\log n) : 0.0001*n*\log n + 300n$

- Even when $n\log n$ is multiplied by a very small decimal, when input size grows it will still be the largest term that grows the most rapidly.

$O(3^n) : 2n^{30} + 3^n$

- Exponentials grows faster than powers. So order of growth is $O(3^n)$.


![Types of order of growth](https://scontent.fkul3-2.fna.fbcdn.net/v/t1.15752-9/292257433_1180369952536190_2868922925712914083_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_ohc=vojOX5r1SmgAX-6xHrJ&_nc_ht=scontent.fkul3-2.fna&oh=03_AVKGkvM_clzpau0-iZcbJu1Q-3jf4gqxoUF-TFRrmGx_AA&oe=62EBF37E)


