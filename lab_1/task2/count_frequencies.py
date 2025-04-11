from collections import Counter
import json


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def count_frequencies(text):
    text = text.replace('\n', '')
 
    total_chars = len(text)
    
    frequency_counter = Counter(text)
    
    frequencies = {}
    for char, count in frequency_counter.items():
        frequencies[char] = round(count / total_chars, 4)  
    
    return dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))


def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)