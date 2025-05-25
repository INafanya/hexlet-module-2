import math

def make(numer, denom):
    gcd = math.gcd(numer, denom)
    numer /= gcd
    denom /= gcd
    return {'numer': int(numer), 'denom': int(denom)}


def get_numer(rational):
    return rational['numer']

def get_denom(rational):
    return rational['denom']


def add(rat_one, rat_two):
    numer_one = get_numer(rat_one)
    numer_two = get_numer(rat_two)
    denom_one = get_denom(rat_one)
    denom_two = get_denom(rat_two)
    if denom_one == denom_two:
        result_numer = numer_one + numer_two
        result_denom = denom_one
    else:
        result_numer = (numer_one * denom_two) + (numer_two * denom_one)
        result_denom = denom_one * denom_two
    return make(result_numer, result_denom)


def sub(rat_one, rat_two):
    numer_one = get_numer(rat_one)
    numer_two = get_numer(rat_two)
    denom_one = get_denom(rat_one)
    denom_two = get_denom(rat_two)
    if denom_one == denom_two:
        result_numer = numer_one - numer_two
        result_denom = denom_one
    else:
        result_numer = (numer_one * denom_two) - (numer_two * denom_one)
        result_denom = denom_one * denom_two
    return make(result_numer, result_denom)
# END


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"



rat1 = make(3, 9)
rat2 = make(10, 3)
rat3 = make(-4, 16)
rat4 = make(12, 5)

print(to_str(rat1))
print(to_str(rat2))

print(sub(rat1, rat2))


import os
import sys

print(sys.path.insert(1, os.path.join(sys.path[0], '..')))
print(os.path.join(sys.path[0], '..'))