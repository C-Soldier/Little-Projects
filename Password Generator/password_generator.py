import random

letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

special_char = ("!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "", "]", "^", "_", "`", "{", "|", "}", "~")

password = []

while True:
    password.clear()
    input("Press enter for new password...")
    for r in range(8):
        char_set = random.choice([letters, numbers, special_char])
        password.append(random.choice(char_set))

    for char in password:
        print(char, end=" ")
    print("\n")
