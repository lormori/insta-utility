from igramscraper.instagram import Instagram
from InstaConfig import username, password
from InstaLogin import login
import InstaFollowers
import time

def unfollow_check(driver):
    followers = InstaFollowers.find_followers(driver)

    f = open("list_followers.txt", "w")

    for follower in followers:
        print(follower)
        f.write("Now the file has more content!")
    
    f.close()

    while(True):
        time.sleep(60)
        followers = InstaFollowers.find_followers(driver)

        f = open("list_followers.txt", "r")
        old_users = f.read().splitlines()

def start():
    driver = login()
    unfollow_check(driver)
    driver.quit()

if __name__ == "__main__":
    start()