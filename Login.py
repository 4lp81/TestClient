import requests


def login():
    print("")
    username = input("Username:")
    password = input("password:")

    response = requests.get('http://localhost:8080/jazzers-backend-1.0-SNAPSHOT/api/v1/login/customer?username='+username+'&password='+password)

    try:
        json = response.json()
        print(json)
    except:
        print("Login failed")