import os
import sys

# sys.path.insert(1, os.path.join(sys.path[0], '..'))
# from src.rational import rational
from src import rational

rat1 = rational.make(3, 9)
rat2 = rational.make(10, 3)
rat3 = rational.make(-4, 16)
rat4 = rational.make(12, 5)


def test_to_str():
    assert rational.to_str(rat1) == "1/3"
    assert rational.to_str(rat3) == "-1/4"


def test_rational1():
    assert rational.get_numer(rat1) == 1
    assert rational.get_denom(rat1) == 3
    assert rational.add(rat1, rat2) == rational.make(11, 3)
    assert rational.sub(rat1, rat2) == rational.make(-3, 1)


def test_rational2():
    assert rational.get_numer(rat3) == -1
    assert rational.get_denom(rat3) == 4
    assert rational.add(rat3, rat4) == rational.make(43, 20)
    assert rational.sub(rat3, rat4) == rational.make(-53, 20)
