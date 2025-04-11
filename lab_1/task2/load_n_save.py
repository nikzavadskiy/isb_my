import json


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_key(key_path):
    with open(key_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def save_decrypted_text(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
            file.write(data)