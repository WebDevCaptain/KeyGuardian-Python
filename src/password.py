"""
Module containing functions for CRUD operations on passwords.
"""

import os
from cryptography.fernet import Fernet
import hashlib
import base64
import storage
import session


# Parameters for PBKDF2
PBKDF2_ITERATIONS = 100000  # Number of iterations
SALT_LENGTH = 32  # Salt length in bytes
KEY_LENGTH = 32  # Derived key length in bytes


def derive_key(session_key, salt):
    """Derive a key from the session_key using PBKDF2."""
    key = hashlib.pbkdf2_hmac(
        "sha256", session_key.encode(), salt, PBKDF2_ITERATIONS, KEY_LENGTH
    )

    fernet_key = base64.urlsafe_b64encode(key)
    return fernet_key


def generate_salt():
    """Generate a random salt."""
    return os.urandom(SALT_LENGTH)


def encrypt_password(password, salt):
    """Encrypt the password"""
    key = derive_key(session.SESSION_KEY, salt)
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password, salt):
    """Decrypt the password"""
    key = derive_key(session.SESSION_KEY, salt)
    cipher = Fernet(key)
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password


def store_password(user_id, website, username, password, notes=""):
    """Store a new password."""
    random_salt = generate_salt()
    encrypted_password = encrypt_password(password, random_salt)
    storage.store_password(
        user_id, website, username, encrypted_password, random_salt, notes
    )


def get_passwords(user_id):
    """Retrieves all passwords for a user."""
    passwords = storage.get_passwords(user_id)
    encrypted_passwords = [
        (website, username, password, notes, salt)
        for website, username, password, notes, salt in passwords
    ]

    decrypted_passwords = [
        (
            encrypted_password[0],
            encrypted_password[1],
            decrypt_password(encrypted_password[2], encrypted_password[4]),
            encrypted_password[3],
            encrypted_password[4],
        )
        for encrypted_password in encrypted_passwords
    ]

    return decrypted_passwords


def update_password(user_id, website, new_password):
    """Update an existing password."""
    salt = storage.get_salt(user_id, website)
    encrypted_password = encrypt_password(new_password, salt)
    storage.update_password(user_id, website, encrypted_password)


def delete_password(user_id, website):
    """Delete a password"""
    storage.delete_password(user_id, website)
