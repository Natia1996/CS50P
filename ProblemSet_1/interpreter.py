def calculate():
    text = input("Please, write your calculation here: ").split(" ")
    x = float(text[0])
    y = text[1]
    z = float(text[2])

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        if z == 0:
            print("Error")

        result = x / z
    else:
        print("Invalid operator")

    print(f"{result:.1f}")


calculate()
