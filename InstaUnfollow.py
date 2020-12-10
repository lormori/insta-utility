from InstaFollowers import find_non_followers
from InstaWhiteList import white_list
from random import randrange
import time

def wait(driver, min, max):
    print("Min wait: " + str(min) + " - Max Wait: " + str(max))
    waitTime = randrange(min,max)
    print("Wait time: " + str(waitTime))
    time.sleep(waitTime)

def is_whitelisted(username : str):
    for i in white_list():
        if(username.__contains__(i)):
            return True
    return False

def unfollow_user(driver, username):
    # go to that user's main page
    print("Unfollowing " + username)
    driver.get(username)
    wait(driver, 1, 6)

    driver.find_element_by_xpath('//span[@aria-label="Following"]').click()
    wait(driver, 2, 4)
    driver.find_element_by_xpath('//button[text()="Unfollow"]').click()

def unfollow_non_followees(driver, max_to_unfollow):
    to_unfollow = find_non_followers(driver)
    
    print("Starting unfollow..")
    print(to_unfollow)

    print("Whitelist..")
    print(white_list())

    to_unfollow = [ entry for entry in to_unfollow if is_whitelisted(entry) == False ] 

    print("Filtered Whitelist Users")
    print(to_unfollow)

    current_count = 0

    for user in to_unfollow:
        unfollow_user(driver, user)
        wait(driver, 2,5)
        current_count += 1

        if(current_count > max_to_unfollow):
            break
    
    print("Total unfollowed: " + str(current_count))

    