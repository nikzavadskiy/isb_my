from cryptography.hazmat.primitives.asymmetric import rsa, padding as rsa_padding
from cryptography.hazmat.primitives import hashes, serialization

class AsymmetricCrypto:
    @staticmethod
    def generate_key_pair():
        """
        Generate RSA key pair.
        
        Returns:
            Tuple of (private_key, public_key)
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def encrypt(data: bytes, public_key) -> bytes:
        """
        Encrypt data using RSA public key.
        
        Args:
            data: Data to encrypt
            public_key: RSA public key
            
        Returns:
            Encrypted data
        """
        ciphertext = public_key.encrypt(
            data,
            rsa_padding.OAEP(
                mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    @staticmethod
    def decrypt(encrypted_data: bytes, private_key) -> bytes:
        """
        Decrypt data using RSA private key.
        
        Args:
            encrypted_data: Data to decrypt
            private_key: RSA private key
            
        Returns:
            Decrypted data
        """
        plaintext = private_key.decrypt(
            encrypted_data,
            rsa_padding.OAEP(
                mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext