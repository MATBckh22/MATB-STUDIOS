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

 We can add functionality to a subclass, in this case we're adding `speak()` while inheriting all attributes of `Animal`

```
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)
```
`speak()`
- instance of type `Cat` can be called with new methods
- instance of type Animal throws error if called with `Cat`’s new method


`__str__` attribute overrides the original `__str__` in the parent class. However, notice there's no `__init__` attribute defined here, python will trace back the attribute in the parent class.

## Which Method to Use?

- subclass can have **methods with same name** as superclass
- for an instance of a class, look for a method name in **current class definition**
- if not found, look for method name **up the hierarchy** (in parent, then grandparent, and so on)
- use first method up the hierarchy that you found with that method name

### Inheritance Example

```
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
```

We start by creating data attributes for a list of friends. 
- `Animal.__init__(self, age)` calls `Animal` constructor
- `self.set_name(name)` calls `Animal`'s method
- `self.friends = []` adds a new data attribute

Here we define a set of methods:

```
def get_friends(self):
        return self.friends
```

Returns the list of friends (getter)

```
def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
```

Adds a friend to the end of the list.

```
def speak(self):
        print("hello")
```

Implementation of `speak()` method to print "hello".

```
def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
```

Prints the age difference.

```
def __str__(self):
    return "person:"+str(self.name)+":"+str(self.age)
```

Overwriting `Animal`'s `__str__` method to return a string.

Full code: [Visualization](https://pythontutor.com/render.html#code=class%20Animal%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20age%29%3A%0A%20%20%20%20%20%20%20%20self.age%20%3D%20age%0A%20%20%20%20%20%20%20%20self.name%20%3D%20None%0A%20%20%20%20def%20get_age%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.age%0A%20%20%20%20def%20get_name%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.name%0A%20%20%20%20def%20set_age%28self,%20newage%29%3A%0A%20%20%20%20%20%20%20%20self.age%20%3D%20newage%0A%20%20%20%20def%20set_name%28self,%20newname%3D%22%22%29%3A%0A%20%20%20%20%20%20%20%20self.name%20%3D%20newname%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22animal%3A%22%2Bstr%28self.name%29%2B%22%3A%22%2Bstr%28self.age%29%0A%0Aclass%20Person%28Animal%29%3A%0A%20%20%20%20def%20__init__%28self,%20name,%20age%29%3A%0A%20%20%20%20%20%20%20%20Animal.__init__%28self,%20age%29%0A%20%20%20%20%20%20%20%20self.set_name%28name%29%0A%20%20%20%20%20%20%20%20self.friends%20%3D%20%5B%5D%0A%20%20%20%20def%20get_friends%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.friends%0A%20%20%20%20def%20add_friend%28self,%20fname%29%3A%0A%20%20%20%20%20%20%20%20if%20fname%20not%20in%20self.friends%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.friends.append%28fname%29%0A%20%20%20%20def%20speak%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28%22hello%22%29%0A%20%20%20%20def%20age_diff%28self,%20other%29%3A%0A%20%20%20%20%20%20%20%20diff%20%3D%20self.age%20-%20other.age%0A%20%20%20%20%20%20%20%20print%28abs%28diff%29,%20%22year%20difference%22%29%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22person%3A%22%2Bstr%28self.name%29%2B%22%3A%22%2Bstr%28self.age%29%0A%0Aprint%28%22%5Cn----%20person%20tests%20----%22%29%0Ap1%20%3D%20Person%28%22jack%22,%2030%29%0Ap2%20%3D%20Person%28%22jill%22,%2025%29%0Aprint%28p1.get_name%28%29%29%0Aprint%28p1.get_age%28%29%29%0Aprint%28p2.get_name%28%29%29%0Aprint%28p2.get_age%28%29%29%0Aprint%28p1%29%0Ap1.speak%28%29%0Ap1.age_diff%28p2%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

print("\n---- person tests ----")
p1 = Person("jack", 30)
p2 = Person("jill", 25)
print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())
print(p1)
p1.speak()
p1.age_diff(p2)
```

### Branching From Inheritance Example

Here we continue to create a subclass of `Student` while inheriting all attributes of `Person`:

```
import random
```

This will bring in method from `random` class:
- `random` is by default in python docs
- `random()` method gives back float in  [0,1)

```
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
```

Setting up new data attributes while using default arguments `self`, `name` and `age`. We also set `major=None` beforehand and a new attribute `self.major`.

```
def change_major(self, major):
        self.major = major
```

Setter method for students to change major.

```
def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
```

Here we're overwriting `speak()` to implement the `random()` method. `r = random.random()` is used to get a number randomly set between 0 to 1 (not including 1). Continuing from here, when it retrieves the random number it will look for a print operation to run correspondingly.

```
 def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
