# Method resolution order

#   A
#  / \
# B   C
#  \ /
#   D


class A:
    def som_method(self):
        print('Method of class A')


class B(A):
    pass
    # def som_method(self):
    #     print('Method of class B')


class C(A):
    @classmethod
    def som_method(cls):
        print('Method of class C')


class D(B, C):
    pass
    # def som_method(self):
    #     print('Method of class D')

# __mro__, mro(), help()


# print(D.__mro__)

print(D.mro())
help(D)

some_object = D()
some_object.som_method()
