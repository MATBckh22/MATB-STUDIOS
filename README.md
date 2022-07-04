# Python Classes and Inheritance

### Author's note: Slide 1-7 is a recap of MIT6-Lec8, it is advised to quickly go through these slides to do a refresh on previous concepts and have an idea of the example showed.
-----

## Example: Creating an Animal Class

Here are we trying to group different objects part of the same type, in this case we're grouping animals. We begin with creating an animal class (initialization):

```
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None 

myanimal = Animal(3)
```

Notice `self.name = None` is a data attribute even though an instance is not initialized with it as a parameter. `self` variable refers to the newly created instance `myanimal` while `(3)` is mapped to `self.age` in class definition. 

A complete visualization of the process can be found here: [Detailed Visualization of Class `Animal`](https://pythontutor.com/render.html#code=class%20Animal%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20age%29%3A%0A%20%20%20%20%20%20%20%20self.age%20%3D%20age%0A%20%20%20%20%20%20%20%20self.name%20%3D%20None%20%0A%0Amyanimal%20%3D%20Animal%283%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Getter and Setter Methods

Getters and setters are often used when implementing a class, this is to prevent bugs when notations are changed:

```
class Animal(object):
    def __init__(self, age): #class initialization
        self.age = age
        self.name = None
    def get_age(self): #getter 1
        return self.age
    def get_name(self): #getter 2
        return self.name
    def set_age(self, newage): #setter 1
        self.age = newage
    def set_name(self, newname=""): #setter 2
        self.name = newname
    def __str__(self): #Defining str print method
        return "animal:"+str(self.name)+":"+str(self.age)
```

- Getters: return values of any data attributes

```
def get_age(self):
    return self.age
def get_name(self):
    return self.name
```

- Setters: set data attributes to mapped values

```
def set_age(self, newage):
    self.age = newage
def set_name(self, newname=""):
    self.name = newnam
```

*Note: getters and setters should be used outside of class to access data attributes.*

## Instance and Dot Notation 

Instantiation creates an instance of an object:

```
a = Animal(3)
```

Dot notation is used to access attributes (data and methods):

```
a.age #allowed but not recommended
a.get_age() #recommended getters and setters method
```

## Information Hiding

Author of class definition may change data attribute variable names:

```
class Animal(object):
    def __init__(self, age):
        self.years = age
    def get_age(self):
        return self.years
```

Notice `self.years = age` how `age` is replaced with `self.years`. Errors may occur if u are accessing **data attributes outside the class and class definiton changes.** 

It is advised to use getters and setters outside of the class, use `a.get_age()` and not `a.age`:
- good style
- easy to maintain code
- prevents bugs

### Python Not Great at Information Hiding

Python allows: **(not recommended)**

- **accessing data** outside class definition:
```
print(a.age)
```
- **writing data** outside class definition:
```
a.age = 'infinite'
```
- **creating data** attributes from an instance outside class definition:
```
a.size = "tiny"
```

## Default Arguments

Default Arguments for formal parameters are used if there's no specific argument is given:

```
def set_name(self, newname=""):
    self.name = newname
```

`""` is called default argument. It can be used in:

```
a = Animal(3)
a.set_name()
print(a.get_name()) 
```

`print(a.get_name())` prints an empty string `""`. No parameters are passed in `a.set_name()`, but because `newname=""` already has a default argument, it will print `""` instead of an error. If there are no formal parameters passed in the argument, then it will use whatever is set by default.

Normal argument:

```
a = Animal(3)
a.set_name("fluffy")
print(a.get_name())
```

This will print `"fluffy"` as it has an argument passed into `a.set_name()`.

## Hierarchies

Hierarchies are layers of classes to build up from:

- parent class (superclass)
    - highest level or higher level of class
- child class (subclass)
inherits all data and behaviors of parent class
    - add more info
    - add more behavior
    - override behavior

*Example: If animal is a parent class, it will have child classes people, cats, rabbits, etc. In a people's class it will have students, workers, etc.

**Different child classes have different behaviours, but they all have the same parent class attributes.**

## Inheritance: Parent Class

```
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def speak(self):
        print("hello")
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)
```

- everything is an object
- class `object` implements basic operations in phyton

## Inheritance: Subclass 

 

