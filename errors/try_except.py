print('some code')
# try:
#
#     print(my_variable)
# except NameError:
#     print('some error')
# except TypeError:
#     print('Type error')
# print('Code after error')

user_dict ={
    'first_name': 'Jack',
    'last_name': 'White',
    'age': 24
}

# print(user_dict['last_name'])
# print(user_dict.get('last'))

def get_dict_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None

print(get_dict_value(user_dict, 'a'))