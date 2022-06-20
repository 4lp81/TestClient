import json
import requests
import Main


def SearchProduct(title):
    is_exit = bool(0)
    while is_exit == bool(0):
        uri = "http://localhost:8080/jazzers-backend-1.0-SNAPSHOT/api/v1/product/searchDigital?username=cpe2877&password=password&titleOrInterpret=" + title

        url = requests.get(uri)
        text = url.text
        data = json.loads(text)
        count = len(data)
        create_table(data, count)
        print(data)
        print("")
        print("## Available commands ##")
        print("home \t Go back to home menu")
        print("add \t Add an article in shopping cart")
        print("")
        command = input("Please enter a command: ")
        print("")
        if command == "home":
            Main.main()


def create_table(data, count):
    print("{:10} {:<40} {:<30} {:<20} {:<20} {:<10} {:<10} ".format(
        'Position',
        'ProductId',
        'Title',
        'Interpret',
        'Medium',
        'Genre',
        'Price'
    ))


    for x in range(count):
        work = data[x]

        print("{:9} {:<40} {:<30} {:<20} {:<20} {:<10} {:<10}".format(
            x+1,
            work['productId'],
            work['title'],
            work['interpret'],
            work['medium'],
            work['genre'],
            work['price']
        ))