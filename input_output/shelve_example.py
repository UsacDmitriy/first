import  shelve

cars = shelve.open('shelve_test1')
cars['opel'] = 'Germany'
cars['ford'] = 'USA'
cars['mazda'] = 'Japan'
cars['renault'] = 'France'
print(cars['ford'])
print(cars['renault'])
print(cars['opel'])

print(cars)
print(type(cars))
cars.close()


# with shelve.open('shelve_test') as cars:
    # cars['opel'] = 'Germany'
    # cars['ford'] = 'USA'
    # cars['mazda'] = 'Japan'
    # cars['renault'] = 'France'

    # print(cars['ford'])
    # print(cars['renault'])
    # print(cars['opel'])
    # print(cars.get('ope'))
    # #
    # # del cars['ope']
    #
    # cars['kia'] = 'South Korea'
    # #
    # # for key in cars:
    # #     print(key)
    #
    # for car in cars:
    #     print(car + ': ' + cars[car] )

    # while True:
    #     key = input('please enter car name ')
    #     if key == 'quit':
    #         break
    #     country = cars.get(key, "We do not have a " + key)
    #     print(country)

    # while True:
    #     key = input('please enter car name ')
    #     if key == 'quit':
    #         break
    #     if key in cars:
    #         country = cars[key]
    #         print(country)
    #     else:
    #         print('We do not have a ' + key)
    # ordered_keys_list = list(cars.keys())
    # ordered_keys_list.sort()
    # for key in ordered_keys_list:
    #     print(key + ': ' + cars[key])

    # for value in cars.values():
    #     print(value)
    #
    # for key in cars.keys():
    #     print(key)
    #
    # for item in cars.items():
    #     print(item)