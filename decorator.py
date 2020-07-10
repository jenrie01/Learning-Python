# Higher Order Function
# def greet(func):
#     func()

# def greet2():
#     def func():
#         return 5
#     return func

# Decorator Pattern
from time import time


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('****************')
        func(*args, **kwargs)
        print('****************')
    return wrap_func

# @my_decorator
# def hello():
#     print('hellllllllooooooo')

# @my_decorator
# def bye():
#     print('Seee yaaaa laterrr')

# hello()
# bye()


@my_decorator
def hello(greeting, emoji='😃'):
    print(greeting, emoji)


# hello('hallo', '😃')
hello('hallo')


def performance(func):
    def wrapper(*args, **kwargs):
        time1 = time()
        result = func(*args, **kwargs)
        time2 = time()
        print(f'start:{time1} end:{time2} took{time2-time1}')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*5


long_time()
