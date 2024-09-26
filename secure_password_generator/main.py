import random
import string

def advanced_password(length=12, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Random Password:", advanced_password(16))
