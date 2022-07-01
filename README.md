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

