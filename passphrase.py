import random
import string

NUM_PASSPHRASES = 1000  # Number of passphrases to generate

def generate_passphrase(length, include_numbers, include_symbols, include_uppercase, include_lowercase):
    characters = ""

    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        return None

    passphrase = ''.join(random.choice(characters) for _ in range(length))
    return passphrase

def generate_and_store_passphrases(num_passphrases):
    with open("passphrases.txt", "w") as f:
        for _ in range(num_passphrases):
            length = random.randint(12, 20)  # Vary the length of passphrases
            include_numbers = random.choice([True, False])
            include_symbols = random.choice([True, False])
            include_uppercase = random.choice([True, False])
            include_lowercase = random.choice([True, False])

            passphrase = generate_passphrase(length, include_numbers, include_symbols, include_uppercase, include_lowercase)
            
            if passphrase:
                f.write(passphrase + "\n")

def main():
    generate_and_store_passphrases(NUM_PASSPHRASES)
    print(f"{NUM_PASSPHRASES} passphrases generated and stored in 'passphrases.txt'.")

if __name__ == "__main__":
    main()
