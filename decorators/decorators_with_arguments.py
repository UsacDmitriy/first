from functools import wraps
#
# def check_if_first_arg_is(value):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != value:
#                 print(f'first argument has to be {value}')
#             return func(*args, **kwargs)
#         return wrapper
#     return inner_dec
#
# @check_if_first_arg_is(7)
# def multiply_seven(a,b):
#     return a*b

# print_rainbow_colors('green', 'red','orange', 'yellow', 'blue')
#
# print(multiply_seven(7,3))
# print(multiply_seven(3,4))

def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for arg, t in zip(args, types):
                new_args.append(t(arg))
            return func(*new_args)
        return wrapper
    return inner_dec

@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)

@enforce(int, int)
def divide(a,b):
    return a/b


print(divide(4,5))
print(divide('4','5'))


print_text_n_times('Dima', "5")

# *args - ('Dima', '3')
# *types - ( str, int)
# zip(args, types) - ('Dima', str), ('3', int)
