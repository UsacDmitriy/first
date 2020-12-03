from collections import Counter

number_list = [1, 2, 3, 1, 2, 3, 3, 2, 1, 2]

print(Counter(number_list))


string = 'cja;cas;dvna;sbdacsjajshblajkbxchvakjvxc'

print(Counter(string))

senteces = 'Hello how are you doing? Hello I am fine. How do you do? Hey Hey Hey'

c = Counter(senteces.split(' '))

print(sum(c.values()))