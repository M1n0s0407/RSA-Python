import random
from math import gcd


def find_e(phi_n):
    while True:
        e = random.randint(1000000, 9999999)  # Generate a random 7-digit number
        if gcd(e, phi_n) == 1:
            return e


# Example usage:
phi_n = 12507844777900

e = find_e(phi_n)
print(e)
