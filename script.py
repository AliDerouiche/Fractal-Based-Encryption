import numpy as np
from math import comb

# -----------------------------
# Generate Sierpinski fractal
# -----------------------------
def generate_sierpinski(n):
    F = np.zeros((n, n), dtype=np.uint8)

    for i in range(n):
        for j in range(i + 1):
            F[i, j] = comb(i, j) % 2

    return F


# -----------------------------
# Convert text to bit matrix
# -----------------------------
def text_to_matrix(text, n):

    data = np.frombuffer(text.encode(), dtype=np.uint8)
    bits = np.unpackbits(data)

    required = n * n
    if len(bits) < required:
        bits = np.pad(bits, (0, required - len(bits)))

    matrix = bits.reshape((n, n))

    return matrix


# -----------------------------
# Convert matrix to text
# -----------------------------
def matrix_to_text(matrix):

    bits = matrix.flatten()

    byte_length = len(bits) // 8
    bits = bits[: byte_length * 8]

    bytes_array = np.packbits(bits)

    try:
        return bytes_array.tobytes().decode(errors="ignore")
    except:
        return bytes_array.tobytes()


# -----------------------------
# Encryption
# -----------------------------
def encrypt(plaintext, n=16):

    M = text_to_matrix(plaintext, n)

    F = generate_sierpinski(n)

    C = np.bitwise_xor(M, F)

    return C


# -----------------------------
# Decryption
# -----------------------------
def decrypt(cipher_matrix):

    n = cipher_matrix.shape[0]

    F = generate_sierpinski(n)

    M = np.bitwise_xor(cipher_matrix, F)

    plaintext = matrix_to_text(M)

    return plaintext


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":

    message = "Hello Fractal Encryption"

    print("Original message:")
    print(message)

    cipher = encrypt(message, n=32)

    print("\nEncrypted Matrix:")
    print(cipher)

    recovered = decrypt(cipher)

    print("\nDecrypted message:")
    print(recovered)
