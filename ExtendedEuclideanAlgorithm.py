def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_euclidean_algorithm(b, a % b)
    return gcd, y, x - (a // b) * y


def mod_inverse(e, phi_n):
    gcd, x, _ = extended_euclidean_algorithm(e, phi_n)
    if gcd != 1:
        raise ValueError("Inverse does not exist")
    return x % phi_n


# Example usage:
e = 4701063
phi_n = 12507844777900

d = mod_inverse(e, phi_n)
print("The value of d is:", d)
