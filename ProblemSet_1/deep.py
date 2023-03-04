def deep_thought():
    text = input(
        "What is the Answer to the Great Question of Life? ").strip().lower()
    if text == "42" or text == "forty two" or text == "forty-two":
        print("Yes")
    else:
        print("No")


deep_thought()
