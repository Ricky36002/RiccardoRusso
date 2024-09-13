from Crypto.Cipher import AES
import base64
import itertools
import string

# Decryption function
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text

# Padding function
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# Brute-force to find the correct key
def find_key_and_decrypt(encrypted_text):
    possible_chars = string.ascii_letters  # Uppercase and lowercase letters
    for prefix in itertools.product(possible_chars, repeat=4):
        key = ''.join(prefix) + 'IsASecretKey'
        try:
            decrypted_text = decrypt(encrypted_text, key)
            # Assuming the decrypted text will be printable and sensible
            if decrypted_text:
                print(f"Key: {key}")
                print(f"Decrypted Text: {decrypted_text}")
                return
        except:
            continue

# The given encrypted message
encrypted_text = "OgJuOYJZT0FDb47DBOkNgA=="

# Execute the decryption with brute-force key search
find_key_and_decrypt(encrypted_text)
