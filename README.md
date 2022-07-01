# Python Classes and Inheritance

## Getter and Setter Methods
Here are we trying to group different objects part of the same type, in this case we're grouping animals. We begin with creating an animal class:

```
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None 

myanimal = Animal(3)
```

Notice `self.name = None` is a data attribute even though an instance is not initialized with it as a parameter. `self` variable refers to the newly created instance `myanimal` while `(3)` is mapped to `self.age` in class definition. 

A complete visualization of the process can be found here: [detailed visualization of class `Animal`](https://pythontutor.com/render.html#code=class%20Animal%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20age%29%3A%0A%20%20%20%20%20%20%20%20self.age%20%3D%20age%0A%20%20%20%20%20%20%20%20self.name%20%3D%20None%20%0A%0Amyanimal%20%3D%20Animal%283%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)



