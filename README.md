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

```
def bisect_search1(L, e):
    if L == []:
        return False
```

We start by avoiding empty inputs, if the user input is empty, `False` is returned.

```
    elif len(L) == 1:
        return L[0] == e
```

If the length of the list is 1, which is the only elements on the list, that number is returned.

```
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1( L[:half], e)
        else:
            return bisect_search1( L[half:], e)
```

Otherwise, divide the list by half, the program will return either half of the list where the number is at.

Full code:

```
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

## Complexity of Bisection Search 1

