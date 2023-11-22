# In python function is a first class object
def double_dacker():
    print('Starting the double dacker')
    def inner():
        print('Inner')
        return 3000
    return inner
    
print(double_dacker()())