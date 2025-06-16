def caesar_decrypt(cipher_text, key):
    decrypted = ""
    for char in cipher_text:
        if char.isalpha():
            shifted = ord(char) - key
            if shifted < ord('A'):
                shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char  # Preserve spaces and punctuation
    return decrypted

#cipher_text = "OR FHER GB QEVAX LBHE BINYGVAR"
#cipher_text = "MUUJ SUXTOTM"
cipher_text = "K NQXG AQW"

# Try all 25 possible keys
for key in range(1, 26):
    result = caesar_decrypt(cipher_text, key)
    print(f"Key {key}: {result}")
  
