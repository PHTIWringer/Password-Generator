import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    # Combine all necessary characters
    characters = string.ascii_letters + string.digits

    # Ensure the password includes at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]

    # Fill the rest of the password with random choices from all characters
    password += [random.choice(characters) for _ in range(length - 4)]

    # Shuffle the password list to avoid predictable sequences
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Generate a 12-character password
password = generate_password(8)
print(password)

