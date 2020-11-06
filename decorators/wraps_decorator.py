from functools import wraps

def print_function_data(function):
    """
    This is decorator function

    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'You are using {function.__name__}')
        print(f'Function documentation: {function.__doc__}')
        return function(*args, **kwargs)
    return wrapper

@print_function_data
def squares_sum(a, b):
    """
    :param a:
    :param b:
    :return: sum of
    """
    return a*a + b*b

print(squares_sum(2,6))
help(squares_sum)