import random

def mix_file(path="all.txt"):
    # Lire tous les caractères
    with open(path, "r", encoding="utf-8") as f:
        chars = list(f.read())

    # Mélanger
    random.shuffle(chars)

    # Réécrire
    with open(path, "w", encoding="utf-8") as f:
        f.write("".join(chars))

if __name__ == "__main__":
    mix_file()
