from count_frequencies import *
from conf2 import SOURCE_PATH, FREQUENCY_IN_TEXT
from load_n_save import *


def main():
    try:
        text = read_file(SOURCE_PATH)
      
        frequencies = count_frequencies(text)

        save_to_json(frequencies, FREQUENCY_IN_TEXT)
        
        print(f"Character frequencies have been saved to {FREQUENCY_IN_TEXT}")
        
    except FileNotFoundError:
        print(f"Error: Could not find the source file {SOURCE_PATH}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()