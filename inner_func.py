# In python function is a first class object

# inner function :

def double_dacker():
    print('Starting the double dacker')
    def inner():
        print('Inner')
        return 3000
    return inner
    
print(double_dacker()())

# take a function as parameter 

def do_something(work):
    print('Work Start')
    # print(work)
    work()
    print('Work Ended')

do_something(2)
do_something('This is naim')

def coding():
    print('Love coding')

do_something(coding)

def sleeping():
    print('Sleeping and dreaming in python')

do_something (sleeping)