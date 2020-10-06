# print(list(range(1,123,3)))
# for i in range(1,123,3):
#     print(i)

my_string = 'abfgsde'
for key, letter in enumerate(my_string):
    print(str(letter) + "  " + str(key)) 

from random import randint

print(randint(12,123))