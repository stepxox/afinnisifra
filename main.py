import string

a = 3
b = 5
m = 26

unwanted_characters = ['.', '-', ',', '!', '_', ')', '(', '<', '>']

numbers = [t.upper() for t in ["+", "ě", "š", "č", "ř", "ž", "ý", "á", "í", "é"]]

abc = string.ascii_uppercase


def mod_inverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1


def to_normal(cipher=""):
    normal = ""
    cipher = cipher.upper()

    for char in unwanted_characters:
        cipher = cipher.replace(char, "")

    cipher = cipher.replace(" ", "").replace("XMEZERAX", " ")

    for c in cipher:
        if c in abc:
            normal += abc[((abc.index(c) - b) * mod_inverse(a, m)) % m]
        elif c == " ":
            normal += " "
        elif c in numbers:
            normal += str(numbers.index(c))

    return normal


def to_cipher(text=""):
    cipher = ""
    cipher_list = []
    text = text.upper()

    for char in unwanted_characters:
        text = text.replace(char, "")

    text_list = list(text)

    for c in text_list:
        if c in abc:
            cipher_list.append(abc[(a * abc.index(c) + b) % m])
        elif c == " ":
            cipher_list.append("XMEZERAX")
        elif c.isnumeric():
            cipher_list.append(numbers[int(c)])

    for i, c in enumerate(cipher_list):
        cipher += str(c)

        if i > 0 and i % 5 == 0:
            cipher += " "

    return cipher


def main():
    if m % a == 0:
        print("m nesmi byt delitelne a")
        return

    if mod_inverse(a, m) == -1:
        print("Pri inverzi a % m nenalezneme vysledek")
        return

    cipher = to_cipher("Ahoj Pepo, sejdeme se v 5 u mostu.")
    print(cipher)

    normal = to_normal(cipher)
    print(normal)


main()
