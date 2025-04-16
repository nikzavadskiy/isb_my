def count_frequencies(text):
    text = text.replace('\n', '')

    total_chars = len(text)

    frequency_counter = Counter(text)

    frequencies = {}
    for char, count in frequency_counter.items():
        frequencies[char] = round(count / total_chars, 4)

    return dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))


def decrypt_text(text, key):
    decrypted_text = []
    for char in text:
        decrypted_text.append(key.get(char, char))
    return ''.join(decrypted_text)
