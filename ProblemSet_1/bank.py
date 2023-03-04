def greeting():
    text = input("Please, greet us: ").lstrip().lower()
    if text.startswith("hello"):
        print("$0")
    elif text.startswith("h") and text != "hello":
        print("$20")
    else:
        print("$100")


greeting()
