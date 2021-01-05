import json
import os.path

filename = "whitelist.txt"

def get_white_list():
    try:
        if(os.path.exists(filename) == False):
            return {}
        whitelist = open(filename)
        data = json.load(whitelist)
        return data["white_list"]
    except ValueError:
        print ("Could not convert white list to JSON, the file will be overwritten with new data now")
        return {}

def save(whitelist):
    old_whitelist = get_white_list()

    if(len(old_whitelist) > 0):
        whitelist.extend(old_whitelist)

    # remove duplicates
    non_duplicates = list(dict.fromkeys(whitelist))

    # convert to dictionary
    whitelist = {}
    whitelist["white_list"] = non_duplicates
    config = open(filename, "w")
    json.dump(whitelist, config)

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


if __name__ == "__main__":
    add()