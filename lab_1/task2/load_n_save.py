import json


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)