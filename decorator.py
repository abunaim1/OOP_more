import math
def timer(func):
    def inner(*args, **kwargs):
        print('Time start')
        # print(func)
        func(*args, **kwargs)
        print('Time ended')
    return inner

# timer()()

@timer  #timer(get_factorial)() 
def get_factorial(n):
    print('factorial started')
    result = math.factorial(n)
    print(f'Factorial of {n} is {result}')

get_factorial(5) 

# vajailla way doing decorator
# @timer --> timer(get_factorial)() 

#what is decorator -> decorator is a nasted function. 