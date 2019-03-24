import unittest


class DiceRollTest(unittest.TestCase):
    def test_within_range(self):
        from ball_game import Die
        for _ in range(100):
            roll = Die.roll_multiple(2)
            self.assertLessEqual(roll[0], roll[1])
            self.assertGreaterEqual(roll[0], 1)
            self.assertLessEqual(roll[1], 6)


if __name__ == "__main__":
    unittest.main()
