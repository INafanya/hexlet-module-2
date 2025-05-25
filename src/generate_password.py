import random
import string


def generate_password(
    length=5, include_uppercase=False, include_digits=False, include_special=False
):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    digits = string.digits if include_digits else ""
    special = string.punctuation if include_special else ""

    all_chars = lowercase + uppercase + digits + special

    password = []
    password.append(random.choice(lowercase))
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_digits:
        password.append(random.choice(digits))
    if include_special:
        password.append(random.choice(special))

    for _ in range(length - len(password)):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return "".join(password)