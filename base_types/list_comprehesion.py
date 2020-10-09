greeting = 'Hello'
# leeter_list = []
# for i in greeting:
#     leeter_list.append(i)

# print(leeter_list)

# leeter_list = [ letter for letter in greeting]
# print(leeter_list)
# num_list = [ i for i in '010010192220']
# print(num_list)
# num_list1 = [ i for i in range(0,10)]
# print(num_list1)
# num_list2 = [ i**2 for i in range(0,10)]
# print(num_list2)
# num_list3 = [ (i-3)/2**2 for i in range(0,10)]
# print(num_list3)
# num_list = [ 1,23,98,34,2,-2,4, -23]
# new_list = [ i for i in num_list if i > 0]
# print(new_list)
# new_list_1 = [ '+' if i>0 else '-' for i in num_list]
# print(new_list_1)
#Dictionary
number_dic = {'first':1,'second':2,'third':3}
new_dic = {key:value**3 for key, value in number_dic.items()}
print(new_dic)

num_list = [ 1,23,98,34,2,-2,4, -23, 0]
number_dic = {number:number**2 for number in num_list}
print(number_dic)
number_dic1 = {number:'positive' if number >0 else 'negative' if number <0 else 'zero'  for number in num_list}
print(number_dic1)