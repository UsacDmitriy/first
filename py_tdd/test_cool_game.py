import unittest
import cool_game

class CoolGameFunctionsTest(unittest.TestCase):
    def test_greet(self):
        """
        greet()have to return How are you
        """
        self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack! How are you?')

    def test_greet_enemy(self):
        self.assertEqual(cool_game.greet('Ivan', True), 'Hello Ivan! I will kill you, bastard')

    def test_greet_enemy_boolean(self):
        with self.assertRaises(ValueError):
            cool_game.greet('Ivan', 'Bla-bla')

    def test_eat_burgers(self):
        self.assertEqual(cool_game.eat_burgers(3), ' Mmm! That was excellent!')

    def test_eat_burgers_too_much(self):
        self.assertEqual(cool_game.eat_burgers(4), ' Oh! I am overate!')

    def test_can_fly_batman(self):
        self.assertTrue(cool_game.can_fly('Batman'), 'Batman has to be able to fly')

    def test_can_fly_anyone(self):
        self.assertEqual(cool_game.can_fly('Bob'), False)
        self.assertEqual(cool_game.can_fly('Kevin'), False)
        self.assertEqual(cool_game.can_fly('Jim'), False)
        # self.assertFalse(cool_game.can_fly('Bob'), 'Anyone has to not be able to fly')
        # self.assertFalse(cool_game.can_fly('Kevin'), 'Anyone has to not be able to fly')
        # self.assertFalse(cool_game.can_fly('Jim'), 'Anyone has to not be able to fly')


    def test_get_arsenal(self):
        self.assertIn(cool_game.get_arsenal(), ('knife', 'handgun', 'machine gun'))

if __name__ == "__main__":
    unittest.main()