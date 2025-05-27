import sys
from enum import Enum
from hybrid_crypto import HybridCryptoSystem

class Command(Enum):
    GENERATE = "generate"
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [generate|encrypt|decrypt] [options]")
        return

    command = sys.argv[1]
    try:
        command_enum = Command(command)
    except ValueError:
        print(f"Invalid command: {command}")
        print("Available commands: generate, encrypt, decrypt")
        return

    crypto_system = HybridCryptoSystem()

    try:
        match command_enum:
            case Command.GENERATE:
                if len(sys.argv) != 5:
                    print("Usage: python main.py generate <encrypted-key> <public-key> <private-key>")
                    return
                crypto_system.generate_keys(sys.argv[2], sys.argv[3], sys.argv[4])
                print("Keys generated successfully!")

            case Command.ENCRYPT:
                if len(sys.argv) != 6:
                    print("Usage: python main.py encrypt <input> <private-key> <encrypted-key> <output>")
                    return
                crypto_system.encrypt_file(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
                print("File encrypted successfully!")

            case Command.DECRYPT:
                if len(sys.argv) != 6:
                    print("Usage: python main.py decrypt <input> <private-key> <encrypted-key> <output>")
                    return
                crypto_system.decrypt_file(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
                print("File decrypted successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
