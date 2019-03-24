import unittest


class DiceRollTest(unittest.TestCase):
    def test_within_range(self):
        from ball_game import Die
        for _ in range(100):
            roll = Die.roll_multiple(2)
            self.assertLessEqual(roll[0], roll[1])
            self.assertGreaterEqual(roll[0], 1)
            self.assertLessEqual(roll[1], 6)


class InningTest(unittest.TestCase):
    def test_begins_at_top(self):
        from ball_game import Inning
        new_inning = Inning()
        self.assertTrue(new_inning.top)
        self.assertFalse(new_inning.bottom)

    def test_change_after_three_outs(self):
        from ball_game import Inning
        inning = Inning()
        inning.add_runs(1)  # 1 - 0
        inning.add_outs(2)
        inning.add_runs(3)  # 4 - 0
        self.assertTrue(inning.top)
        inning.add_outs(2)
        self.assertFalse(inning.top)
        self.assertTrue(inning.bottom)
        self.assertEqual(inning.outs, 0)
        inning.add_runs(2)  # 4 -2
        inning.add_outs(3)
        self.assertTrue(inning.over)
        self.assertEqual(inning.runs, (4, 2))


class BasesTest(unittest.TestCase):
    def test_clear_the_bases(self):
        from ball_game import Bases
        status = Bases()
        status.on_first = True
        status.on_second = True
        self.assertFalse(status.on_third)
        status.clear()
        self.assertFalse(status.on_second)
        self.assertFalse(status.on_first)


if __name__ == "__main__":
    unittest.main()
