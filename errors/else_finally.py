# number = input('enter some number ')
# # print(int(number/2))
#
# try:
#     print(int(number)/2)
# except:
#     print('You have to enter number')
# else:
#     print('Else block')
# finally:
#     print('I am always here')

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("You can not divide by zero")
    except TypeError:
        print('You can divide ')
    else:
        print("Hallo Hallo")
    finally:
        print('Hello')


print(divide(4, 'll'))
