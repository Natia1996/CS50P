def main():
    text = input("What time is it?: ")
    time_converted = convert(text)
    if 7 < time_converted < 8:
        print("breakfast time")
    elif 12 < time_converted < 13:
        print("lunch time")
    elif 18 < time_converted < 19:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    minutes_converted = float(minutes) / 60
    time_converted = float(hours) + minutes_converted
    return time_converted


if __name__ == "__main__":
    main()
