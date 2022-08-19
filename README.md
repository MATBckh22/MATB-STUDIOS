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

```python
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
```

This search method has to look through all of the elements to decide it's not there, for $O(len(L))$ the loop has to test if `e == L[i]`. Overall complexity will be $O(n)$ where n is `len(L)`.

### Sorted Linear

```python
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

$SORT+K * O(\log n) < K * O(n)$
- for large $K$, **sort time becomes irrelevant**, if cost of sorting is small enough

## Sort Algorithms

### Monkey Sort / Bogo Sort

- sorting elements by creating random permutations
- throwing them up in the air repeatedly waiting for a miracle

![Bogo Sort](https://upload.wikimedia.org/wikipedia/commons/7/7b/Bogo_sort_animation.gif)

### Complexity of Bogo Sort

```python
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

```python
def bubble_sort(L):
    swap = False
```

We initially set a flag `swap = False` for an unsorted list.

```python
while not swap:
    print('bubble sort: ' + str(L))
    swap = True
```

Looping the print operation so we can see the process of sorting, `True` is set to to reinitialize the sorting process.

```python
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

```python
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

**Overall Complexity: $O(n^2)$ where n is** `len(L)`**:**

- doing $len(L)-1$ comparisons and $Len(L)-1$ passes

### Selection Sort

This is one of the sorting system that we often use realistically: `{1}, {5}, {6}, {2}, {11}`

- first step: 
    - **extract minimum element**
    - **swap it at index 0**
    - list shortened by 1

`{1}, {5}, {6}, {2}, {11}`: Extract `{1}`

Return sorted list: `{1}`

Return unsorted list: `{5}, {6}, {2}, {11}`

- subsequent/repeating step:
    - **remaining sublist extract another minimum element**
    - **swap that with index 1**

`{5}, {6}, {2}, {11}`: Extract `{2}`

Return sorted list: `{1}, {2}`

Return unsorted list: `{5}, {6}, {11}`

...

Return sorted list: `{1}, {2}, {5}, {6}, {11}`

- keep the left portion of the list sorted:
    - **for i steps, first i elements are sorted**
    - all other elements are bigger than first i elements

| Sorted | Unsorted |
| - | - |
| - | `{1}, {5}, {6}, {2}, {11}`
| `{1}` | `{5}, {6}, {2}, {11}` 
| `{1}, {2}` | `{5}, {6}, {11}`
| `{1}, {2}, {5}` | `{6}, {11}`
| `{1}, {2}, {5}, {6}` | `{11}`
| `{1}, {2}, {5}, {6}, {11}` | -


