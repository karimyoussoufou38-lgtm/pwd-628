import random
import hashlib
import mixer  # importe mixer.py pour mélanger avant chaque génération

def generate_password(all_chars_path="db.txt"):
    # Mélanger le fichier avant génération
    mixer.mix_file(all_chars_path)

    # Lire les 6000 caractères mélangés
    with open(all_chars_path, "r", encoding="utf-8") as f:
        chars = f.read()

    # Choisir longueur aléatoire de 20 à 50
    length = random.randint(20, 50)

    # Générer le mot de passe
    password = "".join(random.choice(chars) for _ in range(length))

    return password

def sha512_hash(text):
    # Encode + SHA-512
    return hashlib.sha512(text.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    pwd = generate_password()
    hashed = sha512_hash(pwd)
    print("Mot de passe généré :")
    print("\nSHA-512 :")
    print(hashed)
