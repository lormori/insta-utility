from InstaLogin import login
from InstaUnfollow import unfollow_non_followees
import InstaConfig
import InstaUnfollowCheck
import argparse

def do_unfollow_check(args):
        InstaUnfollowCheck.start()

def do_unfollow(args):
    driver = login()
    unfollow_non_followees(driver, args.unfollowcount)
    driver.quit()

def main(args):
    if args.username and args.webhook:
        InstaConfig.save_details(args.username, args.password, args.webhook)

    if args.unfollow:
        do_unfollow(args)
    elif args.checkfollowers:
        do_unfollow_check(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Insta Utility - Automatically unfollow who doesn't follow you back, or check for changes in your followers.")

    parser.add_argument("-uf", "--unfollow", help="Unfollow who doesn't follow you back.", action="store_true")
    parser.add_argument("-cf", "--checkfollowers", help="Unfollow who doesn't follow you back.", action="store_true")
    parser.add_argument("--unfollowcount", default=10, type=int)
    parser.add_argument("--username", help="Instagram username to login with.", type=str)
    parser.add_argument("--password", help="Instagram password to login with.", type=str)
    parser.add_argument("--webhook", help="Discord Webhook.", type=str)

    args = parser.parse_args()
    main(args)