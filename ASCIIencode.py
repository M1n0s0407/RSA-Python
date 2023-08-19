def plaintext_to_ascii(plaintext):
    ascii_encoding = []
    for char in plaintext:
        ascii_value = ord(char)  # Convert character to ASCII value
        ascii_encoding.append(str(ascii_value))
    return " ".join(ascii_encoding)


# Example usage:
plaintext = "Khoi"
ascii_representation = plaintext_to_ascii(plaintext)
print(ascii_representation)
