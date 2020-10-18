# Special methods


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'I\'m {self.first_name}, my last name is {self.last_name}, my age is {self.age}'

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.age + other.age

    def __del__(self):
        print('Igor gay')


jack = Person('Jack', 'White', 23)

# print(len([1, 1, 1, 2, 2, 23]))
#
# print(jack)
# print(len(jack))
# # del jack

jane = Person('jane', 'air', 23)
print(jack + jane)


