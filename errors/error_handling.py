# raise ValueError('You enter incorrect valid')
# raise ValueError()

def get_rainbow_color(color_number):
    '''
    :param

    '''
    color_number_list = [1,2,3,4,5,6,7]
    if type(color_number) is not int:
        raise TypeError('Color number msut be integer')
    if color_number not in color_number_list:
        raise ValueError("Color number must be be in range integer from 1 to 7")

    if color_number == 1:
        return 'red'
    elif color_number==2:
        return 'orange'
    elif color_number==3:
        return 'yellow'
    elif color_number==4:
        return 'green'
    elif color_number==5:
        return 'blue'
    elif color_number==6:
        return 'indigo'
    elif color_number==7:
        return 'violet'
help(get_rainbow_color)
color = get_rainbow_color(12)
print(color)