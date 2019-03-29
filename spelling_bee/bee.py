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


PLAYERS = [Player(str(i), i) for i in range(90, 100)]
PLAYERS[-1].name = "me"


def run_bee(players: List[Player]) -> Player:
    eliminated_this_round = []
    rnd = 0
    while len(players) != 1:
        rnd += 1
        for player in players:
            randint = random.randint(1, 100)
            if not player.knows(randint):
                print(f"Player {player.name} eliminated in round {rnd}")
                eliminated_this_round.append(player)
        for player in eliminated_this_round:
            players.remove(player)
        if not players:
            players = eliminated_this_round[:]
        eliminated_this_round = []
    return players[0]
