def double(func):
    def wrapper(x):
        return func(x) *2
    return wrapper
@double 
def my_func(x):
    return x**2

print(my_func(2))
