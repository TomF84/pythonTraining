## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self, name):
        ## An animal is created with a name
        self.name = name
    #pass
    
## A dog is created, it has functions to bark and to print it's name
class Dog(Animal):

    def __init__(self, name):
        ## A dog is created with a name, inherited from parent
        super(Dog, self).__init__(name)
    
    def printName(self):
        print('This is a dog with the name', self.name)
        
    def bark(self):
        print(self.name+':', 'Woof!Woof!')

## ??
class Cat(Animal):

    def __init__(self, name):
        ## Here we define the name of the Fish to be the name argument
        self.name = name
        
## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        # The super function looks at the parent class and inherits the function from it.
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary
        
## ??
class Fish(Animal):

    def __init__(self, name, fins = 2):
        ## A fish is created with a name, inherited from parent, also the number of fins is set, default 2
        super(Fish, self).__init__(name)
        self.fins = fins


## ??    
class Salmon(Fish):

    def __init__(self, name, color = 'pink'):
        ## A fish is created with a name, inherited from parent, also the number of fins is set, default 2
        super(Fish, self).__init__(name)
        self.color = color
    
    pass

## ??    
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish('Flipper')

## ??
crouse = Salmon('Crouse', color = 'red')

## ??
harry = Halibut('Harry')

for x in [rover,satan,mary,frank,flipper,crouse,harry]:
    print(x.name,':\n',help(x))
    
rover.bark()
