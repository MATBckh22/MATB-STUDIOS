# Searching and Sorting

## Searching Algorithms

Search algorithm is a method for finding an item or a group of items with specific properties within a collection of items.

Collection could be:

### implicit
- exp: finding the square root 
    - exhaustive enumeration
    - bisection search
    - Newton-Raphson

### explicit
- exp: student record in stored collection of data

## Types of Search

### Linear Search

- brute force search (British Museum algorithm)
- **list can be unsorted**

### Bisection Search

- two different implementations of algorithm
- **list must be sorted**

## Linear vs Bisection Search - Recap

### Unsorted Linear

```
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
```

This search method has to look through all of the elements to decide it's not there, for $O(len(L))$ the loop has to test if `e == L[i]`. Overall complexity will be $O(n)$ where n is `len(L)`.

### Sorted Linear

```
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```

This search method only looks until a number greater than e, for $O(len(L))$ the loop has to test if `e == L[i]`. Overall complexity will still be $O(n)$ where n is `len(L)`.

### Bisection Search

- pick an index `i` that divides list in half
- ask if `L[i] == e`
- if not, ask if `L[i]` is larger or smaller than `e`
- depending on answer, shift left or right

We're using the new version of divide-and-conquer algorithm that uses `bisect_search_helper`:

```
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

For `bisect_search2` and `bisect_search_helper`:
- $O(\log n)$ bisection search calls
    - reduce size fo problem by factor of 2 on each step
- pass list and indices as parameters
- list never copied, just repassed as pointer
- constant work inside function

**Overall complexity is smaller than linear search: $O(\log n)$**

## Searching a Sorted List - n is `len(L)`

### Incorrect Mindset Debunk

When using linear search, the search for an element, as previously said, is $O(n)$. Binary search is $O(\log n)$. 

So when does it make sense to sort first then search?

Let's assume $SORT$ will be the cost of sorting the list, I want to know **when that cost plus $O(\log n)$ is less than $O(n)$:** 

$SORT+O(\log n) < O(n)$

$SORT < O(n) - O(\log n)$

From here, we can say that we should sort first then search to decrease growth based on previous analysis on linear vs bisection, this is the condition to when does the cost of sorting is less expensive than the linear cost.

### WRONG! Sorting a collection of n elements is already $O(n)$, every element must be looked through at least once for the sort to execute!

## Amortized Cost - n is `len(L)`

- why bother sorting first?
- in some cases, **may sort a list once then do many searches**
- **amortize cost** of the sort over many searches

$SORT+K*O(\log n) < K*O(n)$
- for large $K$, **sort time becomes irrelevant**, if cost of sorting is small enough

## Sort Algorithms

### Monkey Sort / Bogo Sort

- 
![Bogosort](https://upload.wikimedia.org/wikipedia/commons/7/7b/Bogo_sort_animation.gif)
