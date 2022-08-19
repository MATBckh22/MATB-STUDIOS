# Understanding Program Efficiency, Part 2

## Logarithmic Complexity 

Logarithmic complexity refers to growth that grows as log of size of one of it's inputs. 

- bisection search
- binary search

## Bisection Search

A better way to search for particular elements on a list rather than the traditional "walk down" sequential search method:

- pick an index `i` that divides list in half
- ask if `L[i] == e`
- if not, ask if `L[i]` is larger or smaller than `e`
- depending on answer, search to left or right

![bisection search](https://scontent.xx.fbcdn.net/v/t1.15752-9/289555839_354821093470981_1026255080454262356_n.png?stp=dst-png_p403x403&_nc_cat=107&ccb=1-7&_nc_sid=aee45a&_nc_ohc=AohI_pN39lcAX_J3bze&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVIuOSlbDd7OTrn2OJieWj6_qhnN3fWqkLZYvUcQB3jkZw&oe=62F441D6)

### Recursion Complexity

We repeatedly slice the list by half and goes either left or right depending on the answer given, throwing away half of the elements. After `i` steps, we will be left with $\frac{n}{2^i}$ elements.

Worst case: element is not on the list, so the program slices until it is left with one element, and founds out that element is not the answer.

The complexity will be:

$O(\log n), n = len(L)$

## Bisection Search Implementation 1

Here is an example of bisection search to guess a number:

```python
def bisect_search1(L, e):
    if L == []:
        return False
```

We start by avoiding empty inputs, if the user input is empty, `False` is returned.

```python
    elif len(L) == 1:
        return L[0] == e
```

If the length of the list is 1, which is the only elements on the list, that number is returned.

```python
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1( L[:half], e)
        else:
            return bisect_search1( L[half:], e)
```

Otherwise, divide the list by half, the program will return either half of the list where the number is at.

Full code:

```python
def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1( L[:half], e)
        else:
            return bisect_search1( L[half:], e)
```

As we can see, operations under if and elif block take constant time, under else:

```python
if L[half] > e:
            return bisect_search1( L[:half], e)
        else:
            return bisect_search1( L[half:], e)
```

This is not constant, list slicing `list[:]` or list copying `list.copy()` is linear to the amount of elements. Thus, it goes over all the elements of the list and adds a copy of it: $O(n)$

The complexity of recursively copying the half of the list will be as stated earlier: $O(\log n)$

## Complexity of Bisection Search 1

- $O(\log n)$ bisection search calls
    - each recursive call, range of search is sliced half
    - if original size is n, in worst case to range of size 1:
$\frac{n}{2^k} = 1$ or when $k = \log n$

- $O(n)$ for each operation to copy list

- Using multiplication rules, the complexity of the algorithm is $O(\log n) * O(n) = O(n \log n)$
    - note: $O(n)$ still dominates the $\log n$ cost due to the amount of recursive calls used

## Bisection Search Alternative

Although this code is more lengthy, it's more efficient for the computer to run, we will split this into two parts:
- main block: `bisect_search2`
- sub block: `bisect_search_helper`

### `bisect_search2`

```python
def bisect_search2(L, e):
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
```

This block checks if the list is empty. if it is, `False` wil be returned. Otherwise, call `bisect_search_helper` with variables:
- `L`: list of searching range
- `e`: number to search
- `0`: zero, this is later returned with `low` as the lower bound
- `len(L) - 1`: length of list reduced by 1, this is also later returned with `high` as the upper bound

### `bisect_search_helper`

```python
def bisect_search_helper(L, e, low, high):
        print('low: ' + str(low) + '; high: ' + str(high))  #added to visualize
        if high == low:
            return L[low] == e
        mid = (low + high)//2
```

Under this block, we begin by setting a print operation to visualize the searching process. If both bounds are equal, the list would be the length of just 1, thus `return L[low] == e` is executed. 

We then take the mid-point of `low` and `high`.

```python
if L[mid] == e:
    return True
```

Adding this block will check if the mid-point is the number we're looking for.

```python
elif L[mid] > e:
    if low == mid: #nothing left to search
        return False
    else:
        return bisect_search_helper(L, e, low, mid - 1)
```

For `e` that is in the lower half $[low, mid]$, we have another conditional statement where:
- if the mid-point is the lower bound, there is nothing left to search, so `False` is returned
- otherwise, return the same variables but **replace** `mid - 1` **as the new upper bound**

From the latter, `bisect_search_helper` is called again and this process will repeat until either condition is met.

```python
else:
    return bisect_search_helper(L, e, mid + 1, high)
```

For `e` that is in the upper half $[mid,high]$, we also return the same variables but **replace** `mid + 1` **as the new lower bound**

Full code: [Visualization](https://pythontutor.com/render.html#code=def%20bisect_search2%28L,%20e%29%3A%0A%20%20%20%20def%20bisect_search_helper%28L,%20e,%20low,%20high%29%3A%0A%20%20%20%20%20%20%20%20print%28'low%3A%20'%20%2B%20str%28low%29%20%2B%20'%3B%20high%3A%20'%20%2B%20str%28high%29%29%20%20%23added%20to%20visualize%0A%20%20%20%20%20%20%20%20if%20high%20%3D%3D%20low%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20L%5Blow%5D%20%3D%3D%20e%0A%20%20%20%20%20%20%20%20mid%20%3D%20%28low%20%2B%20high%29//2%0A%20%20%20%20%20%20%20%20if%20L%5Bmid%5D%20%3D%3D%20e%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20elif%20L%5Bmid%5D%20%3E%20e%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20low%20%3D%3D%20mid%3A%20%23nothing%20left%20to%20search%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20bisect_search_helper%28L,%20e,%20low,%20mid%20-%201%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20bisect_search_helper%28L,%20e,%20mid%20%2B%201,%20high%29%0A%20%20%20%20if%20len%28L%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20bisect_search_helper%28L,%20e,%200,%20len%28L%29%20-%201%29%0A%0AtestList%20%3D%20%5B%5D%0Afor%20i%20in%20range%28100%29%3A%0A%20%20%20%20testList.append%28i%29%0A%20%20%20%20%0Aprint%28bisect_search2%28testList,%2076%29%29&cumulative=false&curInstr=265&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        print('low: ' + str(low) + '; high: ' + str(high))  #added to visualize
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
```

## Complexity of Bisection Search 2

### Similar to Bisection Implementation 1:

- $O(\log n)$ bisection search calls
    - each recursive call, range of search is sliced half
    - if original size is n, in worst case to range of size 1:
$\frac{n}{2^k} = 1$ or when $k = \log n$

### Difference:

- pass list and indices as parameters
- never copies list, just repasses it as pointers
- `return bisect_search_helper(L, e, low, mid - 1)` and `return bisect_search_helper(L, e, mid + 1, high)` are constant rather than recursive
- overall complexity: $O(\log n) * O(1) = O(\log n)$

## Logarithmic Complexity Example

This is an example of a code that has logarithmic complexity, it changes ints to strings: [Visualization](https://pythontutor.com/render.html#code=def%20intToStr%28i%29%3A%0A%20%20%20%20digits%20%3D%20'0123456789'%0A%20%20%20%20if%20i%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20'0'%0A%20%20%20%20result%20%3D%20''%0A%20%20%20%20while%20i%20%3E%200%3A%0A%20%20%20%20%20%20%20%20result%20%3D%20digits%5Bi%2510%5D%20%2B%20result%0A%20%20%20%20%20%20%20%20i%20%3D%20i//10%0A%20%20%20%20return%20result%0A%20%20%20%20%0Ai%20%3D%20int%28input%28%22Number%20here%22%29%29%0AintToStr%28i%29&cumulative=false&curInstr=1&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result
    
i = int(input("Number here"))
intToStr(i)
```

We first set an existing string of digits from 0-9:
- if int input is zero, it will return zero as a string
- otherwise, **divide the number by 10 and get the remainder repeatedly until there's no remainder left to divide**
    - *note: dividing by 10 is intended to get the digit we're looking for*

### Complexity

Only the while loop block will be considered here:
- constant number of operations per loop
- how many times `i` can be divided by 10?
    - $O(\log i)$

## $O()$ Factorial

### Iterative Factorial

Complexity can depend on number of iterative calls:

```python
def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod
```

The complexity for this is overall $O(n)$, constant cost each time for n loops.

### Recursive Factorial

Another alternative to compute factorials is to code it recursively:

```python
def fact_recur(n):
    """ assume n >= 0 """
    if n <= 1:
        return 1
    else:
        return n*fact_recur(n – 1)
```

Although due to the amount of function calls it runs a bit slower than the iterative version. However, growth is still the same - $O(n)$.

## Log-Linear Complexity
- many practical algorithms are log-linear
- commonly used is merge sort

## Polynomial Complexity
- quadratic
- nested loops / recursive function calls

## Exponential Complexity
- recursive functions
    - more than one recursive call for one problem
        - Tower of Hanoi
- many important problems are inherently exponential
    - high costs
    - consider approximate solutions to provide reasonable answers more quickly

### Complexity of Towers of Hanoi

Let $t_{n}$ denote time to solve tower of size n:

$t_{n} = 2t_{n-1}+1$

$= 2(2t_{n-2}+1)+1$

$= 4t_{n-2}+2+1$

$= 4(2t_{n-3}+1)+2+1$

$= 8t_{n-3}+4+2+1$

$= 2^kt_{n-k}+2^{k-1}+...+4+2+1$

$= 2^{n-1}+2^{n-2}+...+4+2+1$

Applying Geometric Growth:

$a = 2^{n-1}+...+2+1$

$2a = 2^n+2^{n-1}+...+2$

$a = 2^n-1$

$\because a = 2^n-1$

$\therefore 2^{n-1}+2^{n-2}+...+4+2+1 = 2^n-1$

Order of Growth = $O(2^n)$

## Exponential Complexity - Power Set

A power set is to generate the collection of **all possible subsets when given a set of no repeating integers.**

Exp:
{1, 2, 3, 4} would generate (*order doesn't matter*):

`{}, {1}, {2}, {3}, {4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}, {1, 2, 3},	{1,	2, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2,	3, 4}`

### Power Set - Recursive Concept

- generate set of integers 1 to n
- assume we can generate set integers of 1 to n-1
- all of the subsets belong to bigger power sets

$2^1$: `{}, {1}`

$2^2$: `{}, {1}, {2}, {1,2}`

$2^3$: `{}, {1}, {2}, {1,2}, {3}, {1,3}, {2,3}, {1,2,3}`

$...$

$2^n$

Notice how a $2^2$ power set is by adding elements into a $2^1$ subset and branch from there. Same as a  $2^3$ power set where it adds 3 in subset $2^2$ and branch from there.

### Power Set - Code

A code to create a power set looks like this:

```python
def genSubsets(L):
    res = [] #base case
    if len(L) == 0:
        return [[]] #list of empty list
```

We start of to create a new list variable `res`, and if the input of the list is blank, it returns an empty list.

```python
smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []
```

Continuing from that, we create three variables:
- `smaller`: all subsets without the last element, it calls the function recursively to add elements into the list
- `extra`: list with only the last element
- `new`: empty list to be added with `smaller`

```python
for small in smaller:
        new.append(small+extra) 
```

For all of the subsets that exclude the last element, it will be added in here, as `new` is added with all `smaller` subsets and `extra`.

```
return smaller+new
```

Returning the generated power list.

Full code: [Visualization](https://pythontutor.com/render.html#code=def%20genSubsets%28L%29%3A%0A%20%20%20%20res%20%3D%20%5B%5D%0A%20%20%20%20if%20len%28L%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20%5B%5B%5D%5D%20%23list%20of%20empty%20list%0A%20%20%20%20smaller%20%3D%20genSubsets%28L%5B%3A-1%5D%29%20%23%20all%20subsets%20without%20last%20element%0A%20%20%20%20print%28smaller%29%0A%20%20%20%20extra%20%3D%20L%5B-1%3A%5D%20%23%20create%20a%20list%20of%20just%20last%20element%0A%20%20%20%20new%20%3D%20%5B%5D%0A%20%20%20%20for%20small%20in%20smaller%3A%0A%20%20%20%20%20%20%20%20new.append%28small%2Bextra%29%20%20%23%20for%20all%20smaller%20solutions,%20add%20one%20with%20last%20element%0A%20%20%20%20return%20smaller%2Bnew%20%20%23%20combine%20those%20with%20last%20element%20and%20those%20without%0A%0A%0AtestSet%20%3D%20%5B1,2,3,4%5D%0Aprint%28genSubsets%28testSet%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
def genSubsets(L):
    res = [] #base case
    if len(L) == 0:
        return [[]] #list of empty list
    smaller = genSubsets(L[:-1]) # all subsets without last element
    print(smaller)
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra)  # for all smaller solutions, add one with last element
    return smaller+new  # combine those with last element and those without


testSet = [1,2,3,4]
print(genSubsets(testSet))
```

### Power Set - Recursive Complexity

Rather than iterating tedious loops to complete a power set, it's better to break it down to two parts and then connect it together:
- generate all possible subsets excluding last element
- adding last element into all subsets

These two parts contribute to the complexity of this program, but all of this depends on the heaviest dependent variable: `smaller`.

**Overall, for a set of size k, we will have $2^k$ cases.**

Let $t_{n}$ denote time to solve problem of size n, in this case it's `smaller = genSubsets(L[:-1])`.

Let $s_{n}$ denote size of solution to solve problem of size n, in this case it's `for small in smaller`.

Let $c$ be the constant number of the operations that take constant time.

$t_{n} = t_{n-1}+s_{n-1}+c$

$t_{n} = t_{n-1}+2^{n-1}+c$

$= t_{n-1}+2^{n-2}+c+2^{n-1}+c$

$= t_{n-k}+2^{n-k}+...+2^{n-1}+c$

$= t_{0}+2^{0}+...+2^{n-1}+nc$

$= 1+2^n+nc$

Therefore, complexity of a power set is $O(2^n)$

## Iterative vs Recursive Fibonacci

### Iterative Fibonacci

```python
def fib_iter(n):
    if n == 0:
        return 0
    elif: n == 1:
        return 1
    else:
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii 
```

There's only one for loop block we need to consider. Since the operations underneath are all constant, the order of growth will be:
- best case: $O(1)$
- worst case: $O(1)+O(n)+O(1) = O(n)$

### Recursive Fibonacci

```python
def fib_recur(n):
    """ assumes n an int >= 0 """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)
```

Although this code looks cleaner, it's way more inefficient for the computer to run. Given that it includes two recursive calls, the complexity of this is exponential: $O(2^n)$

That said, recursive programs, although looks cleaner and more efficient to write from a programmer stance, it's not always efficient for the computer to run. 

## Big Oh Summary

- compare **efficiency of algorithms**
    - notation that describes growth
    - **lower order of growth is always faster**
    - **independent of machine specific implementation**

- use Big Oh
    - describe **order of growth**
    - **asymptotic growth**
    - **upper bound**
    - **worst case** analysis
