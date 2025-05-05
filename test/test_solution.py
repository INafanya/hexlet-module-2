import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from src.functions import get_function

get = get_function()

if get({"key": "value"}, "key") != "value":
    raise Exception("Функция работает неверно!")

if get({}, "key", "default") != "default":
    raise Exception("Функция работает неверно!")

if get({"key": "value"}, "key", "default") != "value":
    raise Exception("Функция работает неверно!")

print('Все тесты пройдены!')

