from InstaConfig import username, password
from InstaLogin import login
import InstaConfig
import instaloader
import InstaFollowers
import time
from os import path
import ast

follower_list_file = "followers_list.txt"

def start():
    L = instaloader.Instaloader()
    L.login(InstaConfig.username(), InstaConfig.password())

    profile = instaloader.Profile.from_username(L.context, "lomos_dungeon")
    current_followers = profile.get_followers()

    for user in current_followers:
        print(user.username)

    if not path.exists(follower_list_file):
        f = open(follower_list_file, "w")
        f.write(str([user.username for user in current_followers]))
        f.close()
    else:
        f = open(follower_list_file, "r+")
        old_followers = f.read()
        f.close()
        old_followers = ast.literal_eval(old_followers)




if __name__ == "__main__":
    start()