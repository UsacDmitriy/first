import pickle

# honda = (
#     'civic',
#     'grey',
#     2009,
#     (
#         (1, 'James Brown'),
#         (2, 'Jane White'),
#         (3, 'Jack Green')
#     )
# )
#
# with open('honda.picle', 'wb') as honda_file:
#     pickle.dump(honda, honda_file)

# with open('honda.picle', 'rb') as honda_file:
#     honda = pickle.load(honda_file)
#
# print(honda)
# model, color, year, owners = honda
# print(model)
# print(color)
# print(year)
# print(owners)


honda = (
    'civic',
    'grey',
    2009,
    (
        (1, 'James Brown'),
        (2, 'Jane White'),
        (3, 'Jack Green')
    )
)

models = ['civic', 'accord', 'pilot']
owners = ['James Brown', 'Jane White', 'Jack Green']

with open('honda.picle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)
    pickle.dump(models, honda_file)
    pickle.dump(owners, honda_file)
    pickle.dump(909009, honda_file)

with open('honda.picle', 'rb') as honda_file:
    honda = pickle.load(honda_file)
    models = pickle.load(honda_file)


print(honda)
print(models)