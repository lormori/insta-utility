from InstaFollowers import find_non_followers
from InstaWhiteList import white_list

def is_whitelisted(username : str):
    for i in white_list():
        if(username.__contains__(i)):
            return True
    return False

def unfollow_non_followees(driver):
    to_unfollow = find_non_followers(driver)
    
    print("Starting unfollow..")
    print(to_unfollow)

    print("Whitelist..")
    print(white_list())

    to_unfollow = [ entry for entry in to_unfollow if is_whitelisted(entry) == False ] 

    print("Filtered Whitelist Users")
    print(to_unfollow)