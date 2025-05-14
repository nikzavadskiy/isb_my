import sys
import argparse
from hybrid_crypto import HybridCryptoSystem


def create_parser():
    parser = argparse.ArgumentParser(description='Hybrid Cryptosystem (RSA + IDEA)')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    generate_parser = subparsers.add_parser('generate', help='Generate encryption keys')
    generate_parser.add_argument('--encrypted-key', required=True, help='Path to save encrypted symmetric key')
    generate_parser.add_argument('--public-key', required=True, help='Path to save public key')
    generate_parser.add_argument('--private-key', required=True, help='Path to save private key')

    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a file')
    encrypt_parser.add_argument('--input', required=True, help='Path to input file')
    encrypt_parser.add_argument('--private-key', required=True, help='Path to private key')
    encrypt_parser.add_argument('--encrypted-key', required=True, help='Path to encrypted symmetric key')
    encrypt_parser.add_argument('--output', required=True, help='Path to save encrypted file')
    encrypt_parser.add_argument('--show-encrypted', action='store_true', help='Show encrypted content in hex format')

    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt a file')
    decrypt_parser.add_argument('--input', required=True, help='Path to encrypted file')
    decrypt_parser.add_argument('--private-key', required=True, help='Path to private key')
    decrypt_parser.add_argument('--encrypted-key', required=True, help='Path to encrypted symmetric key')
    decrypt_parser.add_argument('--output', required=True, help='Path to save decrypted file')

    return parser


def print_hex_dump(data: bytes, bytes_per_line: int = 16):
    for i in range(0, len(data), bytes_per_line):
        chunk = data[i:i + bytes_per_line]
        hex_values = ' '.join(f'{b:02x}' for b in chunk)
        ascii_values = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
        print(f'{i:08x}: {hex_values:<{bytes_per_line * 3}} | {ascii_values}')


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    crypto_system = HybridCryptoSystem()

    try:
        if args.command == 'generate':
            crypto_system.generate_keys(args.encrypted_key, args.public_key, args.private_key)
            print("Keys generated successfully!")
        elif args.command == 'encrypt':
            crypto_system.encrypt_file(args.input, args.private_key, args.encrypted_key, args.output)
            print("File encrypted successfully!")
            
            if args.show_encrypted:
                print("\nEncrypted content (hex dump):")
                print("-" * 60)
                with open(args.output, 'rb') as f:
                    encrypted_data = f.read()
                print_hex_dump(encrypted_data)
                print("-" * 60)
                
        elif args.command == 'decrypt':
            crypto_system.decrypt_file(args.input, args.private_key, args.encrypted_key, args.output)
            print("File decrypted successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 