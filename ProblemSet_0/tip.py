def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    corrected_text = d.lstrip("$")
    float_value = float(corrected_text)
    return (float_value)


def percent_to_float(p):
    stripped_text = p.rstrip('%')
    float_convert = float(stripped_text) / 100
    return (float_convert)


main()
