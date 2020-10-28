def function1():
    print('function from first.py')

print('Top level in first.py')

if __name__ == '__main__':
    print('first.py is rinning directly')
else:
    print('first.py has been imported')