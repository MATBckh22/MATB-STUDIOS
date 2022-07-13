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

[Visualization](https://pythontutor.com/render.html#code=def%20bisect_search2%28L,%20e%29%3A%0A%20%20%20%20def%20bisect_search_helper%28L,%20e,%20low,%20high%29%3A%0A%20%20%20%20%20%20%20%20print%28'low%3A%20'%20%2B%20str%28low%29%20%2B%20'%3B%20high%3A%20'%20%2B%20str%28high%29%29%20%20%23added%20to%20visualize%0A%20%20%20%20%20%20%20%20if%20high%20%3D%3D%20low%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20L%5Blow%5D%20%3D%3D%20e%0A%20%20%20%20%20%20%20%20mid%20%3D%20%28low%20%2B%20high%29//2%0A%20%20%20%20%20%20%20%20if%20L%5Bmid%5D%20%3D%3D%20e%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20elif%20L%5Bmid%5D%20%3E%20e%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20low%20%3D%3D%20mid%3A%20%23nothing%20left%20to%20search%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20bisect_search_helper%28L,%20e,%20low,%20mid%20-%201%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20bisect_search_helper%28L,%20e,%20mid%20%2B%201,%20high%29%0A%20%20%20%20if%20len%28L%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20bisect_search_helper%28L,%20e,%200,%20len%28L%29%20-%201%29%0A%0AtestList%20%3D%20%5B%5D%0Afor%20i%20in%20range%28100%29%3A%0A%20%20%20%20testList.append%28i%29%0A%20%20%20%20%0Aprint%28bisect_search2%28testList,%2076%29%29&cumulative=false&curInstr=265&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
