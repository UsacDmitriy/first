# x = input("Ask me ")
#
# print('siski ' + x)

# lorem_ipsum = open('E:\\py_projects\\1.2 sample.txt.txt')
#
# for line in lorem_ipsum:
#     print(line, end='')
# lorem_ipsum.close()

#
# lorem_ipsum = open('E:\\py_projects\\1.2 sample.txt.txt')
#
# for line in lorem_ipsum:
#     if 'let' in line.lower():
#         print(line, end='')
# lorem_ipsum.close()

# with open('E:\\py_projects\\1.2 sample.txt.txt') as lorem:
#     for line in lorem:
#         if 'let' in line.lower():
#             print(line, end='')


# with open('E:\\py_projects\\1.2 sample.txt.txt') as lorem:
#     lines = lorem.readlines()
#
# for i in lines[::-1]:
#     print(i)

with open('E:\\py_projects\\1.2 sample.txt.txt') as lorem:
    text = lorem.read()

print(text)