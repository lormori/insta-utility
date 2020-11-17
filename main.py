from InstaLogin import login
from InstaFollowers import find_non_followers

def main():
    driver = login()
    find_non_followers(driver)

if __name__ == "__main__":
    main()