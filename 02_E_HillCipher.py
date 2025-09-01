# Convert characters to numbers and back
def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr(n + ord('A'))

# Preprocess text: remove spaces + pad with X
def process_text(text, size):
    text = text.replace(" ", "").upper()
    while len(text) % size != 0:
        text += 'X'
    return text

# Matrix multiplication mod 26 (2x2 * 2x1 vector)
def multiply_matrix_vector(matrix, vector):
    result = []
    for row in matrix:
        val = sum(row[i] * vector[i] for i in range(len(vector))) % 26
        result.append(val)
    return result

# Modular inverse of determinant using Extended Euclidean Algorithm
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Find inverse of 2x2 matrix mod 26
def inverse_matrix(matrix):
    # determinant
    det = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        raise ValueError("Matrix is not invertible modulo 26")
    
    # adjugate matrix
    adj = [[matrix[1][1], -matrix[0][1]],
           [-matrix[1][0], matrix[0][0]]]
    
    # multiply adjugate by det_inv mod 26
    inv = [[(det_inv * adj[i][j]) % 26 for j in range(2)] for i in range(2)]
    return inv

# Hill Cipher Encryption
def hill_encrypt(plaintext, key_matrix):
    plaintext = process_text(plaintext, 2)
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        block = plaintext[i:i+2]
        vec = [char_to_num(c) for c in block]
        enc_vec = multiply_matrix_vector(key_matrix, vec)
        ciphertext += ''.join(num_to_char(num) for num in enc_vec)
    return ciphertext

# Hill Cipher Decryption
def hill_decrypt(ciphertext, key_matrix):
    key_inv = inverse_matrix(key_matrix)
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        block = ciphertext[i:i+2]
        vec = [char_to_num(c) for c in block]
        dec_vec = multiply_matrix_vector(key_inv, vec)
        plaintext += ''.join(num_to_char(num) for num in dec_vec)
    return plaintext

# -----------------------------
# Main program
# -----------------------------
if __name__ == "__main__":
    # 2x2 key matrix
    key_matrix = [[3, 3],
                  [2, 5]]
    
    plaintext = "HELLO"
    
    print("Plaintext :", plaintext)
    cipher = hill_encrypt(plaintext, key_matrix)
    print("Ciphertext:", cipher)
    
    decrypted = hill_decrypt(cipher, key_matrix)
    print("Decrypted :", decrypted)
