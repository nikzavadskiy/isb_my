import pickle
from typing import Tuple
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def save_rsa_keys(private_key, public_key, 
                 private_key_path: str, public_key_path: str) -> None:
    """
    Save RSA keys to files.
    """
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(private_key_path, 'wb') as f:
        f.write(pem_private)
        
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(public_key_path, 'wb') as f:
        f.write(pem_public)

def load_rsa_private_key(private_key_path: str):
    """
    Load RSA private key from file.
    """
    with open(private_key_path, 'rb') as f:
        return serialization.load_pem_private_key(
            f.read(),
            password=None
        )

def save_encrypted_symmetric_key(encrypted_key: bytes, path: str) -> None:
    """
    Save encrypted symmetric key to file.
    
    Args:
        encrypted_key: Encrypted symmetric key
        path: Path to save the key
    """
    with open(path, 'wb') as f:
        pickle.dump(encrypted_key, f)

def load_encrypted_symmetric_key(path: str) -> bytes:
    """
    Load encrypted symmetric key from file.
    
    Args:
        path: Path to encrypted key file
        
    Returns:
        Encrypted symmetric key
    """
    with open(path, 'rb') as f:
        return pickle.load(f)

def read_file(path: str) -> bytes:
    """
    Read file contents.
    
    Args:
        path: Path to file
        
    Returns:
        File contents as bytes
    """
    with open(path, 'rb') as f:
        return f.read()

def write_file(data: bytes, path: str) -> None:
    """
    Write data to file.
    
    Args:
        data: Data to write
        path: Path to write to
    """
    with open(path, 'wb') as f:
        f.write(data)

def save_encrypted_text(data: bytes, path: str) -> None:
    """
    Save encrypted text to file.
    
    Args:
        data: Encrypted data
        path: Path to save the encrypted text
    """
    with open(path, 'wb') as f:
        f.write(data)

def save_decrypted_text(data: bytes, path: str) -> None:
    """
    Save decrypted text to file.
    
    Args:
        data: Decrypted data
        path: Path to save the decrypted text
    """
    with open(path, 'wb') as f:
        f.write(data) 