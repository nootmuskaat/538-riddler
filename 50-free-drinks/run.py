import random


def iteration() -> int:
    """Simulate randomly spending with one of two cards loaded with 50
    free drinks"""
    cards = [50, 50]
    while True:
        idx = random.randint(0, 1)
        if not cards[idx]:
            return cards[0 if idx == 1 else 1]
        cards[idx] -= 1


def main() -> None:
    """Run 100,000 iterations and print results"""
    runs = []
    iterations = 100000
    for _ in range(iterations):
        runs.append(iteration())
    where_remaining = [run for run in runs if run]
    percent_remaining = len(where_remaining) / iterations
    average_overall = sum(runs) / iterations
    average_where_remaining = sum(where_remaining) / len(where_remaining)
    print(f"The other card hard drinks on it {percent_remaining:.04}% of the time")
    print(f"Overall {average_overall:.04} drinks remained")
    print(f"{average_where_remaining:.04} if we only consider times when something was left")


if __name__ == "__main__":
    main()
