# Tests for Python code

# Assertions

# assert 2 + 2 == 4

# assert 2+ 2 == 5, 'You are retard'

# def divide(a,b):
#     assert b !=0, 'b must not equal 0'
#     return a/b
#
# print(divide(2,2))
# print(divide(2,0))

# def multiply_positive_numbers(a,b):
#     assert a > 0 and b > 0, 'a and b must be positive'
#     print(a*b)
#
# multiply_positive_numbers(1,2)
# multiply_positive_numbers(1,-2)

def get_access(password):
    password_list = [111, 222, 333]
    assert int(password) in password_list, 'Password is invalid'
    print('You can make dangerous stuff')

password1 = input('Please enter password')
get_access(password1)