```

Overwriting `__str__` again.

Full code: [Visualization](https://pythontutor.com/render.html#code=class%20Animal%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20age%29%3A%0A%20%20%20%20%20%20%20%20self.age%20%3D%20age%0A%20%20%20%20%20%20%20%20self.name%20%3D%20None%0A%20%20%20%20def%20get_age%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.age%0A%20%20%20%20def%20get_name%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.name%0A%20%20%20%20def%20set_age%28self,%20newage%29%3A%0A%20%20%20%20%20%20%20%20self.age%20%3D%20newage%0A%20%20%20%20def%20set_name%28self,%20newname%3D%22%22%29%3A%0A%20%20%20%20%20%20%20%20self.name%20%3D%20newname%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22animal%3A%22%2Bstr%28self.name%29%2B%22%3A%22%2Bstr%28self.age%29%0A%20%20%20%20%20%20%20%20%0Aclass%20Person%28Animal%29%3A%0A%20%20%20%20def%20__init__%28self,%20name,%20age%29%3A%0A%20%20%20%20%20%20%20%20Animal.__init__%28self,%20age%29%0A%20%20%20%20%20%20%20%20self.set_name%28name%29%0A%20%20%20%20%20%20%20%20self.friends%20%3D%20%5B%5D%0A%20%20%20%20def%20get_friends%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.friends%0A%20%20%20%20def%20speak%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28%22hello%22%29%0A%20%20%20%20def%20add_friend%28self,%20fname%29%3A%0A%20%20%20%20%20%20%20%20if%20fname%20not%20in%20self.friends%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.friends.append%28fname%29%0A%20%20%20%20def%20age_diff%28self,%20other%29%3A%0A%20%20%20%20%20%20%20%20diff%20%3D%20self.age%20-%20other.age%0A%20%20%20%20%20%20%20%20print%28abs%28diff%29,%20%22year%20difference%22%29%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22person%3A%22%2Bstr%28self.name%29%2B%22%3A%22%2Bstr%28self.age%29%0A%20%20%20%20%20%20%20%20%0Aimport%20random%0A%0Aclass%20Student%28Person%29%3A%0A%20%20%20%20def%20__init__%28self,%20name,%20age,%20major%3DNone%29%3A%0A%20%20%20%20%20%20%20%20Person.__init__%28self,%20name,%20age%29%0A%20%20%20%20%20%20%20%20self.major%20%3D%20major%0A%20%20%20%20def%20change_major%28self,%20major%29%3A%0A%20%20%20%20%20%20%20%20self.major%20%3D%20major%0A%20%20%20%20def%20speak%28self%29%3A%0A%20%20%20%20%20%20%20%20r%20%3D%20random.random%28%29%0A%20%20%20%20%20%20%20%20if%20r%20%3C%200.25%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22i%20have%20homework%22%29%0A%20%20%20%20%20%20%20%20elif%200.25%20%3C%3D%20r%20%3C%200.5%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22i%20need%20sleep%22%29%0A%20%20%20%20%20%20%20%20elif%200.5%20%3C%3D%20r%20%3C%200.75%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22i%20should%20eat%22%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22i%20am%20watching%20tv%22%29%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22student%3A%22%2Bstr%28self.name%29%2B%22%3A%22%2Bstr%28self.age%29%2B%22%3A%22%2Bstr%28self.major%29%0A%0Aprint%28%22%5Cn----%20student%20tests%20----%22%29%0As1%20%3D%20Student%28'alice',%2020,%20%22CS%22%29%0As2%20%3D%20Student%28'beth',%2018%29%0Aprint%28s1%29%0Aprint%28s2%29%0Aprint%28s1.get_name%28%29,%22says%3A%22,%20end%3D%22%20%22%29%0As1.speak%28%29%0Aprint%28s2.get_name%28%29,%22says%3A%22,%20end%3D%22%20%22%29%0As2.speak%28%29&cumulative=false&curInstr=53&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```
import random

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)

