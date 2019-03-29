import random
from typing import List


class Player(object):
    def __init__(self, name: str, percent_known: int) -> None:
        self.name = name
        self.percent_known = percent_known

    def __hash__(self) -> int:
        return hash(f"{type(self)}|{self.name}|{self.percent_known}")

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def knows(self, number: int) -> bool:
        return number <= self.percent_known


def run_bee(players: List[Player]) -> Player:
    eliminated_this_round = []
    rnd = 0
    while len(players) != 1:
        rnd += 1
        for player in players:
            randint = random.randint(1, 100)
            if not player.knows(randint):
                eliminated_this_round.append(player)
        for player in eliminated_this_round:
            players.remove(player)
        if not players:
            players = eliminated_this_round[:]
        eliminated_this_round = []
    return players[0]


def main() -> None:
    """Run simulation"""
    me = Player("me", 99)
    players = [Player(str(i), i) for i in range(90, 99)] + [me]
    iterations = 100000

    # run ascending
    print("Running ascending")
    won = []
    for _ in range(iterations):
        won.append(run_bee(players[:]))
    print(f"{len([w for w in won if w == me])}  / {iterations}")

    # run descending
    print("Running descending")
    won = []
    for _ in range(iterations):
        won.append(run_bee(players[::-1]))
    print(f"{len([w for w in won if w == me])}  / {iterations}")


if __name__ == "__main__":
    main()
