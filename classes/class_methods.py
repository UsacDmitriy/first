class Gamer:

    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        print(cls)
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def get_nickname(self):
        return self.nickname

    def logout(self):
        Gamer.active_gamers -= 1

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_permission(self):
        if self.is_adult():
            print("You can play game")
        else:
            print("You can't play game")

# print(Gamer.active_gamers)
# gamer_1 = Gamer('hell_boy', 23, 5, 13)
# print(Gamer.active_gamers)
# gamer_2 = Gamer('harry_potter', 13, 7, 34)
# print(Gamer.active_gamers)
# print(gamer_1.get_age())
# print(gamer_1.get_adult_permission())
#
# print(gamer_2.get_age())
# print(gamer_2.get_adult_permission())
#
# print(Gamer.active_gamers)
#
# print(Gamer.get_active_gamers())


name = Gamer.gamer_from_string('name, 12, 13, 12')
print(name.get_level())
my_dict = dict.fromkeys((1,2,3,4), ('apple', 'orange', 'banan', 'pieapple'))
print(my_dict)