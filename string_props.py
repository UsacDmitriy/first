# Immutable
first_name = 'Jake'
print(first_name[1])
# first_name[2] = 'b'

first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1:]
print(last_letter)

#Concatenble
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)

print(new_first_name.upper())
print(new_first_name.lower())

long_string = 'This is a long string'
print(long_string.split(';'))