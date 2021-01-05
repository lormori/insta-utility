from igramscraper.instagram import Instagram

def unfollow_check():
    instagram = Instagram()
    instagram.with_credentials("asd", "asd")
    instagram.login()

    print("Unfollow Check hello world")

def start():
    unfollow_check()


if __name__ == "__main__":
    start()