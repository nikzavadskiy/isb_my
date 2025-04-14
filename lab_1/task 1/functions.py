import json
import os


def read_json_config(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file {file_path} not found")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return {}
    except Exception as e:
        print(f"Error reading configuration: {str(e)}")
        return {}


def load_key(config):
    try:
        with open(config['KEY'], 'r', encoding='utf-8') as f:
            key_data = json.load(f)
            if 'key' not in key_data:
                raise KeyError(f"Файл ключа {config['KEY']} не содержит поле 'key'")
            key = key_data['key'].upper()
            if not key:
                raise ValueError("Ключ не может быть пустым")
            if not all(char in config['ALPHABET'] for char in key):
                raise ValueError("Ключ содержит недопустимые символы")
            return key
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл ключа {config['KEY']} не найден")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Неверный формат JSON в файле ключа", "", 0)


def load_source_text(config):
    try:
        with open(config['SOURCE_PATH'], 'r', encoding='utf-8') as f:
            text = f.read().upper()
            if not text:
                raise ValueError("Исходный текст не может быть пустым")
            return text
    except FileNotFoundError:
        raise FileNotFoundError(f"Исходный текстовый файл {config['SOURCE_PATH']} не найден")


def save_encrypted_text(encrypted_text, config):
    try:
        encrypted_lines = encrypted_text.split('\n')
        output_data = {
            'encrypted_text': encrypted_lines
        }
        with open(config['ENCRYPTED_PATH'], 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        raise FileNotFoundError(f"Невозможно записать в выходной файл {config['ENCRYPTED_PATH']}")