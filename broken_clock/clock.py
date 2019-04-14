class Time(object):
    def __init__(self, hour: int, minute: int) -> None:
        self.hour = hour
        self.minute = minute
        self.hour_hand_angle = (hour * 30) + (minute // 12)
        self.minute_hand_angle = minute * 6

    def __str__(self) -> str:
        hour = 12 if self.hour == 0 else self.hour
        return f"{hour}:{self.minute:02}"

    def looks_like(self, other) -> bool:
        return self.minute_hand_angle == other.hour_hand_angle and \
                self.hour_hand_angle == other.minute_hand_angle



def main() -> None:
    times = []
    for hour in range(12):
        for minute in range(60):
            times.append(Time(hour, minute))
    for idx, time in enumerate(times):
        for other_time in times[idx+1:]:
            if time.looks_like(other_time):
                print(f"{time} looks like {other_time}")


if __name__ == "__main__":
    main()
