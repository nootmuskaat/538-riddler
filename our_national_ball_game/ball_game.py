import logging as log
import random
import sys
from typing import Any, List, Tuple

import event


class Die(int):
    lowest = 1
    highest = 6

    def __init__(self, value: int) -> None:
        if not self.lowest <= value <= self.highest:
            raise ValueError(f"Provided value {value} outside of bounds: "
                             f"[{self.lowest},{self.highest}]")
        super().__init__()

    @classmethod
    def roll(cls):
        rolled = random.randint(cls.lowest, cls.highest)
        return cls(rolled)

    @classmethod
    def roll_multiple(cls, number_of_dice: int):
        rolled = []
        for _ in range(number_of_dice):
            rolled.append(cls.roll())
        return tuple(sorted(rolled))


class Inning(object):
    total_strikes = 3
    total_outs = 3

    def __init__(self) -> None:
        self.outs = 0
        self.strikes = 0
        self.runs = [0, 0]
        self.over = False
        self.top = True
        self.bottom = False
        self.bases = Bases()

    def status(self) -> str:
        return f"{self.runs} | {self.strikes} strikes, {self.outs} outs, {self.bases}"

    @staticmethod
    def log(text: str) -> None:
        log.info(text)

    def new_batter(self) -> None:
        self.strikes = 0

    def new_half_inning(self) -> None:
        self.log("That takes us to the bottom of the inning")
        self.new_batter()
        self.outs = 0

    def add_strike(self) -> bool:
        self.strikes += 1
        if self.strikes == self.total_strikes:
            return self.add_out()
        return False

    def add_out(self) -> bool:
        """
        Increment the out counter
        Returns:
            True if the out is the last out of the half inning
        """
        self.outs += 1
        self.new_batter()
        if self.outs == self.total_outs:
            self.bases.clear()
            if self.bottom:
                self.over = True
                self.bottom = False
                self.runs = tuple(self.runs)
            if self.top:
                self.new_half_inning()
                self.top = False
                self.bottom = True
            return True
        return False

    def add_runs(self, runs_scored: int) -> None:
        if runs_scored:
            self.log(f"And {runs_scored} runs score!")
        if self.top:
            self.runs[0] += runs_scored
        elif self.bottom:
            self.runs[1] += runs_scored

    def score_from(self, base: int) -> None:
        runs = self.bases.score_from(base)
        self.add_runs(runs)
        self.new_batter()

    def runners_advance(self, number_of_bases: int) -> None:
        runs = self.bases.runners_advance(number_of_bases)
        self.add_runs(runs)
        self.new_batter()

    def clear_lowest_runner(self) -> None:
        self.bases.clear_lowest_runner()

    def turn_double_play(self) -> None:
        if self.bases.clear_lowest_runner():
            self.log("And they turned the double play!")
            self.add_out()


class Bases(object):
    """The current state of the bases"""
    def __init__(self) -> None:
        self.on_first = False
        self.on_second = False
        self.on_third = False

    def __str__(self):
        if all(self.as_tuple):
            return "Bases loaded"
        elif not any(self.as_tuple):
            return "Bases empty"
        occupied = []
        if self.on_first:
            occupied.append("first")
        if self.on_second:
            occupied.append("second")
        if self.on_third:
            occupied.append("third")
        if len(occupied) == 1:
            return f"Runner on {occupied[0]}"
        else:
            return f"Runners on {occupied[0]} and {occupied[1]}"

    def clear(self) -> None:
        """clear the bases"""
        self.__init__()

    @property
    def as_tuple(self):
        return self.on_first, self.on_second, self.on_third

    @classmethod
    def from_tuple(cls, on_first, on_second, on_third):
        """Useful classmethod for testing"""
        self = cls()
        self.on_first = on_first
        self.on_second = on_second
        self.on_third = on_third
        return self

    def score_from(self, base: int) -> int:
        """
        Base from which any runners might score
        Args:
            base: 1 == score from first, etc
        Returns:
            number of runs scored
        """
        runs = 0
        if base <= 3 and self.on_third:
            runs += 1
            self.on_third = False
        if base <= 2 and self.on_second:
            runs += 1
            self.on_second = False
        if base <= 1 and self.on_first:
            runs += 1
            self.on_first = False
        return runs

    def runners_advance(self, number_of_bases: int) -> int:
        """
        Advance runners along the bases
        Args:
            number_of_bases: how many bases they advance
        Returns:
            runs scored: this will be 0 unless a player walks with bases loaded
                    or a home run is hit
        """
        def runner_moves(x, y):
            return x and y, x or y

        def and_tuples(x, y):
            return tuple([a and b for a, b in zip(x, y)])

        if number_of_bases not in range(1, 5):
            raise ValueError(f"Runners can advance between 1 and 4 bases only")

        forced = True
        scored = 0
        bases_to_clear = number_of_bases - 1
        while number_of_bases:
            forced, self.on_first = runner_moves(forced, self.on_first)
            forced, self.on_second = runner_moves(forced, self.on_second)
            forced, self.on_third = runner_moves(forced, self.on_third)
            if forced:
                scored += 1
            forced = True
            number_of_bases -= 1
        current = self.as_tuple
        to_leave = ([False] * bases_to_clear + [True] * 3)[:3]
        new_state = and_tuples(current, to_leave)
        self.on_first, self.on_second, self.on_third = new_state
        return scored

    def clear_lowest_runner(self) -> bool:
        if not any(self.as_tuple):
            return False
        if self.on_first:
            self.on_first = False
        elif self.on_second:
            self.on_second = False
        else:
            self.on_third = False
        return True
