import getpass
import json
import os.path

filename = "config.txt"

def save():
    user_config = {}

    user_config["user_name"] = input("Type your user name:")
    print("Username inserted is: ", user_config.get("user_name"))

    user_config["password"] = getpass.getpass("Insert password:")
    print("Password inserted is: ", user_config["password"])

    config = open(filename, "w")
    json.dump(user_config, config)

def username():
    if(os.path.exists(filename) == False):
        save()

    config = open(filename)
    data = json.load(config)
    return data["user_name"]

def password():
    if(os.path.exists(filename) == False):
        save()
        
    config = open(filename)
    data = json.load(config)
    return data["password"]