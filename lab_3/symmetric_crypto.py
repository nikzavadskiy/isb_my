from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

class SymmetricCrypto:
    @staticmethod
    def generate_key():
        """Generate a 128-bit key for IDEA encryption."""
        return os.urandom(16) 

    @staticmethod
    def encrypt(data: bytes, key: bytes) -> bytes:
        """
        Encrypt data using IDEA algorithm.
        
        Args:
            data: Data to encrypt
            key: 128-bit key for IDEA
            
        Returns:
            Encrypted data with IV
        """
        iv = os.urandom(8)
        
        padder = padding.PKCS7(64).padder()
        padded_data = padder.update(data) + padder.finalize()
        
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        return iv + encrypted_data

    @staticmethod
    def decrypt(encrypted_data: bytes, key: bytes) -> bytes:
        """
        Decrypt data using IDEA algorithm.
        
        Args:
            encrypted_data: Data to decrypt (IV + encrypted data)
            key: 128-bit key for IDEA
            
        Returns:
            Decrypted data
        """

        iv = encrypted_data[:8]
        actual_encrypted_data = encrypted_data[8:]
        
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        
        padded_data = decryptor.update(actual_encrypted_data) + decryptor.finalize()
        
        unpadder = padding.PKCS7(64).unpadder()
        return unpadder.update(padded_data) + unpadder.finalize()