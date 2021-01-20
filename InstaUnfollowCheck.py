from InstaConfig import username, password
from InstaLogin import login
import InstaConfig
import instaloader
import InstaFollowers
import time
from os import path
import ast

follower_list_file = "followers_list.txt"

def save_followers_to_file(current_followers):
        f = open(follower_list_file, "w")
        f.write(str([user.username for user in current_followers]))
        f.close()

def start():
    L = instaloader.Instaloader()
    L.login(InstaConfig.username(), InstaConfig.password())

    profile = instaloader.Profile.from_username(L.context, "lomos_dungeon")
    current_followers = profile.get_followers()

    for user in current_followers:
        print(user.username)

    if not path.exists(follower_list_file):
        save_followers_to_file(current_followers)
    else:
        f = open(follower_list_file, "r+")
        old_followers = f.read()
        f.close()
        old_followers = ast.literal_eval(old_followers)

        follower_change = len(current_followers) - len(old_followers)

        if follower_change != 0:
            # send discord message here
            unfollowers = set(old_followers) - set(current_followers)

            
        
        save_followers_to_file(current_followers)



if __name__ == "__main__":
    start()