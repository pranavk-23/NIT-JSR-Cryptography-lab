def additive_decrypt(ciphertext):
    ciphertext = ciphertext.upper()
    for key in range(26):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                decrypted = (ord(char) - ord('A') - key) % 26
                plaintext += chr(decrypted + ord('A'))
            else:
                plaintext += char
        print(f'Key {key}: {plaintext}')

ciphertext = "PDAKLANWPEKJOPWNP" 
additive_decrypt(ciphertext)
