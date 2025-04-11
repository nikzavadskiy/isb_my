from functions import load_key, load_source_text, vigenere_encrypt, save_encrypted_text
from conf import ALPHABET
import json


def main():
    try:
        key = load_key()
        source_text = load_source_text()
        
        encrypted_text = vigenere_encrypt(source_text, key, ALPHABET)
        save_encrypted_text(encrypted_text)
        print("Шифрование успешно завершено!")
        
    except FileNotFoundError as e:
        print(f"Ошибка файла: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"Ошибка JSON: {str(e)}")
    except KeyError as e:
        print(f"Ошибка ключа: {str(e)}")
    except ValueError as e:
        print(f"Ошибка значения: {str(e)}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {str(e)}")


if __name__ == '__main__':
    main()