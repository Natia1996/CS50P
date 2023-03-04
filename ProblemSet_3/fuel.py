while True:
    try:
        x, y = [int(i) for i in input("Friction: ").split("/")]
        friction = x/y
        if x > y:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        continue
    else:
        percentage = friction * 100
        if percentage <= 1:
            print("E")
            break
        elif percentage >= 99:
            print("F")
            break
        else:
            print(f'{round(percentage)}%')
            break
