from functions import*
from encrypt_decrypt import vigenere_encrypt
import json


def main():
    try:
        config =  read_json_config('conf2.json')
        key = load_key(config)
        source_text = load_source_text(config)
        
        encrypted_text = vigenere_encrypt(source_text, key, config['ALPHABET'])
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