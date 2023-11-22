class Person:
    def __init__(self, name,age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def eat(self):
        print('Mangsho polaw khabo')
    
    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # > sign operator overload
    def __gt__(self, other):
        return self.age > other.age
    
    # * sign operator overload
    def __mul__(self, other):
        return self.height * other.height
    
    # + sign operator overload
    def __add__(self, other):
        return self.weight + other.weight
    
    #override
    def eat(self):
        print('Vagitable')
    
    def exercise(self):
        print('Gym a poisha hudai gham jhorai')

sakib = Cricketer('Sakib Al Hasan', 33, 38, 66, 'BD')
mushi = Cricketer('Mushfiqur Rahim', 30, 22, 44, 'BD')

# sakib.eat()
# sakib.exercise()

print(sakib > mushi)
print(sakib * mushi)
print(sakib + mushi)