rainbow_colors= {'blue','yellow','orange','green','indigo','violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set =set()
print(empty_set)
print(type(empty_set))

number_list = [1,43,56]
text_tuple = ('sdfs','aas','edv')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)
print(set_from_list)
print(set_from_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')

print(set_from_list)
print(set_from_tuple)