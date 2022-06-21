
import urllib

import Login
import SearchProduct
import Session


def main():
    while bool(1):
        print("")
        print("What would you like to do?")
        print("___________________________")
        print("exit \t Exit the programm")
        print("search \t Search a product")
        print("login \t Login to your account")
        print("")
        user_input = input("Please enter a command: ")
        print("")
        if user_input == "search":
            print("Please type an artist or a title")
            title = urllib.parse.quote(input('Enter an artist or a title: '), safe='')  # safe -> include /
            SearchProduct.SearchProduct(title)
        elif user_input == "login":
            if Session.session.loggedin == bool(0):
                print("You are currently in a session")
            else:
                Login.login()
        elif user_input == "exit":
            quit()
        else:
            print("What are you trying?")

if __name__ == "__main__":
    main()