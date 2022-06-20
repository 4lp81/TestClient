
import urllib

import Login
import SearchProduct


def main():
    while bool(1):
        print("")
        print("What would you like to do? Commands")
        print("exit \t \t Exit the programm")
        print("search \t \t Search a product")
        print("purchase \t Purchase a product")
        print("login \t Login to your account")
        print("")
        user_input = input("Please enter a command: ")
        print("")
        if user_input == "search":
            print("Please type an artist or a title")
            title = urllib.parse.quote(input('Enter an artist or a title: '), safe='')  # safe -> include /
            SearchProduct.SearchProduct(title)
        elif user_input == "login":
            Login.login()

if __name__ == "__main__":
    main()