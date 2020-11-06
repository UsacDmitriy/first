# Higher order functions, which accept another functions as arguments

# def product(n, func):
#     result = 1
#     for number in range(1, n):
#         result *= func(number)
#     return result
#
# def square(x):
#     return x*x
#
# def cube(x):
#     return x*x*x

# print(product(4, square))
# print(product(4, cube))
#
# def my_func(a, b, foo):
#     return foo([a, b])
#
# print(my_func(1, 2, sum))

from random import choice

# def colorize(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#
#     return get_color() + ' ' + thing


# def make_color():
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#     return get_color
#
#
# my_color = make_color()
# print(my_color())
#
# for i in range(10):
#     print(my_color())

def make_color():
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color + ' '
    return get_color

def colorize(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color + ' ' + thing

    return get_color

print(colorize('apple')())