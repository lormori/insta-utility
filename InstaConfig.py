import getpass
import json
import os.path

filename = "config.txt"

def save_details(username, password, webhook):
    user_config = {}

    user_config["user_name"] = username
    user_config["password"] = password
    user_config["webhook"] = webhook

    config = open(filename, "w")
    json.dump(user_config, config)

def save():
    username = input("Type your user name:")
    print("Username inserted is: ", username)

    password = getpass.getpass("Insert password:")
    print("Password inserted is: ", password)

    webhook = input("Insert Discord webhook:")
    print("Discord webhook inserted is: ", webhook)
    
    save_details(username, password, webhook)

def get_username():
    if(os.path.exists(filename) == False):
        save()

    config = open(filename)
    data = json.load(config)
    return data["user_name"]

def get_password():
    if(os.path.exists(filename) == False):
        save()
        
    config = open(filename)
    data = json.load(config)
    return data["password"]

def get_webhook():
    if(os.path.exists(filename) == False):
        save()
        
    config = open(filename)
    data = json.load(config)
    return data["webhook"]