def modular_exponentiation(x, e, n):
    result = 1
    while e > 0:
        if e % 2 == 1:
            result = (result * x) % n
        x = (x * x) % n
        e //= 2
    return result


# Example usage:
x = 104
e = 4701063
n = 12507852135013

result = modular_exponentiation(x, e, n)
print(result)
