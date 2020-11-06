from functools import wraps

def prohibit_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('keywords arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper

def prohibit_int_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for val in args:
            if type(val) == int:
                raise ValueError('integer arguments are prohibited')
        for key, val in kwargs.items():
            if type(val) == int:
                raise ValueError('integer arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper

@prohibit_int_arguments
def print_hello(name):
    print((f'Hello {name}'))

# print_hello(name = 'Jack')
print_hello(3)