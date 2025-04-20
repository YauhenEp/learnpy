def new_func():
    x = 10
    return x

def func(a, b, c = 10):
    return a + b + c

print(func(5, 9, 12))

def numeric_func(*args):
    return sum(args)

print(numeric_func(5, 9, 12, 234, 34,34,42))

def numeric_func1(a = 100, b = 10):
    return a + b

print(numeric_func1(b = 5))

def numeric_func2(**kwargs):
    print(kwargs)
    return kwargs

print(numeric_func2(b = 5))

a = lambda x: x + 1
print(a(5))

def func_decorator(func):
    def wrapper():
        print('Pre')
        func()
        print('Post')
    return wrapper

@func_decorator
def func():
    print('Function')

func()