print("\n---- student tests ----")
s1 = Student('alice', 20, "CS")
s2 = Student('beth', 18)
print(s1)
print(s2)
print(s1.get_name(),"says:", end=" ")
s1.speak()
print(s2.get_name(),"says:", end=" ")
s2.speak()
```

## Class Variables and The `Rabbit` Subclass

Class variables are different than instance variables, **their values are shared between all instances of a class:**

```
class Rabbit(Animal):
    # a class variable, tag, shared across all instances
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
```

`tag` is a class variable initialized to 1. `__init__` defines the creation of the object, `self`, `age` and two `parents`. Both of the parents' data attributes will then be set.

Notice `self.rid = Rabbit.tag`, **instance variable** `self.rid` is assigned to a **class variable** `Rabbit.tag`. When initialized, `tag` will be at 1, but later increments by 1 in the `__init__`.

**This shows that whenever other instances are created these instances will access the updated value of** `tag`**:**

- `tag` used to give unique id to each new rabbit instance

[Jump to 39:01 for a more detailed explanation of this](https://youtu.be/FlGjISF3l78)

## `Rabbit` Getter Methods

```
def get_rid(self):
        # zfill used to add leading zeroes 001 instead of 1
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
```

`zfill()` is a method on a string to pad the beginning with zeros, it prints 001 instead of 1

These are the getter methods specific for a `Rabbit` class since we already have inherited `Animal` class getters `get_name` and `get_age`.

## Working With Your Own Types

```
def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
```

Here we return a new `Rabbit` object. It recalls `0` as the rabbit's age, `self` as the parent of the new rabbit `parent1 = None1`, `other` as the other parent `parent2 = None`.

- define + operator between two `Rabbit` instances
    - define what something like this does: r4 = r1 + r2 where r1 and r2 are `Rabbit` instances
    - r4 is a new `Rabbit` instance with age 0
    - r4 has `self` as one parent and `other` as the other parent
    - in `__init__` `parent1` and `parent2` are of type `Rabbit`

## Special Method to Compare Two `Rabbits`

This is a method that allows the program decide that **two rabbits are equal if they have the same two parents:**

```
def __eq__(self, other):
        # compare the ids of self and other's parents
        # don't care about the order of the parents
        # the backslash tells python I want to break up my line
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
```

`parents_same` and `parents_opposite` are booleans. They either return the same or the opposite parents.

- compare ids of parents since ids are unique (due to class variables)
- note you can’t compare objects directly
    - exp: `self.parent1 == other.parent1`
    - this calls the `__eq__` method over and over until call it on `None` and gives an `AttributeError` when it tries to do `None.parent1`

Full Code: [Visualization](https://pythontutor.com/render.html#code=class%20Animal%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20age%29%3A%0A%20%20%20%20%20%20%20%20self.age%20%3D%20age%0A%20%20%20%20%20%20%20%20self.name%20%3D%20None%0A%20%20%20%20def%20get_age%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.age%0A%20%20%20%20def%20get_name%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.name%0A%20%20%20%20def%20set_age%28self,%20newage%29%3A%0A%20%20%20%20%20%20%20%20self.age%20%3D%20newage%0A%20%20%20%20def%20set_name%28self,%20newname%3D%22%22%29%3A%0A%20%20%20%20%20%20%20%20self.name%20%3D%20newname%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22animal%3A%22%2Bstr%28self.name%29%2B%22%3A%22%2Bstr%28self.age%29%0A%20%20%20%20%20%20%20%20%0Aclass%20Rabbit%28Animal%29%3A%0A%20%20%20%20%23%20a%20class%20variable,%20tag,%20shared%20across%20all%20instances%0A%20%20%20%20tag%20%3D%201%0A%20%20%20%20def%20__init__%28self,%20age,%20parent1%3DNone,%20parent2%3DNone%29%3A%0A%20%20%20%20%20%20%20%20Animal.__init__%28self,%20age%29%0A%20%20%20%20%20%20%20%20self.parent1%20%3D%20parent1%0A%20%20%20%20%20%20%20%20self.parent2%20%3D%20parent2%0A%20%20%20%20%20%20%20%20self.rid%20%3D%20Rabbit.tag%0A%20%20%20%20%20%20%20%20Rabbit.tag%20%2B%3D%201%0A%20%20%20%20def%20get_rid%28self%29%3A%0A%20%20%20%20%20%20%20%20%23%20zfill%20used%20to%20add%20leading%20zeroes%20001%20instead%20of%201%0A%20%20%20%20%20%20%20%20return%20str%28self.rid%29.zfill%283%29%0A%20%20%20%20def%20get_parent1%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.parent1%0A%20%20%20%20def%20get_parent2%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.parent2%0A%20%20%20%20def%20__add__%28self,%20other%29%3A%0A%20%20%20%20%20%20%20%20%23%20returning%20object%20of%20same%20type%20as%20this%20class%0A%20%20%20%20%20%20%20%20return%20Rabbit%280,%20self,%20other%29%0A%20%20%20%20def%20__eq__%28self,%20other%29%3A%0A%20%20%20%20%20%20%20%20%23%20compare%20the%20ids%20of%20self%20and%20other's%20parents%0A%20%20%20%20%20%20%20%20%23%20don't%20care%20about%20the%20order%20of%20the%20parents%0A%20%20%20%20%20%20%20%20%23%20the%20backslash%20tells%20python%20I%20want%20to%20break%20up%20my%20line%0A%20%20%20%20%20%20%20%20parents_same%20%3D%20self.parent1.rid%20%3D%3D%20other.parent1.rid%20%5C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20and%20self.parent2.rid%20%3D%3D%20other.parent2.rid%0A%20%20%20%20%20%20%20%20parents_opposite%20%3D%20self.parent2.rid%20%3D%3D%20other.parent1.rid%20%5C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20and%20self.parent1.rid%20%3D%3D%20other.parent2.rid%0A%20%20%20%20%20%20%20%20return%20parents_same%20or%20parents_opposite%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22rabbit%3A%22%2B%20self.get_rid%28%29%0A%0Aprint%28%22%5Cn----%20rabbit%20tests%20----%22%29%0Aprint%28%22----%20testing%20creating%20rabbits%20----%22%29%0Ar1%20%3D%20Rabbit%283%29%0Ar2%20%3D%20Rabbit%284%29%0Ar3%20%3D%20Rabbit%285%29%0Aprint%28%22r1%3A%22,%20r1%29%0Aprint%28%22r2%3A%22,%20r2%29%0Aprint%28%22r3%3A%22,%20r3%29%0Aprint%28%22r1%20parent1%3A%22,%20r1.get_parent1%28%29%29%0Aprint%28%22r1%20parent2%3A%22,%20r1.get_parent2%28%29%29%0A%0Aprint%28%22----%20testing%20rabbit%20addition%20----%22%29%0Ar4%20%3D%20r1%2Br2%20%20%20%23%20r1.__add__%28r2%29%0Aprint%28%22r1%3A%22,%20r1%29%0Aprint%28%22r2%3A%22,%20r2%29%0Aprint%28%22r4%3A%22,%20r4%29%0Aprint%28%22r4%20parent1%3A%22,%20r4.get_parent1%28%29%29%0Aprint%28%22r4%20parent2%3A%22,%20r4.get_parent2%28%29%29%0A%0Aprint%28%22----%20testing%20rabbit%20equality%20----%22%29%0Ar5%20%3D%20r3%2Br4%0Ar6%20%3D%20r4%2Br3%0Aprint%28%22r3%3A%22,%20r3%29%0Aprint%28%22r4%3A%22,%20r4%29%0Aprint%28%22r5%3A%22,%20r5%29%0Aprint%28%22r6%3A%22,%20r6%29%0Aprint%28%22r5%20parent1%3A%22,%20r5.get_parent1%28%29%29%0Aprint%28%22r5%20parent2%3A%22,%20r5.get_parent2%28%29%29%0Aprint%28%22r6%20parent1%3A%22,%20r6.get_parent1%28%29%29%0Aprint%28%22r6%20parent2%3A%22,%20r6.get_parent2%28%29%29%0Aprint%28%22r5%20and%20r6%20have%20same%20parents%3F%22,%20r5%20%3D%3D%20r6%29%0Aprint%28%22r4%20and%20r6%20have%20same%20parents%3F%22,%20r4%20%3D%3D%20r6%29&cumulative=false&curInstr=238&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```
class Rabbit(Animal):
    # a class variable, tag, shared across all instances
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        # zfill used to add leading zeroes 001 instead of 1
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    def __eq__(self, other):
        # compare the ids of self and other's parents
        # don't care about the order of the parents
        # the backslash tells python I want to break up my line
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    def __str__(self):
        return "rabbit:"+ self.get_rid()

print("\n---- rabbit tests ----")
print("---- testing creating rabbits ----")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())

print("---- testing rabbit addition ----")
r4 = r1+r2   # r1.__add__(r2)
print("r1:", r1)
print("r2:", r2)
print("r4:", r4)
print("r4 parent1:", r4.get_parent1())
print("r4 parent2:", r4.get_parent2())

print("---- testing rabbit equality ----")
r5 = r3+r4
r6 = r4+r3
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r5 parent1:", r5.get_parent1())
print("r5 parent2:", r5.get_parent2())
print("r6 parent1:", r6.get_parent1())
print("r6 parent2:", r6.get_parent2())
print("r5 and r6 have same parents?", r5 == r6)
print("r4 and r6 have same parents?", r4 == r6)
```

## Conclusion on OOP

- **create** your own collections of data
- **organize** information
- **division** of work
- access information in a consistent manner
- **add layers of complexity**
- like functions, classes are a mechanism for
**decomposition and abstraction** in programming
