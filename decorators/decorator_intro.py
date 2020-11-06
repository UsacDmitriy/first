# def foo():
#     # print('Some code before')
#     print('Foo foo code')
#     # print('Some code after old code')
#
# foo()

# decorator_func = decorator_foo(foo)
# decorator_func()
# def decorator_foo(foo):
#     def wrap_foo():
#         print('Some code before')
#         foo()
#         print('Some code after old code')
#     return wrap_foo
#
# @decorator_foo
# def foo():
#     print('Foo foo code')
#
# foo()
def make_compliment(func):
    def wrapper(*args, **kwargs):
        print('Nice to meet')
        func(*args, **kwargs)
        print("You look great")
    return wrapper

@make_compliment
def ask_name():
    print('What is your name?')

ask_name()

@make_compliment
def say_name(name):
    print('My name is ' + name)


say_name('Jack')

@make_compliment
def order(foot, drink):
    print(f'give me {foot} and {drink}')

order(foot='chips', drink='cola')