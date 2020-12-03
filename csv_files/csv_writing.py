import csv

# with open('students.csv', 'w') as file:
#     writer_csv = csv.writer(file)
#     writer_csv.writerow(['First name', 'Last name', 'age'])
#     writer_csv.writerow(['Jack', 'White', '20'])
#     writer_csv.writerow(['Jane', 'Black', '22'])

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     make_model_list = []
#
#     for car in csv_reader:
#         make_model = [car[1], car[2]]
#         make_model_list.append(make_model)
#     print(make_model_list)
#
# with open('cars_make_model.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     for row in make_model_list:
#         csv_writer.writerow(row)

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     # make_model_list = []
#
#     with open('cars_make_model.csv', 'w') as file:
#         csv_writer = csv.writer(file)
#         for row in csv_reader:
#             csv_writer.writerow([row[1], row[2]])

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     # make_model_list = []
#
#     with open('cars_make_model.csv', 'w') as file:
#         csv_writer = csv.writer(file)
#         for row in csv_reader:
#             csv_writer.writerow([row[1], row[2]])

# with open('students1.csv', 'w') as file:
#     headers_list = ['First name', 'Last name', 'age']
#     writer_csv = csv.DictWriter(file, fieldnames=headers_list, delimiter=";")
#     writer_csv.writeheader()
#     writer_csv.writerow({
#          'First name': 'Jack',
#          'Last name': 'White',
#          'age': '20'})
#     # writer_csv.writerow(['Jane', 'Black', '22'])

with open('cars.csv') as file:
    csv_reader = csv.DictReader(file)
    car_list = list(csv_reader)
    print(car_list)

with open('make_model.csv', 'w') as file:
    headers_list = ['Make', 'Model']
    csw_writer = csv.DictWriter(file, fieldnames=headers_list)
    csw_writer.writeheader()
    for car in car_list:
        csw_writer.writerow({
            'Make': car['Make'],
            'Model': car['Model']
        })

