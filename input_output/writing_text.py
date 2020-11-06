color_list = ['blue', 'red', 'yellow', 'green', 'indigo', 'green','violet']

with open('E:\\py_projects\\rainbow_1.txt', 'w') as rainbow:
    for color in color_list:
        print(color, file=rainbow)

color_list =[]

with open('E:\\py_projects\\rainbow_1.txt', 'r') as rainbow:
    for color in rainbow:
        color_list.append(color.strip('\n'))
print(color_list)

with open('E:\\py_projects\\rainbow_1.txt', 'a') as rainbow:
    print('easy mid', file=rainbow)