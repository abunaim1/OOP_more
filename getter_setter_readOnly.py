# read only --> you can not set the value. value can not be changed. 
# getter --> get a value of a property through a method, Maximum time getting the value of a private attribute.
# setter --> set a value of a property through a method, Maximum time setting the value of a private attribute.

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money
    
    #getter without any setter is ready-only attribute 
    @property
    def age(self):
        return self._age
    
    #getter
    @property
    def salary(self):
        return self.__money
    
    # getter must then setter
    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'Money can not be neg.' 
        self.__money += value


user1 = User('Naim', 22, 4000)
print(user1.salary) # not using method though salary is being used as a method avobe. 

user1.salary = 1000
print(user1.salary)