![Selection Sort](https://upload.wikimedia.org/wikipedia/commons/f/f6/Selection_Sort_Animation.gif)

### Complexity of Selection Sort

```python
def selection_sort(L):
    suffixSt = 0
    while suffixSt !=  len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
```

We will start off with a counter variable `suffixSt`. In the while loop where the counter doesn't go over the length of the list, it keeps track of two variables:
- `i`: element counter in the list
- `suffixSt`: element to compare

From the list, let's say `suffixSt` is 1 which is the 2nd variable of the list, `L[i]` will go through every index to find whether an element is less than the 2nd variable `L[suffixSt]`. If it is, swap them and add the counter by 1, keeping the left part of the list sorted.

[Visualization](https://pythontutor.com/render.html#code=def%20selection_sort%28L%29%3A%0A%20%20%20%20suffixSt%20%3D%200%0A%20%20%20%20while%20suffixSt%20!%3D%20%20len%28L%29%3A%0A%20%20%20%20%20%20%20%20print%28'selection%20sort%3A%20'%20%2B%20str%28L%29%29%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28suffixSt,%20len%28L%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20L%5Bi%5D%20%3C%20L%5BsuffixSt%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20L%5BsuffixSt%5D,%20L%5Bi%5D%20%3D%20L%5Bi%5D,%20L%5BsuffixSt%5D%0A%20%20%20%20%20%20%20%20suffixSt%20%2B%3D%201%0A%20%0AtestList%20%3D%20%5B1,3,5,7,2,6,25,18,13%5D%0A%20%20%20%20%20%20%20%0Aprint%28''%29%0Aprint%28selection_sort%28testList%29%29%0Aprint%28testList%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

- outer loop: executes `len(L)` times
- inner loop: executes `len(L) - suffixSt` times, which is $O(len(L))$

Since this is a nested loop, the complexity of a selection sort is quadratic: $O(n^2)$

### Merge Sort

Merge sort is a sorting method using a **divide-and-conquer approach:**
- if `len(L)` is 0 or 1, already sorted
- if list has more than one element, split into two groups and sort each
- merge sorted sublists
    - **look at first element of each, move smaller to the end of the result**
    - **when one list empty, copy rest of the list**

**We will break this method mainly into three steps:**

### Spliting

Assume we have a list of `{1}, {5}, {9}, {7}, {0}, {10}, {20}`

- split list into groups of two, remainding element will also be in a group:

S1: `{1}, {5}`

S2: `{9}, {7}`

S3: `{0}, {10}`

S4: `{20}`

### Compare

- compare each element in the group and sort accordingly:

S1: `{1}, {5}`

S2: `{7}, {9}`

S3: `{0}, {10}`

S4: `{20}`

### Merge

- merge two groups together and compare:
    - smallest of each group first
    - winner compare to larger element in 1st group
    - winner compare to larger element in 2nd group

M1 = S1 + S2 = `{1}, {5}` + `{9}, {7}`

| Compare | Winner | Sorted List |
| - | - | -|
| `{1}, {9}` | `{9}` | `{1}`
| `{9}, {5}` | `{9}` | `{1}, {5}`
| `{9}, {7}` | `{9}` | `{1}, {5}, {7}`
| - | - | `{1}, {5}, {7}, {9}`

M2 = S3 + S4 = `{0}, {10}` + `{20}`

| Compare | Winner | Sorted List |
| - | - | -|
| `{20}, {0}` | `{20}` | `{0}`
| `{20}, {10}` | `{20}` | `{0}, {10}`
| - | - | `{0}, {10}, {20}`

### Repeat

- merge again and sort:

M = M1 + M2 = `{1}, {5}, {7}, {9}` + `{0}, {10}, {20}`

| Compare | Winner | Sorted List |
| - | - | -|
| `{0}, {1}` | `{1}` | `{0}`
| `{1}, {10}` | `{10}` | `{0}, {1}`
| `{10}, {5}` | `{10}` | `{0}, {1}, {5}`
| `{10}, {7}` | `{10}` | `{0}, {1}, {5}, {7}`
| `{10}, {9}` | `{10}` | `{0}, {1}, {5}, {7}, {9}`
| - | - | `{0}, {1}, {5}, {7}, {9}, {10}, {20}`

Return sorted list: `{0}, {1}, {5}, {7}, {9}, {10}, {20}`

![Merge Sort](https://upload.wikimedia.org/wikipedia/commons/8/8e/Merge_sort_animation.gif)

### Merge Sort Algorithm - Recursive `merge_sort`

This section will focus on spliting the list into sublists for them to be compared after: [Visualization](https://pythontutor.com/render.html#code=def%20merge_sort%28L%29%3A%0A%20%20%20%20print%28'merge%20sort%3A%20'%20%2B%20str%28L%29%29%0A%20%20%20%20if%20len%28L%29%20%3C%202%3A%0A%20%20%20%20%20%20%20%20return%20L%5B%3A%5D%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20middle%20%3D%20len%28L%29//2%0A%20%20%20%20%20%20%20%20left%20%3D%20merge_sort%28L%5B%3Amiddle%5D%29%0A%20%20%20%20%20%20%20%20right%20%3D%20merge_sort%28L%5Bmiddle%3A%5D%29%0A%20%20%20%20%20%20%20%20return%20merge%28left,%20right%29%0A%20%20%20%20%20%20%20%20%0AtestList%20%3D%20%5B1,3,5,7,2,6,25,18,13%5D%0A%0Aprint%28''%29%0Aprint%28merge_sort%28testList%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
```

This function is to do two things:
- base case: if `len(L)` is less than 2, break the list in half and return this to `merge` (sorting function)
- recursive step: otherwise, break the length of the list into two parts `left` and `right` and return them again to `merge`

This is to divide list into halves so smallest pieces down one branch will be considered before moving to larger pieces.

### Merging Sublists Step - `merge`

This function will execute the merging and comparing section of the sorting process:

```python
def merge(left, right):
    result = []
    i,j = 0,0
```

We begin by setting two variables `i` and `j` and a new `result` list to keep track of the sorted part of the list.

```python
while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
```

This is to say that when there's still elements in both lists, compare the smallest input of both lists:
- if the input in left section is smaller than the right, add the input into the sorted list as the smallest number and add `i` counter by 1
- otherwise, add the input in the right section to the sorted list as the smallest number and add `j` counter by 1

```python
while (i < len(left)):
        result.append(left[i])
        i += 1
while (j < len(right)):
        result.append(right[j])
        j += 1
```

This handles the copying part of the sorting process. If either `left` or `right` is empty, copy the remaining elements of the other list into result to skip unnecessary sorting.

Full code:

```python
def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result
```

### Complexity of `merge_sort` and `merge`

Full code: [Visualization](https://pythontutor.com/render.html#code=def%20merge%28left,%20right%29%3A%0A%20%20%20%20result%20%3D%20%5B%5D%0A%20%20%20%20i,j%20%3D%200,0%0A%20%20%20%20while%20i%20%3C%20len%28left%29%20and%20j%20%3C%20len%28right%29%3A%0A%20%20%20%20%20%20%20%20if%20left%5Bi%5D%20%3C%20right%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result.append%28left%5Bi%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result.append%28right%5Bj%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%2B%3D%201%0A%20%20%20%20while%20%28i%20%3C%20len%28left%29%29%3A%0A%20%20%20%20%20%20%20%20result.append%28left%5Bi%5D%29%0A%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%20%20%20%20while%20%28j%20%3C%20len%28right%29%29%3A%0A%20%20%20%20%20%20%20%20result.append%28right%5Bj%5D%29%0A%20%20%20%20%20%20%20%20j%20%2B%3D%201%0A%20%20%20%20print%28'merge%3A%20'%20%2B%20str%28left%29%20%2B%20'%26'%20%2B%20str%28right%29%20%2B%20'%20to%20'%20%2Bstr%28result%29%29%0A%20%20%20%20return%20result%0A%0Adef%20merge_sort%28L%29%3A%0A%20%20%20%20print%28'merge%20sort%3A%20'%20%2B%20str%28L%29%29%0A%20%20%20%20if%20len%28L%29%20%3C%202%3A%0A%20%20%20%20%20%20%20%20return%20L%5B%3A%5D%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20middle%20%3D%20len%28L%29//2%0A%20%20%20%20%20%20%20%20left%20%3D%20merge_sort%28L%5B%3Amiddle%5D%29%0A%20%20%20%20%20%20%20%20right%20%3D%20merge_sort%28L%5Bmiddle%3A%5D%29%0A%20%20%20%20%20%20%20%20return%20merge%28left,%20right%29%0A%20%20%20%20%20%20%20%20%0AtestList%20%3D%20%5B1,3,5,7,2,6,25,18,13%5D%0A%0Aprint%28''%29%0Aprint%28merge_sort%28testList%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
def merge(left, right): 
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result

def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
        
testList = [1,3,5,7,2,6,25,18,13]

print('')
print(merge_sort(testList))
```

![Merge Sort Visualization](https://scontent.xx.fbcdn.net/v/t1.15752-9/289054493_610030770441958_4212030267877862078_n.png?stp=dst-png_p403x403&_nc_cat=104&ccb=1-7&_nc_sid=aee45a&_nc_ohc=8YZdsuN23VsAX83cqls&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVKKWHGKkZdP8Dq13NyXfaYxz3Pl0CqsVzSUePCMe8pvLQ&oe=62FE80AC)

`merge_sort`
- divide list into **two halves**
- considers **smallest pieces down one branch first before moving to larger pieces**

**This is a recursive program, hence overall complexity: $O(\log n)$**

`merge`
- goes through two lists and **passing only once**
- compare only **smallest elements in each sublist**
- **$O(len(left)+len(right))$ copied elements**
- comparisons consider the longer lengths of the list
    - **linear in length of lists**

**Overall complexity: $O(n)$**

`merge_sort` and `merge`
- first recursion level:
    - $\frac{n}{2}$ elements in each list
    - $O(n)+O(n) = O(n)$ where n is `len(L)`
- second recursion level:
    - $\frac{n}{4}$ elements in each list
    - two merges
        - $O(n)$ where n is `len(L)`
- each recursive level is $O(n)$ where dividing list in half with each recursive call is $O(\log n)$

**Complexity of merge sort: $O(n) * O(\log n) = O(n \log n)$ (fastest among sorting algorithms discussed until now!)**

## Sorting Summary

| Algorithms | Complexity |
| - | - |
| Bogo | unbounded $O(?)$
| Bubble | $O(n^2)$
| Selection | $O(n^2)$
| Merge | $O(n \log n)$

## Three A's of Computational Thinking

### Abstraction

- choosing right abstractions
- operating in multiple layers of abstraction simultaneously
- defining relationships bettween abstraction layers

### Automation

- think in terms of mechanizing abstractions
    - possible because we have precise and exacting notations and models
    - some "machine" that can interpret our notations

### Algorithms

- language for describing automated processes
- also allows abstraction of details
- language for communicating ideas and processes

## Aspects of Computational Thinking

- analyzing difficulty of a problem and the best solution to solve it
    - theortical computer science gives precise meaning to these and related questions and their answers
- thinking recursively
    - reformulating a seemingly difficult problem into smaller problems
    - reduction, embedding, transformation, simulation



