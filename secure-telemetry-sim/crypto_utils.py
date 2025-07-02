from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a new Fernet symmetric encryption key
    and saves it to 'secret.key' file.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the encryption key from 'secret.key' file.
    """
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_message(message: str, key: bytes) -> bytes:
    """
    Encrypts a string message using the provided key.
    Returns the encrypted bytes.
    """
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

def decrypt_message(token: bytes, key: bytes) -> str:
    """
    Decrypts encrypted bytes using the provided key.
    Returns the original string message.
    """
    f = Fernet(key)
    decrypted = f.decrypt(token)
    return decrypted.decode()

