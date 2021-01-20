from InstaConfig import username, password
from InstaLogin import login
import InstaConfig
import instaloader
import InstaFollowers
import time
from os import path
import ast
import discord_webhook
import sys

follower_list_file = "followers_list.txt"

def save_followers_to_file(current_followers):
        f = open(follower_list_file, "w")
        f.write(str(current_followers))
        f.close()

def send_discord_message(message, profiles):

    for profile in profiles:
        message += "https://www.instagram.com/{} \n".format(profile)
        if len(message) > 1900:
            # getting closer to the 2000 characters limit, send message now and reset
            webhook = discord_webhook.DiscordWebhook(url=InstaConfig.webhook(), content=message)
            webhook.execute()
            message = ""
            # avoid throttling
            time.sleep(10)

    webhook = discord_webhook.DiscordWebhook(url=InstaConfig.webhook(), content=message)
    webhook.execute()

def check_followers():
    L = instaloader.Instaloader()
    L.login(InstaConfig.username(), InstaConfig.password())

    profile = instaloader.Profile.from_username(L.context, "lomos_dungeon")
    current_followers = profile.get_followers()
    current_followers = [user.username for user in current_followers]

    if not path.exists(follower_list_file):
        save_followers_to_file(current_followers)
    else:
        f = open(follower_list_file, "r+")
        old_followers = f.read()
        f.close()
        old_followers = ast.literal_eval(old_followers)

        follower_change = len(current_followers) - len(old_followers)

        if follower_change != 0:
            unfollowers = set(old_followers) - set(current_followers)
            message = "Followers changed by {} - from {} to {}".format(follower_change, len(old_followers), len(current_followers))
            send_discord_message(message, unfollowers)
        
        save_followers_to_file(current_followers)

def start():
    while(True):
        try:
            check_followers()
            time.sleep(60 * 60) # wait 1 hour before running again 
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)
        except Exception as e:
            print(e)
            sys.exit(0)

def test_webhook():
    L = instaloader.Instaloader()
    L.login(InstaConfig.username(), InstaConfig.password())

    profile = instaloader.Profile.from_username(L.context, "lollo.bot")
    current_followers = profile.get_followers()

    current_followers = [user.username for user in current_followers]

    save_followers_to_file(current_followers)

    message = "You have {} followers: \n".format(len(current_followers))
    send_discord_message(message, current_followers)

if __name__ == "__main__":
    start()
    #test_webhook()
