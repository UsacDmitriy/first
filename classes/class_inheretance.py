# Inheretance

class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crahed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crahed
        print('car is created')

    def drive(self, city):
        print(self.name + " is driving to " + city)

    def change_color(self, new_color):
        self.color = new_color
        print('Color is changed to ' + new_color)


class Truck(Car):
    wheels_number = 6

    def __init__(self, name, color, year, is_crahed):
        Car.__init__(self, name, color, year, is_crahed)
        print('truck is created')

    def drive(self, city):
        print('truck ' + self.name + " is driving to " + city)

    def load_cargo(self, weight):
        print(f'the cargo is loaded. Weight is {weight}')


man_truck = Truck('man', 'white', 2015, False)

man_truck.change_color('green')
man_truck.drive('new your')

print(man_truck.wheels_number)
man_truck.load_cargo(1000)


# Polymotphism

class Animal:
    def __init__(self, name):
        self.name = name

    def speake(self):
        raise NotImplementedError('Class succecor must implemet this method')


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speake(self):
        print(self.name + ' is saying woof')


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speake(self):
        print(self.name + ' is saying meow')


class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def speake(self):
        print(self.name + ' is saying nothing')

fredy = Fish("freddy")
spike = Dog('Spike')
tom = Cat('Tom')

pet_list = [spike, tom, fredy]

for pet in pet_list:
    pet.speake()


def pet_voice(pet):
    pet.speake()


pet_voice(spike)


pet_voice(fredy)
