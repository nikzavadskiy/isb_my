from functions_for_help import *
from decod import *
import json

def main():
    try:
        config = read_json_config('conf2.json')
        text = read_file(config['SOURCE_PATH'])

        frequencies = count_frequencies(text)
        save_to_json(frequencies, config['FREQUENCY_IN_TEXT'])
            
        key = read_key(config['KEY_PATH'])

        decrypted_text = decrypt_text(text, key)
        save_decrypted_text(decrypted_text, config['DECRYPTED_PATH'])

    except Exception as e:
        print(f"Непредвиденная ошибка: {str(e)}")
        return
    except FileNotFoundError as e:
        print(f"Ошибка: {str(e)}")
        return
    except json.JSONDecodeError as e:
        print(f"Ошибка: {str(e)}")
        return
    except ValueError as e:
        print(f"Ошибка: {str(e)}")
        return
    except IOError as e:
        print(f"Ошибка: {str(e)}")
        return
    
    

if __name__ == "__main__":
    main()