 Playfair Cipher Implementation

def generate_key_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in keyword:
        if char not in used and char.isalpha():
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J excluded
        if char not in used:
            used.add(char)
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def preprocess_text(text):
    text = text.upper().replace("J", "I")
    prepared = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        if not char1.isalpha():
            i += 1
            continue
        if i+1 < len(text):
            char2 = text[i+1]
            if char2 == char1:
                prepared += char1 + "X"
                i += 1
            else:
                prepared += char1 + char2
                i += 2
        else:
            prepared += char1 + "X"
            i += 1
    return prepared


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def playfair_encrypt(text, matrix):
    text = preprocess_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # Same row
            cipher += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:  # Same column
            cipher += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:  # Rectangle
            cipher += matrix[r1][c2] + matrix[r2][c1]
    return cipher


def playfair_decrypt(cipher, matrix):
    plain = ""

    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # Same row
            plain += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:  # Same column
            plain += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:  # Rectangle
            plain += matrix[r1][c2] + matrix[r2][c1]
    return plain


# Example Usage
if __name__ == "__main__":
    keyword = "MONARCHY"
    text = "NITJSR"

    key_matrix = generate_key_matrix(keyword)

    print("Key Matrix:")
    for row in key_matrix:
        print(row)

    encrypted = playfair_encrypt(text, key_matrix)
    decrypted = playfair_decrypt(encrypted, key_matrix)

    print("\nOriginal:", text)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
