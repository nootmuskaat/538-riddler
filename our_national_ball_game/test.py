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
        inning.add_runs(2)  # 4 - 2
        inning.add_outs(3)
        self.assertTrue(inning.over)
        self.assertEqual(inning.runs, (4, 2))


class BasesTest(unittest.TestCase):
    def test_clear_the_bases(self):
        from ball_game import Bases
        status = Bases.from_tuple(True, True, False)
        self.assertFalse(status.on_third)
        status.clear()
        self.assertFalse(status.on_second)
        self.assertFalse(status.on_first)

    def test_scores_from_first_on_triple(self):
        from ball_game import Bases
        bases = Bases.from_tuple(True, False, False)
        scored = bases.score_from(1)
        self.assertEqual(scored, 1)
        self.assertFalse(bases.on_first)

    def test_scores_from_second_on_double(self):
        from ball_game import Bases
        bases = Bases.from_tuple(True, True, False)
        scored = bases.score_from(2)
        self.assertEqual(scored, 1)
        self.assertFalse(bases.on_second)  # doesn't consider hitter

    def test_bases_load_all_score_on_triple(self):
        from ball_game import Bases
        bases = Bases.from_tuple(True, True, True)
        scored = bases.score_from(1)
        self.assertEqual(scored, 3)

    def test_scores_from_third_on_single(self):
        from ball_game import Bases
        bases = Bases.from_tuple(True, False, True)
        scored = bases.score_from(3)
        self.assertEqual(scored, 1)

    def test_score_on_walk_with_bases_loaded(self):
        from ball_game import Bases
        bases = Bases.from_tuple(True, True, True)
        scores = bases.runners_move(1)
        self.assertEqual(1, scores)

    def test_fill_the_bases(self):
        from ball_game import Bases
        bases = Bases.from_tuple(True, True, False)
        scores = bases.runners_move(1)
        self.assertEqual(0, scores)
        full_bases = (True, True, True)
        self.assertEqual(full_bases, bases.as_tuple)

    def test_no_advance_from_third_on_walk(self):
        from ball_game import Bases
        bases = Bases.from_tuple(False, False, True)
        scores = bases.runners_move(1)
        self.assertEqual(0, scores)
        expected = (True, False, True)
        self.assertEqual(expected, bases.as_tuple)


if __name__ == "__main__":
    unittest.main()
