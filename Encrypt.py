def caesar_encrypt(plain_text, key):
    encrypted = ""
    for char in plain_text:
        if char.isalpha():
            shifted = ord(char) + key
            if shifted > ord('Z'):
                shifted -= 26
            encrypted += chr(shifted)
        else:
            encrypted += char  # Preserve spaces and punctuation
    return encrypted

# Get user input
plain_text = input("Enter your message in CAPITAL LETTERS: ")
key = int(input("Enter the encryption key (1-25): "))

# Validate key
if key < 1 or key > 25:
    print("Key must be between 1 and 25.")
else:
    encrypted_text = caesar_encrypt(plain_text, key)
    print(f"Encrypted message: {encrypted_text}")
