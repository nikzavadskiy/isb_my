import json
from conf import *


def load_key() -> str:
    try:
        with open(KEY, 'r', encoding='utf-8') as f:
            key_data = json.load(f)
            key = key_data['key'].upper()
            return key
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл ключа {KEY} не найден")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Неверный формат JSON в файле ключа", "", 0)


def load_source_text()-> str:
    try:
        with open(SOURCE_PATH, 'r', encoding='utf-8') as f:
            text = f.read().upper()
            if not text:
                raise ValueError("Исходный текст не может быть пустым")
            return text
    except FileNotFoundError:
        raise FileNotFoundError(f"Исходный текстовый файл {SOURCE_PATH} не найден")


def save_encrypted_text(encrypted_text)-> None:
    try:
        encrypted_lines = encrypted_text.split('\n')
        output_data = {
            'encrypted_text': encrypted_lines
        }
        with open(ENCRYPTED_PATH, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        raise FileNotFoundError(f"Невозможно записать в выходной файл в {ENCRYPTED_PATH}")


def vigenere_encrypt(text, key, alphabet)-> str:
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


def vigenere_decrypt(encrypted_text, key, alphabet)-> str:
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