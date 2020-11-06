import shelve

university = shelve.open('university_file')

university['schedules'] = {
    'monday_schedule': ['Math', 'English', 'System programmning', 'Python'],
    'tuesday_schedule': ['English', 'HTML', 'Python', 'Football'],
    'wednesday_schedule': ['Physics', 'English', 'Python'],
    'thursday_schedule': ['Math', 'Chemistry', 'Java'],
    'friday_schedule': ['Running', 'Math', 'Python'],
}

university['tutors'] = {
    'Math': ['Jack White', 'Jim Black'],
    'Python': ['Youra Alla', 'Jane Smith']
}
print(university['schedules']['wednesday_schedule'])
print(university['tutors']['Math'])

x = university['schedules']

print(type(x))



# university = {
#     'schedules': {
#         'monday_schedule': ['Math', 'English', 'System programmning', 'Python'],
#         'tuesday_schedule': ['English', 'HTML', 'Python', 'Football'],
#         'wednesday_schedule': ['Physics', 'English',  'Python'],
#         'thursday_schedule': ['Math', 'Chemistry', 'Java'],
#         'friday_schedule': ['Running', 'Math', 'Python'],
#     },
#     'tutors': {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['Youra Alla', 'Jane Smith']
#     }
# }
#
# print(university['schedules']['wednesday_schedule'])
# print(university['tutors']['Math'])

