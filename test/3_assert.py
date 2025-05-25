import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from src.capitalize import capitalize


assert capitalize("hello") == "Hello"

assert capitalize("") == ""

assert capitalize("hello") == "hello"


