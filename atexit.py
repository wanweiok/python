import atexit

def atexit_func_1():
    print("This is atexit func 1")

def atexit_func_2(name, age):
    print("This is atexit func 2, %s is %d" % (name, age))

atexit.register(atexit_func_1)
atexit.register(atexit_func_2, 'tom', 20)
print("Program finished")

@atexit.register
def atexit_func_3():
    print("This is atexit func 3")

# result: be care of the sequence
# Program finished
# This is atexit func 3
# This is atexit func 2, tom is 20
# This is atexit func 1