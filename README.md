# Algorithms

## Evaluating Efficiency

We say that an efficient algorithm consumes acceptable amount of resources in terms of:

- **time**
- **space (memory)**

### This part we will be focusing on time efficiency

Challenges in understanding efficiency of a solution to a computational problem:
- a program can be implemented in many different ways
- problem can be solved using only some algorithms 
- separating choices of implementation from choices of more abstract algorithm

## Orders of Growth

We want to achieve these:
- evaluate program efficiency with **very large inputs**
- express **growth of program's run time**
- putting **upper bound** of growth
- emphasizing **order** and **not exact**
- tighting upper bound on growth as function of size of input in worst case

## Asymptotic Analysis

### Measuring Worst Case: Big "Oh" Notation: $O()$

The Big O Notation is about **ignoring multiplicative and additive constants. It's focused on considering the largest/dominant term that grows the most rapidly.** It is the expression to compute asymptotic behaviour of an algorithm as input size grows.

For worst case analysis, it determines the upper bound on the running time of the algorithm with maximum operations and inputs.

- used to describe worst case:
    - worst case occurs often and is the bottleneck when a program runs
    - express rate of growth of program relative to input size
    - **evaluate algorithm only**

Focus on **dominant terms:**

$O(n^2) : n^2 + 2n + 2$

- Since $n^2$ is the largest term here, the asymptotic behavior of this is $O(n^2)$.

$O(n^2) : n^2 + 100000n + 3^{1000}$

- Although $100000n$ is considered very large in the beginning, when n input grows to an incredibly large amount, $n^2$ will still be the dominant term.

$O(n) : \log n + n + 4$

- n grows much faster than $\log n$, so the order of growth here will be $O(n)$.

$O(n \log n) : 0.0001 \times n \times \log n + 300n$

- Even when $n\log n$ is multiplied by a very small decimal, when input size grows it will still be the largest term that grows the most rapidly.

$O(3^n) : 2n^{30} + 3^n$

- Exponentials grows faster than powers. So order of growth is $O(3^n)$.

### As observed (time to input size):
- constant growth doesn't change
- linear growth increases as a straight line
- quadratic growth starts to grow more quicker 
- logarithmic is always better than linear as it slows down at the end
- $n \log n$ sits between linear and quadratic, it's commonly found in algorithms
- exponential growth booms

### Complexity classes

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

### Analyzing Programs and Their Complexity

Laws of addition and multiplication can combine complex cases and multiple O notations:

### Laws of Addition: $O(f(n))+O(g(n)) = O(f(n)+g(n)) = O(\max{(f(n),g(n))})$

- used with **sequential** statements:

```python
for i in range(n):
    print ("a")
for j in range(n*n):
    print ("b")
```

Again only considering the dominant term we get $O(n)+O(n \times n) = O(n+n^2) = O(n^2)$.

### Laws of Multiplication: $O(f(n))+O(g(n)) = O(f(n) \times g(n))$

- used with **nested** statements:

```python
for i in range(n):
    for j in range(n):
        print('a')
```

Outer loop goes n times, and the inner loop goes every n times as well for every outer loop iterated: $O(n) \times O(n) = O(n \times n) = O(n^2)$

### Measuring Average Case: Theta Notation $\theta()$

### Measuring Best Case: Omega Notation $\Omega()$