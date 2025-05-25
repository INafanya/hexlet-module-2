import os
import re

import pytest
import right
import solution
import wrong1
import wrong2
import wrong3


@pytest.fixture(name="generate_password")
def _generate_password():
    name = os.environ["FUNCTION_VERSION"]
    return {
        "user_implementation": solution,
        "right": right,
        "wrong1": wrong1,
        "wrong2": wrong2,
        "wrong3": wrong3,
    }[name].generate_password


def test_generate_password_min_len(generate_password):
    password = generate_password()
    assert len(password) == 5


# BEGIN (write your solution here)
def test_generate_password_upper_case(generate_password):
    password = generate_password(5, include_uppercase=True)
    assert any(char.isupper() for char in password) == True

def test_generate_password_digits(generate_password):
    password = generate_password(5, include_uppercase=True, include_digits=True)
    assert any(char.isdigit() for char in password) == True


def test_generate_password_special(generate_password):
    password = generate_password(5, include_uppercase=True, include_digits=True, include_special=True)
    special = '!@#$%^&*(),.?":{}|<>'
    assert any(True if char in special else False for char in password) == True
# END

# Teacher:
def test_generate_password_default(generate_password):
    password = generate_password(30)
    assert (
        re.search(r'[A-Z\d!@#$%^&*(),.?":{}|<>]', password) is None
    ), "default pass should only include lowercase letters"


def test_generate_password_symbol_for_each_type(generate_password):
    password = generate_password(
        6, include_uppercase=True, include_digits=True, include_special=True
    )
    assert re.search(r"[A-Z]", password) is not None
    assert re.search(r"\d", password) is not None
    assert re.search(r"[^a-zA-Z0-9]", password) is not None