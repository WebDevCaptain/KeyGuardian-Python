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


def get_passwords(user_id):
    """Retrieves all passwords for a user."""
    passwords = storage.get_passwords()
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
