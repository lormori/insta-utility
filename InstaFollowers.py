from selenium import webdriver

from InstaConfig import username, password

def find_non_followers(driver):
   # go to user profile
   driver.get("https://www.instagram.com/" + username())

   # Click followers
   driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()

   driver.execute_script('''
      var fDialog = document.querySelector('div[role="dialog"] .isgrP');
      fDialog.scrollTop = fDialog.scrollHeight
   ''')

   # Go to user's following
   driver.get("https://www.instagram.com/" + username() + "/following/")

