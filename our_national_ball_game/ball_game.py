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
