from selenium import webdriver
from InstaConfig import username, password
import time
import random

count = 0

def scroll_dialog(followNumber, driver):
   time.sleep(2)
   
   # find the dialog
   dialog = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

   followersList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
   numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

   time.sleep(2)

   #scroll down the page
   while(numberOfFollowersInList < followNumber):
      driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
      time.sleep(random.randint(500,1000)/1000)
      numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
      print("Loaded followers: " + str(numberOfFollowersInList))

   followers = []

   for user in followersList.find_elements_by_css_selector('li'):
      userLink = user.find_element_by_css_selector('a').get_attribute('href')
      print(userLink)
      followers.append(userLink)
      if (len(followers) == max):
            break

   return followers

def find_followers(driver, username_to_check = None):
   time.sleep(2)

   if(username_to_check is None):
      username_to_check = username()

   # go to user profile
   driver.get("https://www.instagram.com/" + username_to_check)

   # find number of followers
   allfoll=int(driver.find_element_by_xpath("//li[2]/a/span").text) 
   print("Followers to find: " + str(allfoll))

   # Click followers
   driver.find_element_by_partial_link_text("follower").click()

   return scroll_dialog(allfoll, driver)

def find_following(driver):
   time.sleep(2)

   # go to user profile
   driver.get("https://www.instagram.com/" + username())

   # find number of following
   allFollowing=int(driver.find_element_by_xpath("//li[3]/a/span").text) 
   print("Following to find: " + str(allFollowing))

   # Click following
   driver.find_element_by_partial_link_text("following").click()
   return scroll_dialog(allFollowing, driver)

def find_non_followers(driver):
   followers = find_followers(driver)
   following = find_following(driver)

   if(len(following) > len(followers)):
      return set(following) - set(followers)

   return []
   