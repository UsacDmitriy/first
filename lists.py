# list = [1, 2,'hello', True]
# print(list)
# print(len(list))

# first_list = [1,2,3,'hello', 'mail', True]
# second_list = ['igor','rak']
# new_list = first_list+second_list
# print(new_list)
# #adding items in list
# new_list.append('kukold')
# new_list.insert(1, 'igor kukold')
# new_list.insert(0, 'igor kukold')
# print(new_list)

# #removing items
# new_list.pop()
# new_list.pop(0)

# name = new_list.pop(3)
# print(new_list)
# print(name)

# new_list.remove(1)
# print(new_list)

number_list =[1,2,3,4,5,6]
letter_list= ['s','w','v','r']

number_list.sort()
letter_list.sort()
new_list = letter_list
letter_list.reverse()


print(number_list)
print(id(letter_list))
print(id(new_list))

