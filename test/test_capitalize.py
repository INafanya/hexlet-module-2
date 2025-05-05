import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from src.capitalize import capitalize


if capitalize("hello") != "Hello":
    raise Exception("Функция работает неверно!")

if capitalize("") != "":
    raise Exception("Функция работает неверно!")

print("Все тесты пройдены!")