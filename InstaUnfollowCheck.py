from InstaConfig import username, password
from InstaLogin import login
import InstaConfig
import instaloader
import InstaFollowers
import time
from os import path
import ast
import discord_webhook

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
        current_followers = [user.username for user in current_followers]
        old_followers = ast.literal_eval(old_followers)

        follower_change = len(current_followers) - len(old_followers)

        if follower_change != 0:
            unfollowers = set(old_followers) - set(current_followers)

            message = "Your followers have changed by {}: from {} to {} \n".format(follower_change, len(old_followers), len(current_followers))

            if unfollowers > 0:
                message += '\n'.join(["https://www.instagram.com/{}".format(unfollower) for unfollower in unfollowers])

            webhook = discord_webhook.DiscordWebhook(url="https://discord.com/api/webhooks/801565339976466512/cFcV4CgUY8XhOXOKGJiumuR7TDyMyi9TTGkS06riGmj87AnZZ8qO4HrW8Z8HZ6FaUYNf", content=message)
            webhook.execute()
        
        save_followers_to_file(current_followers)

def test_webhook():
    L = instaloader.Instaloader()
    L.login(InstaConfig.username(), InstaConfig.password())

    profile = instaloader.Profile.from_username(L.context, "lollo.bot")
    current_followers = profile.get_followers()

    current_followers = [user.username for user in current_followers]
    message = "Your followers: {} \n".format(len(current_followers))
    message += '\n'.join(["https://www.instagram.com/{}".format(follower) for follower in current_followers])

    webhook = discord_webhook.DiscordWebhook(url="https://discord.com/api/webhooks/801565339976466512/cFcV4CgUY8XhOXOKGJiumuR7TDyMyi9TTGkS06riGmj87AnZZ8qO4HrW8Z8HZ6FaUYNf", content=message)
    webhook.execute()

if __name__ == "__main__":
    #start()
    test_webhook()
