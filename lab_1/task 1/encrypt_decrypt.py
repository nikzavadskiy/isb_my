def vigenere_encrypt(text, key, alphabet):
    if not text:
        raise ValueError("Текст не может быть пустым")
    if not key:
        raise ValueError("Ключ не может быть пустым")
    if not alphabet:
        raise ValueError("Алфавит не может быть пустым")

    encrypted_text = []
    key_length = len(key)
    alphabet_length = len(alphabet)

    for i, char in enumerate(text):
        if char in alphabet:
            text_pos = alphabet.index(char)
            key_pos = alphabet.index(key[i % key_length])

            new_pos = (text_pos + key_pos) % alphabet_length

            encrypted_char = alphabet[new_pos]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)


def vigenere_decrypt(encrypted_text, key, alphabet):
    if not encrypted_text:
        raise ValueError("Зашифрованный текст не может быть пустым")
    if not key:
        raise ValueError("Ключ не может быть пустым")
    if not alphabet:
        raise ValueError("Алфавит не может быть пустым")

    decrypted_text = []
    key_length = len(key)
    alphabet_length = len(alphabet)

    for i, char in enumerate(encrypted_text):
        if char in alphabet:
            encrypted_pos = alphabet.index(char)
            key_pos = alphabet.index(key[i % key_length])

            original_pos = (encrypted_pos - key_pos) % alphabet_length

            decrypted_char = alphabet[original_pos]
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)