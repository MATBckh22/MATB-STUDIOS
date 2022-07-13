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

- Although $100000n$ is considered very large in the beginning, when n input grows to an incredibly large amount, $n^2$ will still be the dominant term.

$O(n) : \log n + n + 4$

- n grows much faster than $\log n$, so the order of growth here will be $O(n)$.

$O(n \log n) : 0.0001 * n * \log n + 300n$

- Even when $n\log n$ is multiplied by a very small decimal, when input size grows it will still be the largest term that grows the most rapidly.

$O(3^n) : 2n^{30} + 3^n$

- Exponentials grows faster than powers. So order of growth is $O(3^n)$.


![Types of order of growth](https://scontent.fkul3-2.fna.fbcdn.net/v/t1.15752-9/292257433_1180369952536190_2868922925712914083_n.png?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_ohc=vojOX5r1SmgAX-6xHrJ&_nc_ht=scontent.fkul3-2.fna&oh=03_AVKGkvM_clzpau0-iZcbJu1Q-3jf4gqxoUF-TFRrmGx_AA&oe=62EBF37E)

### As observed (time to input size):
- constant growth doesn't change
- linear growth increases as a straight line
- quadratic growth starts to grow more quicker 
- logarithmic is always better than linear as it slows down at the end
- $n \log n$ sits between linear and quadratic, it's commonly found in algorithms
- exponential growth booms

## Complexity classes

Here is a table of complexity classes from low to high:

| Class | example | 
| - | - |
| Constant | $O(k), k \in \mathbb{R}$ 
| Logarithmic | $O(\log n)$
| Linear | $O(n)$
| Log-linear | $O(n \log n)$
| Polynomial | $O(n^k)$
| Exponential | $O(k^n)$
| Factorial | $O(n!)$

## Analyzing Programs and Their Complexity

Laws of addition and multiplication can combine complex cases and multiple O notations:

### Laws of Addition: $O(f(n))+O(g(n)) = O(f(n)+g(n)) = O(\max{(f(n),g(n))})$

- used with **sequential** statements:

```
for i in range(n):
    print ("a")
for j in range(n*n):
    print ("b")
```

Again only considering the dominant term we get $O(n)+O(n * n) = O(n+n^2) = O(n^2)$.

### Laws of Multiplication: $O(f(n))+O(g(n)) = O(f(n) * g(n))$

- used with **nested** statements:

```
for i in range(n):
    for j in range(n):
        print('a')
```

Outer loop goes n times, and the inner loop goes every n times as well for every outer loop iterated: $O(n) * O(n) = O(n * n) = O(n^2)$


## Linear Complexity

### Linear Search on **Unsorted** List

This is an example function used to search things linearly:

```
def linear_search(L, e):
    found = False
    for i in range(len(L)): 
        if e == L[i]: #speeding up by returning True, but doesn't impact worst case
        found = True
    return found
```

The overall complexity of this program is $O(n)$ where n is `len(L)`. Worst case: it must look through all elements to decide it's not there.

- $O(len(L))$ for the loop $O(1)$ to test if `e == L[i]`
    - $O(1+4n+1) = O(4n+2) = O(n)$

### Linear Search on **Sorted** List

```
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```  

Given that the list is sorted, we can program it so that when the search finds the desired element, it will return `True`, for elements beyond will return `False`.

Overall complexity is still $O(n)$ where `len(L)` will be the total length of the search. Though run time may differ for this method.

## Constant Time List Access

List access `L[i]` is different from search methods. Here we will explain why accessing an index from a list takes constant time:

### About Constant Time: $O(k)$

Constant complexity refers to an algorithm that **takes the same amount of time no matter how many inputs are given.** 

### How is list/array access constant time?

A list is represented internally as an array. An array lookup is always $O(1)$, it does not depend on the size of the array. this is known by a memory location or a pointer. 

In case of array, the memory location is calculated by using base pointer, index of element and size of element. 

Let's say, an array of 10 integer variables, with indices 0 through 9, may be stored as 10 words at memory addresses 2000, 2004, 2008, … 2036, so that the element with index i has the address 2000 + 4 × i. **This involves one multiplication and one addition operation, which takes constant time to execute, since this operation is fixed, list access takes constant time to execute as well.**

Relative sources: 
- [Complexity Exercises](https://www.geeksforgeeks.org/understanding-time-complexity-simple-examples/?ref=lbp)
- [Stack Overflow](https://stackoverflow.com/questions/7297916/why-does-accessing-an-element-in-an-array-take-constant-time)

## Linear Complexity

### Example 1

`addDigits()` is a function to search a list in sequence to see if the element is present:

```
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val
```

### Example 2

`fact_iter()` is an example of a factorial code:

```
def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod
```

it loops n times but the number of operations inside the loop is constant:
- set `i`
- multiply
- set `prod`

Since the complexity inside the loop is $O(1+3n+1) = O(3n+2) = O(n)$, the overall complexity of the entire function is also $O(n)$, which is linear.

## Quadratic Complexity - Nested Loops

### Subset List

This example is to determine whether one list is a subset of another (every element of the first list appears in the second, assuming there are no duplicates): [Visualization](https://pythontutor.com/render.html#code=def%20isSubset%28L1,%20L2%29%3A%0A%20%20%20%20for%20e1%20in%20L1%3A%0A%20%20%20%20%20%20%20%20matched%20%3D%20False%0A%20%20%20%20%20%20%20%20for%20e2%20in%20L2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20e1%20%3D%3D%20e2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matched%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20if%20not%20matched%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20return%20True%0A%0A%0AisSubset%28%7B1,2,3,4,5,6%7D,%7B1,2,3,4,5,6,7%7D%29&cumulative=false&curInstr=77&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
```

We begin by setting a `False` flag, for every 1st for loop is being executed the 2nd for loop will be looped to search for the elements. This will go either two ways:
- if it finds that both elements are present in the lists, as `e1 == e2`, the loop will break and return True, adding the counter by 1 and restarting the process again
- if it goes through the entire list and doesn't find it, `False` is returned

### Subset Complexity

Outer loops is executed `len(L1)` times, note that each iteration will execute the inner loop up to `len(L2)` times in which a constant number of operations will be executed under that loop. **Hence, for every outer loop runs a `len(L2)` inner loop is ran:**

$O(len(L1) * len(L2))$

**Worst case scenario: no elements that are shared in both lists, :**

$O({len(L1)}^2), len(L1) = len(L2)$

### List Intersection

This example finds an intersection of two lists. It returns a list where it appears on both of the lists:
[Visualization](https://pythontutor.com/render.html#code=def%20intersect%28L1,%20L2%29%3A%0A%20%20%20%20tmp%20%3D%20%5B%5D%0A%20%20%20%20for%20e1%20in%20L1%3A%0A%20%20%20%20%20%20%20%20for%20e2%20in%20L2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20e1%20%3D%3D%20e2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20tmp.append%28e1%29%0A%20%20%20%20res%20%3D%20%5B%5D%0A%20%20%20%20for%20e%20in%20tmp%3A%0A%20%20%20%20%20%20%20%20if%20not%28e%20in%20res%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20res.append%28e%29%0A%20%20%20%20return%20res%0A%20%20%20%20%0Aintersect%28%5B1,2,3,4,5%5D,%5B1,2%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```
def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
```

We begin by creating an empty list variable `tmp`, using similar concepts from subset, when there is an element shared within `L1` and `L2`, that element will be added into `tmp`. 

We then create another empty list variable `res` to remove any possible duplicates in `tmp` and add it into the list.

`res` is returned containing elements that are in both lists.

### Intersection Complexity

First nested loop, similar to subsets, has a complexity of

$O(len(L1) * len(L2))$

Second loop is not nested, it depends on `tmp`, specifically the length of `L1`, so it's complexity is just

$O(len(L1))$

Assuming both lists are about the same length, applying basic rules of asymptotic complexity this algorithm has a growth of

$O({len(L1)}^2), len(L1) = len(L2)$

## $O()$ Nested Loops

Basic example to calculate $n^2$: 
```
def g(n):
    """ assume n >= 0 """
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x
```

- inefficient
- when dealing with nested loops, **look at ranges**
- nested loops, **each iterating n times**
- **nested loops typically have quadratic behaviour:** $O(n^2)$
