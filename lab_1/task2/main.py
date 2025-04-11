from count_frequencies import *
from conf2 import *
from load_n_save import *
from decod import *


def main():
    try:
        text = read_file(SOURCE_PATH)
        key = read_key(KEY_PATH)
      
        frequencies = count_frequencies(text)

        save_to_json(frequencies, FREQUENCY_IN_TEXT)

        decrypted_text = decrypt_text(text, key)

        save_decrypted_text(decrypted_text, DECRYPTED_PATH)

    except FileNotFoundError:
        print(f"Error: Could not find the source file {SOURCE_PATH}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()