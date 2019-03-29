class Player(object):
    def __init__(self, name: str, percent_known: int) -> None:
        self.name = name
        self.percent_known = percent_known

    def knows(self, number: int) -> bool:
        return number > self.percent_known


PLAYERS = [Player(str(i), i) for i in range(90, 100)]
PLAYERS[-1].name = "me"
