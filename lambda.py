# # def sum_of_two_numbers(x):
# #     return x+x

# # number_list = [1,2,2,23,3,3,3,3,33,2,4,44,5,4,4]

# # map_result = map(sum_of_two_numbers, number_list)
# # print(map_result)
# # new_list = []
# # for item in map_result:
    
# #     new_list.append(item)

# # print(new_list)

# # def is_a_in_string(string):
# #     if 'a' in string:
# #         print('a in string')
# #         return True
# #     else:
# #         print('a is not in string')
# #         return False

# # string_list = ['11qaq', 'asdeded','eveve','cwcw']

# # print(list(map(is_a_in_string, string_list)))

# def is_number_odd(number):
#     return number % 2 == 0
# number_list = [1,2,2,23,3,3,3,3,33,2,4,44,5,4,4]
# print(list(filter(is_number_odd, number_list)))

# def is_a_in_string(string):
#     if 'a' in string:
#         # print('a in string')
#         return True
#     else:
#         # print('a is not in string')
#         return False

# string_list = ['11qaq', 'asdeded','eveve','cwcw']

# print(list(filter(is_a_in_string, string_list)))

# Lambda expression

# def cube(number): 
#     return number ** 3

number_list = [1,2,2,23,3,3,3,3,33,2,4,44,5,4,4]  

print(list(map(lambda number:number**3, number_list)))

print(list(filter(lambda number:number % 2 == 0, number_list)))