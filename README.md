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

- sorting elements by creating random permutations
- throwing them up in the air repeatedly waiting for a miracle

![Bogo Sort](https://upload.wikimedia.org/wikipedia/commons/7/7b/Bogo_sort_animation.gif)

### Complexity of Bogo Sort

```
def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)
```

- best case: $O(n)$, n is `len(L)` to check if sorted
- worst case: $O(?)$, unbounded if really unlucky (forever)

### Bubble Sort

Assume a list of 5 elements: `{1}, {5}, {6}, {2}, {11}`

- **compare and swap** pairs of elements such that smaller is first:

`{1}, {5}`: Correct

`{5}, {6}`: Correct

`{6}, {2}`: Incorrect, swap: `{2}, {6}`

`{6}, {11}`: Correct

Return list: `{1}, {5}, {2}, {6}, {11}`

- **repeat again and stop when no more swaps are made:**

`{1}, {5}, {2}, {6}, {11}`

`{1}, {2}, {5}, {6}, {11}`

- largest unsorted element always at **end after pass, so at most n passes:**

`{1}, {2}, {5}, {6}, {11}`: Correct

![Bubble Sort](https://upload.wikimedia.org/wikipedia/commons/3/37/Bubble_sort_animation.gif)

### Complexity of Bubble Sort

Bubble sort code looks like this:

```
def bubble_sort(L):
    swap = False
```

We initially set a flag `swap = False` for an unsorted list.

```
while not swap:
    print('bubble sort: ' + str(L))
    swap = True
```

Looping the print operation so we can see the process of sorting, `True` is set to to reinitialize the sorting process.

```
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
```

This will be the main sorting process. `if L[j-1] > L[j]` compares two elements:
- if (n-1)th element is smaller than nth element, `swap` remains `True`, as previously set, program will continue to the next pair
- if (n-1)th element is bigger than nth element, `swap` will be changed to `False`, current positions in the pair of elements will be swapped


Full code: [Visualization](https://pythontutor.com/render.html#code=def%20bubble_sort%28L%29%3A%0A%20%20%20%20swap%20%3D%20False%0A%20%20%20%20while%20not%20swap%3A%0A%20%20%20%20%20%20%20%20print%28'bubble%20sort%3A%20'%20%2B%20str%28L%29%29%0A%20%20%20%20%20%20%20%20swap%20%3D%20True%0A%20%20%20%20%20%20%20%20for%20j%20in%20range%281,%20len%28L%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20L%5Bj-1%5D%20%3E%20L%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20swap%20%3D%20False%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20temp%20%3D%20L%5Bj%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20L%5Bj%5D%20%3D%20L%5Bj-1%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20L%5Bj-1%5D%20%3D%20temp%0A%0AtestList%20%3D%20%5B1,3,5,7,2,6,25,18,13%5D%0A%0Aprint%28''%29%0Aprint%28bubble_sort%28testList%29%29%0Aprint%28testList%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```
def bubble_sort(L):
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

testList = [1,3,5,7,2,6,25,18,13]

print('')
print(bubble_sort(testList))
print(testList)
```

- inner for loop is for the **comparisons**
- outer while loop is for doing **multiple passes until no more swaps**

**Overall Complexity: $O(n^2)$ where n is** `len(L)`**, note that this is not a nested loop.**
- doing $len(L)-1$ comparisons and $Len(L)-1$ passes

### Selection Sort
