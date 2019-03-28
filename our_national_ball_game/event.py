"""
Baseball events
"""

SINGLE = (
        ("log", "And the hit's good for a single"),
        ("score_from", 2),
        ("runners_advance", 1),
        )

DOUBLE = (
        ("log", "And that'll be good for a double"),
        ("score_from", 2),
        ("runners_advance", 2),
        )

TRIPLE = (
        ("log", "And he turns it into a triple!"),
        ("score_from", 1),
        ("runners_advance", 3),
        )

HOME_RUN = (
        ("log", "it's going... going... gone!"),
        ("score_from", 1),
        ("runners_advance", 4),
        )

# The task description makes no mention of counting hits or errors
BASE_ON_ERROR = (
        ("log", "And that'll be an error"),
        ("score_from", 3),
        ("runners_advance", 1),
        )

BASE_ON_BALLS = (
        ("log", "And he walked him..."),
        ("runners_advance", 1),
        )

STRIKE = (
        ("log", "that'll be a strike"),
        ("add_strike",),
        )

FOUL_OUT = (
        ("log", "The catchers under it... and he's out"),
        ("add_out",),
        )

OUT_AT_1ST = (
        ("log", "And they'll throw him out at first"),
        ("add_out",),
        ("score_from", 3),
        ("runners_advance", 1),
        ("clear_lowest_runner",),
        )

FLY_OUT = (
        ("log", "The outfielder's under it. Out"),
        ("add_out",),
        ("score_from", 3),
        )

DOUBLE_PLAY = (
        ("log", "they've got him at first..."),
        ("add_out",),
        ("turn_double_play",),
        )

EVENT_TABLE = {
        (1, 1): DOUBLE,
        (1, 2): SINGLE,
        (1, 3): SINGLE,
        (1, 4): SINGLE,
        (1, 5): BASE_ON_ERROR,
        (1, 6): BASE_ON_BALLS,
        (2, 2): STRIKE,
        (2, 3): STRIKE,
        (2, 4): STRIKE,
        (2, 5): STRIKE,
        (2, 6): FOUL_OUT,
        (3, 3): OUT_AT_1ST,
        (3, 4): OUT_AT_1ST,
        (3, 5): OUT_AT_1ST,
        (3, 6): OUT_AT_1ST,
        (4, 4): FLY_OUT,
        (4, 5): FLY_OUT,
        (4, 6): FLY_OUT,
        (5, 5): DOUBLE_PLAY,
        (5, 6): TRIPLE,
        (6, 6): HOME_RUN
        }
