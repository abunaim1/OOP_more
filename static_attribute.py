# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# differences between static method and class method

class Shopping:
    cart = [] # class attirubte /  Static Attribute
    origin = 'China'

    def __init__(self, name, location) -> None:
        self.name = 'Jamuna Future PArk' #instance attribute
        self.locaation = 'Jam r moddhe'
    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying {item}, prics {price}, extra {remaining}')
    
    @staticmethod 
    def multiply(a,b):
        print(a*b)

    @classmethod
    def sell_product(self, product):
        print(f'becha kina nai bollei chole tobe {product} bhalo sell hoi')
    

bashundhara = Shopping('Bashundhara Shopping Mall', 'Rajarbag')
bashundhara.purchase('Lungi', 500, 1000)

# class method
Shopping.sell_product('lungi')

# Static Method
Shopping.multiply(6, 9) 