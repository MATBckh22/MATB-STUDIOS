# Object Oriented Programming

Python supports different kinds of data, each is an object, every object has:
- a type
- an internal data representation (primitive or composite)
- a set of procedures for interaction with the object
- an object is an instance of a type
    - `1234` is an instance of an `int`
    - `"hello"` is an instance of a string

## Object Oriented Programming (OOP)

**Everything in python is an object**

- **create new** objects
- **manipulate** objects
- **destroy** objects
    - explicitly using `del` or just *forget about them* (binding to a new variable)

*Python system will reclaim destroyed or inaccessible
objects – called “garbage collection”*

## Objects

Objects are **data abstraction** that captures
- **internal representation**
    - through data attributes
- **interface** for interacting with object
    - through methods (aka procedures/functions)
    - defines behaviors but hides implementation

### Example: `[1,2,3,4]` has type list

Lists are represented internally through linked list of cells.

There are many ways to manipulate a list (mutating):
- `L[i]`, `L[i:j]`, `+`
- `len()`, `min()`, `max()`, `del(L[i])`
- `L.append()`, `L.extend()`, `L.count()`, `L.index()`, `L.insert()`, `L.pop()`, `L.remove()`, `L.reverse()`, `L.sort()`

Internal representation should be **private**, correct behavior may be compromised if you manipulate
internal representation directly.

## Advantages of OOP

-  **bundle data into packages** together with procedures
that work on them through well-defined interfaces
- **divide-and-conquer** development:
    - implement and test behavior of each class separately
    - increased modularity reduces complexity

- **reusing code is easier with classes:**
    - many Python modules define new classes
    - each class has a **separate environment (no collision on function names)**
    - inheritance allows subclasses to redefine or extend a selected subset of a superclass’ behavior

## Creating and Using Own Types With Classes

### Creating vs Using Classes

- **creating**
    - defining the class name
    - defining class attributes
    - *someone wrote code to implement a list class*

- **using**
    - creating new instances of objects
    - doing operations on the instances
    - `L=[1,2]` *and* `len(L)`

## Defining Own Types

`class` keyword is used to define a new type:

```
class Coordinate(object):
    #define attributes here
```
`Coordinate()` is the type of object u want to define where in the parentheses will be ur class parent.

