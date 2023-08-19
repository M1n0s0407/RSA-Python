import math

def check_coprime(e, phi_n):
    if math.gcd(e, phi_n) == 1:
        return True
    else:
        return False

# Example usage:
e = 2564981
phi_n = 1102176

is_coprime = check_coprime(e, phi_n)
print(is_coprime)
