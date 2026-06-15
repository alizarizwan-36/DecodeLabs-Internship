import random
import string
import math

try:
    length = int(input("Enter password length: "))

    # Validate range properly
    if length <= 8 or length >= 64:
        print("Password length must be greater than 8 and less than 64.")
    else:
        # Character pool
        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        # Generate password
        password = ""

        for _ in range(length):
            password += random.choice(characters)

        # Calculate entropy
        entropy = length * math.log2(len(characters))

        print("\nGenerated Password:", password)
        print("Password Length:", length)
        print("Entropy:", round(entropy, 2), "bits")

except ValueError:
    print("Invalid input! Please enter a valid number.")
