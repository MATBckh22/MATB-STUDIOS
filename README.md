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

Similar to `def`, indent code to indicate which statements are part of the class definition.

`Coordinate is a a python object, all attributes are **inherited**:
- `Coordinate` is a subclass of `object`
-`object`is a superclass of `Coordinate`

## Attributes

**Data** and **procedures/methods** that belong to the class.

- **data attributes**
    - think of data as other objects that **make up the class**
    - *a coordinate is made up of two numbers*

- **methods** (procedural attributes)
    - think of methods as functions that only work with this class
    - **how to interact with the object**
    - *can define a distance between two coordinate objects but there is no meaning to a distance between two list objects*

## Defining How To Create An Instance of A Class

Before creating an instance of a class, **u have to define how to create an instance of it.**

`__init__()` is specifically used to initialize data attributes:

```
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

- **double underscore** `__` is a special method to create an instance
- `self` is a p**arameter that refers to an instance of a class**, this is going to be a placeholder for any sort of instance when it creates an object
- `x,y` is what **data initializes** a `Coordinate` object
- `self.x` and `self.y` are two **data attributes** for every `Coordinate` object.

## Actually Creating An Instance of A Class

After defining a way to create instances, we will begin to actually create them:

```
c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x)
print(origin.x)
```

- `Coordinate(3,4)` **creates a new object** of type `Coordinate` and **passes 3 and 4** to the `__init__`
- the dot in `print(c.x)` is used to **access an attribute of instance c**
- don't have to provide a separate argument for `self`, as python automatically assigns it by default. Meaning that `self` by default is assigned to `c`

## Methods

A method in python is seen as a procedural attribute, it's like a **function that works only with this class.**

- python always passes the object as first argument
    - **convention is to use** `self` **as the name of the first argument of all methods**
- the `.` operator is used to **access any attribute**
    - a data attribute of an object
    - a method of an object

## Defining A Method For The Coordinate Class

Methods behave like a function other than `self` and dot notation (take params, do operations, return):

```
def distance(self, other):
# code here
```
This is the format to **define a method.** Inside the parentheses of a method it **refers to an existing instance called** `self` **and creates another parameter `other`,** combining the previous instance definition will look like this:

```
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
```
Instance definitions are always followed by a method, in this case it's `distance`. In `distance` parameter there will be `self` and `other`:
- `self` is used to refer to any instance
- `other` is used as another parameter to method

`x_diff_sq` and `y_diff_sq` are variables to calculate the difference of x and y attributes squared.

Return operator is also used under method block as it behaves similarly to functions.

## Using Methods

