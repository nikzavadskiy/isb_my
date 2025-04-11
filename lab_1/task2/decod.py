def decrypt_text(text, key):
    decrypted_text = []
    for char in text:
        decrypted_text.append(key.get(char, char))
    return ''.join(decrypted_text)