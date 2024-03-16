"""
Module containing the command-line interface logic.
"""

import auth


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


def handle_login():
    """Handles the login process"""
    print("\n--- Login ---")
    username, password = login_menu()
    auth.login(username, password)


def handle_signup():
    """Handles the signup process"""
    print("\n--- Sign Up ---")
    username, password = signup_menu()
    auth.register(username, password)


def main():
    """Runs the Key Guardian CLI"""
    auth.create_users_table()

    while True:
        main_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            handle_login()
        elif choice == "2":
            handle_signup()
        elif choice == "3":
            print("Exiting KeyGuardian. Goodbye!!")
            break
        else:
            print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()
