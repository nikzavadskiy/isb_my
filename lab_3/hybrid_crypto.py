from symmetric_crypto import SymmetricCrypto
from asymmetric_crypto import AsymmetricCrypto
import functions_for_hel

class HybridCryptoSystem:
    def __init__(self):
        pass

    def generate_keys(self, encrypted_key_path: str, public_key_path: str, private_key_path: str) -> None:
        """
        Generate and save all necessary keys for the hybrid system.
        
        Args:
            encrypted_key_path: Path to save encrypted symmetric key
            public_key_path: Path to save public key
            private_key_path: Path to save private key
        """
        symmetric_key = SymmetricCrypto.generate_key()
        private_key, public_key = AsymmetricCrypto.generate_key_pair()

        functions_for_hel.save_rsa_keys(private_key, public_key, private_key_path, public_key_path)

        with open('symmetric_key.json', 'wb') as f:
            f.write(symmetric_key)

        encrypted_symmetric_key = AsymmetricCrypto.encrypt(symmetric_key, public_key)
        functions_for_hel.save_encrypted_symmetric_key(encrypted_symmetric_key, encrypted_key_path)

    def encrypt_file(self, input_file_path: str, private_key_path: str, 
                    encrypted_key_path: str, output_file_path: str) -> None:
        """
        Encrypt a file using the hybrid system.
        
        Args:
            input_file_path: Path to input file
            private_key_path: Path to private key
            encrypted_key_path: Path to encrypted symmetric key
            output_file_path: Path to save encrypted file
        """
        private_key = functions_for_hel.load_rsa_private_key(private_key_path)
        encrypted_symmetric_key = functions_for_hel.load_encrypted_symmetric_key(encrypted_key_path)
        symmetric_key = AsymmetricCrypto.decrypt(encrypted_symmetric_key, private_key)

        data = functions_for_hel.read_file(input_file_path)
        encrypted_data = SymmetricCrypto.encrypt(data, symmetric_key)

        functions_for_hel.write_file(encrypted_data, output_file_path)
        functions_for_hel.save_encrypted_text(encrypted_data, 'encrypted_text.txt')

    def decrypt_file(self, input_file_path: str, private_key_path: str, 
                    encrypted_key_path: str, output_file_path: str) -> None:
        """
        Decrypt a file using the hybrid system.
        
        Args:
            input_file_path: Path to encrypted file
            private_key_path: Path to private key
            encrypted_key_path: Path to encrypted symmetric key
            output_file_path: Path to save decrypted file
        """
        private_key = functions_for_hel.load_rsa_private_key(private_key_path)
        encrypted_symmetric_key = functions_for_hel.load_encrypted_symmetric_key(encrypted_key_path)
        symmetric_key = AsymmetricCrypto.decrypt(encrypted_symmetric_key, private_key)

        encrypted_data = functions_for_hel.read_file(input_file_path)
        decrypted_data = SymmetricCrypto.decrypt(encrypted_data, symmetric_key)

        functions_for_hel.write_file(decrypted_data, output_file_path)
        functions_for_hel.save_decrypted_text(decrypted_data, 'decrypted_text.txt') 
