"""
Module containing functions for CRUD operations on passwords.
"""

import storage


def encrypt_password(password):
    """Encrypt the password"""
    # Use AES to encrypt. For now, using string reversal
    return password[::-1]


def decrypt_password(encrypted_password):
    """Decrypt the password"""
    return encrypted_password[::-1]


def store_password(user_id, website, username, password, notes=""):
    """Store a new password."""
    encrypted_password = encrypt_password(password)
    storage.store_password(user_id, website, username, encrypted_password, notes)


def get_passwords(user_id):
    """Retrieves all passwords for a user."""
    passwords = storage.get_passwords(user_id)
    decrypted_passwords = [
        (website, username, decrypt_password(password), notes)
        for website, username, password, notes in passwords
    ]
    return decrypted_passwords


def update_password(user_id, website, new_password):
    """Update an existing password."""
    encrypted_password = encrypt_password(new_password)
    storage.update_password(user_id, website, encrypted_password)


def delete_password(user_id, website):
    """Delete a password"""
    storage.delete_password(user_id, website)
