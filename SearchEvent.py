import json
import urllib

import requests
import Main


def SearchEvent(title):
    is_exit = bool(0)
    while is_exit == bool(0):
        uri = "http://localhost:8080/backendTest-1.0-SNAPSHOT/api/v1/event/searchEvent?username=aar9086&password=test&titleOrInterpret=" + title

        url = requests.get(uri)
        text = url.text
        data = json.loads(text)
        count = len(data)
        create_table(data, count)
        print(data)
        print("")
        print("## Available commands ##")
        print("home \t Go back to home menu")
        print("search \t Search another work")
        print("exit \t Exit the programm")
        print("")
        command = input("Please enter a command: ")
        print("")
        if command == "home":
            Main.main()
        elif command == "search":
            print("Please type an artist or a event")
            title = urllib.parse.quote(input('Enter an artist or a title: '), safe='')  # safe -> include /
            SearchEvent(title)
        elif command == "exit":
            quit()


def create_table(data, count):
    print("{:10} {:<40} {:<30} {:<20} {:<20} {:<10} {:<10} {:<10} {:<10} {:<10} ".format(
        'Position',
        'eventId',
        'title',
        'location',
        'description',
        'date',
        'price',
        'time',
        'availableSeat',
        'availableStanding'
    ))


    for x in range(count):
        event = data[x]

        print("{:9} {:<40} {:<30} {:<20} {:<20} {:<10} {:<10}".format(
            x + 1,
            event['eventId'],
            event['title'],
            event['location'],
            event['description'],
            event['date'],
            event['price'],
            event['time'],
            event['availableSeat'],
            event['availableStanding']
        ))