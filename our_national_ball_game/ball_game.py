import random


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
    def __init__(self) -> None:
        self.outs = 0
        self.runs = [0, 0]
        self.over = False
        self.top = True
        self.bottom = False
        self.bases = Bases()

    def add_outs(self, outs_to_add: int) -> None:
        self.outs += outs_to_add
        if self.outs >= 3:
            self.bases.clear()
            if self.bottom:
                self.over = True
                self.bottom = False
                self.runs = tuple(self.runs)
            if self.top:
                self.outs = 0
                self.top = False
                self.bottom = True

    def add_runs(self, runs_scored: int) -> None:
        if self.top:
            self.runs[0] += runs_scored
        elif self.bottom:
            self.runs[1] += runs_scored
        else:
            raise PermissionError("Innings that are over can't be modified")


class Bases(object):
    """The current state of the bases"""
    def __init__(self) -> None:
        self.on_first = False
        self.on_second = False
        self.on_third = False

    def clear(self) -> None:
        """clear the bases"""
        self.__init__()

    @property
    def as_tuple(self):
        return self.on_first, self.on_second, self.on_third
