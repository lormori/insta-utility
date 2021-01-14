from igramscraper.instagram import Instagram
from InstaConfig import username, password
from InstaLogin import login
import InstaFollowers

def unfollow_check(driver):
    followers = InstaFollowers.find_followers(driver)

    for follower in followers:
        print(follower)
        
def start():
    driver = login()
    unfollow_check(driver)
    driver.quit()

if __name__ == "__main__":
    start()