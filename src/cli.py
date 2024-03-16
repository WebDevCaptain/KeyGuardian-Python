"""
Module containing the command-line interface logic.
"""

import auth
from storage import create_password_table
import password as password_utils


def main_menu():
    """Displays the main menu for Key Guardian"""
    print("Welcome to Key Guardian")
    print("1. Login")
    print("2. Sign up")
    print("3. Exit")


def login_menu():
    """Prompt the user for login credentials"""
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password


def signup_menu():
    """Prompt the user for creating a user account in Key Guardian"""
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    return username, password


def password_menu():
    """Display password management menu."""
    print("\n--- Password Management ---")
    print("1. Store a new password")
    print("2. Retrieve saved passwords")
    print("3. Update a password")
    print("4. Delete a password")
    print("5. Back to main menu")


def handle_login():
    """Handles the login process"""
    print("\n--- Login ---")
    username, password = login_menu()
    return auth.login(username, password)


def handle_signup():
    """Handles the signup process"""
    print("\n--- Sign Up ---")
    username, password = signup_menu()
    auth.register(username, password)


def handle_password_management(user_id):
    """Handle password management process."""
    while True:
        password_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            entered_password = input(
                "Enter password: "
            )  # password_utils.generate_secure_password() will be implemented later
            password_utils.store_password(user_id, website, username, entered_password)
            print("Password stored successfully.")
        elif choice == "2":
            passwords = password_utils.get_passwords(user_id)
            if passwords:
                print("Saved Passwords:")
                for website, username, password, notes, _ in passwords:
                    print(
                        f"Website: {website}, Username: {username}, Password: {password}, Notes: {notes}"
                    )
            else:
                print("No passwords saved.")
        elif choice == "3":
            website = input("Enter website: ")
            new_password = input(
                "Enter new password: "
            )  # password_utils.generate_secure_password()
            password_utils.update_password(user_id, website, new_password)
            print("Password updated successfully.")
        elif choice == "4":
            website = input("Enter website: ")
            password_utils.delete_password(user_id, website)
            print("Password deleted successfully.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    """Runs the Key Guardian CLI"""
    auth.create_users_table()
    create_password_table()

    while True:
        main_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = handle_login()

            if user_id:
                handle_password_management(user_id)
        elif choice == "2":
            handle_signup()
        elif choice == "3":
            print("Exiting KeyGuardian. Goodbye!!")
            break
        else:
            print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()
