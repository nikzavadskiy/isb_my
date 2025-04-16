import json
from collections import Counter


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            if not text:
    except FileNotFoundError:
        raise FileNotFoundError(f"Исходный файл {file_path} не найден")


def read_json_config(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
            if not config:
                raise ValueError("Конфигурационный файл пуст")
            return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл конфигурации {file_path} не найден")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Неверный формат JSON в файле конфигурации", "", 0)


def read_key(key_path):
    try:
        with open(key_path, 'r', encoding='utf-8') as file:
            key = json.load(file)
            if not key:
                raise ValueError("Файл с ключом пуст")
            return key
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл с ключом {key_path} не найден")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Неверный формат JSON в файле с ключом", "", 0)


def save_to_json(data, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except IOError:
        raise IOError(f"Ошибка при сохранении файла {output_path}")


def save_decrypted_text(data, output_path):
    try:    
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(data)
    except IOError:
        raise IOError(f"Ошибка при сохранении файла {output_path}")
