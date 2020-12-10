import json
import os.path

filename = "whitelist.txt"

def white_list():
    if(os.path.exists(filename) == False):
        return {}

    whitelist = open(filename)
    data = json.load(whitelist)
    return data["white_list"]

def clean_duplicates():
    mylist = list(dict.fromkeys(white_list()))

    whitelist = {}
    whitelist["white_list"] = mylist
    config = open(filename, "w")
    json.dump(whitelist, config)

def save(whitelist):
    new_whitelist = whitelist

    if(os.path.exists(filename)):
        old_whitelist = {}
        config = open(filename)
        data = json.load(config)
        old_whitelist = data["white_list"]

        if(len(old_whitelist) > 0):
            new_whitelist.extend(old_whitelist)

    whitelist = {}
    whitelist["white_list"] = new_whitelist
    config = open(filename, "w")
    json.dump(whitelist, config)

    clean_duplicates()

def add():
    newWhitelist = []

    while(True):
        username = input("Enter user to whitelist: ")
        newWhitelist.append(username)
        print("Added user: " + username)

        continueInput = input("Add new user? (y/n)")
        if(continueInput == "n"):
            break

    save(newWhitelist)