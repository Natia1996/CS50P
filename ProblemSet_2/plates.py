def starts_with_two_letters(s):
    return s[:2].isalpha()


def contains_two_to_six_letters_or_numbers(s):
    return s.isalnum() and 2 <= len(s) <= 6


def ends_with_one_to_three_letters(s):
    for i in s:
        if i.isdigit():
            ind = s.index(i)
            return s[ind:].isdigit() and int(i) != 0
    return True


def is_valid(s):
    return starts_with_two_letters(s) and contains_two_to_six_letters_or_numbers(s) and ends_with_one_to_three_letters(s)


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()
