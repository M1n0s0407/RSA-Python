# Hàm tính gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Hàm tính modulo bình phương nhanh
def fast_modular_exponentiation(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return result

# Chọn hai số nguyên tố p và q
p = 17
q = 23

# Tính modulus n
n = p * q

# Tính giá trị của hàm Euler (phi)
phi_n = (p - 1) * (q - 1)

# Chọn số nguyên e thỏa mãn gcd(e, phi(n)) = 1
e = 7

# Tên cần mã hóa
name = "Alice"

# Mã hóa từng ký tự trong tên
cipher_text = []
for char in name:
    # Chuyển đổi ký tự thành số nguyên theo bảng mã ASCII hoặc Unicode
    plain_text = ord(char)
    
    # Mã hóa ký tự
    encrypted_char = fast_modular_exponentiation(plain_text, e, n)
    
    # Thêm ký tự đã mã hóa vào danh sách cipher_text
    cipher_text.append(encrypted_char)

print("Mã hóa của tên", name, "là:", cipher_text)
