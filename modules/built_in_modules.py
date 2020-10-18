# import random
#
# x = random.randint(1,10)
# for i in range (10):
#     print(random.randint(1,10))

from random import randint

x = randint(1,20)
print(x)

from random import shuffle as sh

list = [1,2,3,5,6,3]
sh(list)
print(list)