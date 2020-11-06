#Iterate

number_list = [1,2,3,4,5]

# for num in number_list:
#     print(num)

#Iterators

number_list_iterator = iter(number_list)
print(type(number_list_iterator))
#
#
# # print(number_list_iterator.__next__())
# # print(number_list_iterator.__next__())
# # print(number_list_iterator.__next__())
#
#
# print(next(number_list_iterator))
# print(next(number_list_iterator))


def my__for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print("Print is finished")
            break




my__for_loop("siski")