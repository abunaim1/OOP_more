class Shopping:
    cart = [] # class attirubte /  Static Attribute
    origin = 'China'

    def __init__(self, name, location) -> None:
        self.name = 'Jamuna Future PArk' #instance attribute
        self.locaation = 'Jam r moddhe'
    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying {item}, prics {price}, extra {remaining}')
    
    @classmethod
    def sell_product(self, product):
        print(f'becha kina nai bollei chole tobe {product} bhalo sell hoi')
    

bashundhara = Shopping('Bashundhara Shopping Mall', 'Rajarbag')
bashundhara.purchase('Lungi', 500, 1000)

Shopping.sell_product('lungi')