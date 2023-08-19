def decrypt(ciphertext, d, n):
    plaintext = pow(ciphertext, d, n)
    return plaintext


# Example usage:
ciphertext = 9182271226214
d = 8311719970027
n = 12507852135013

plaintext = decrypt(ciphertext, d, n)
print(plaintext)
