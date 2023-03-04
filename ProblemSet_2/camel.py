def camel_to_snake():
    text = input("Write you camelCase string here: ")
    snake_text = ""
    for letter in text:
        if letter.isupper():
            snake_text = snake_text + "_" + letter.lower()
        else:
            snake_text = snake_text + letter.lower()

    print(snake_text)


camel_to_snake()
