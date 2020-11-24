from InstaLogin import login
from InstaUnfollow import unfollow_non_followees

def main():
    driver = login()
    unfollow_non_followees(driver)

if __name__ == "__main__":
    main()