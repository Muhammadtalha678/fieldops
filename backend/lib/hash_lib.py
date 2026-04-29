from pwdlib.hashers.argon2 import Argon2Hasher
from pwdlib import PasswordHash
# Aron2 is one way as only encrypt not decrypt
password_hash = PasswordHash((Argon2Hasher(),))

def hash_password(password:str) -> str:
    """Hash a password using Argon2"""
    return password_hash.hash(password=password)

def verify_password(plain_text:str,hash_password:str) -> bool:
    """verify a password aganst it hash"""
    return password_hash.verify(password=plain_text,hash=hash_password)
