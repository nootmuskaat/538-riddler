"""
Baseball events
"""

SINGLE = (
        ("score_from", 2),
        ("runners_advance", 1),
        )

DOUBLE = (
        ("score_from", 2),
        ("runners_advance", 2),
        )

TRIPLE = (
        ("score_from", 1),
        ("runners_advance", 3),
        )

HOME_RUN = (
        ("score_from", 1),
        ("runners_advance", 4),
        )

BASE_ON_ERROR = SINGLE  # The task description makes no mention of counting
                        # hits or errors

BASE_ON_BALLS = (
        ("runners_advance", 1),
        )

STRIKE = (
        ("add_strike",),
        )

FOUL_OUT = (
        ("add_out",),
        )

OUT_AT_1ST = (
        ("add_out",),
        ("score_from", 3),
        ("runners_advance", 1),
        ("clear_lowest",),
        )

FLY_OUT = (
        ("add_out",),
        ("score_from", 3),
        )

DOUBLE_PLAY = (
        ("add_out",),
        ("clear_lowest",),
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
