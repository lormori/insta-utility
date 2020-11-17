from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from InstaConfig import username, password

def click_button(driver, element_xpath):
    driver.find_element_by_xpath(element_xpath).click()

def wait_for_element_and_click(driver, element_xpath, timeout):
    try:
        element_present = expected_conditions.presence_of_element_located((By.XPATH,element_xpath))
        WebDriverWait(driver, timeout).until(element_present)

        click_button(driver, element_xpath)
    except TimeoutException:
        print( "Timed out waiting for page to load")

def login():
    # Go to Instagram
    driver = webdriver.Chrome(executable_path="C:/Dev/Personal/chromedriver.exe")
    driver.get("https://www.instagram.com/")

    # Accept Cookies
    driver.find_element_by_xpath('//button[text()="Accept"]').click()

    # Fill out username and password and click
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys(username())

    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(password())

    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//button[@type="submit"]').click()

    # Save login info?
    wait_for_element_and_click(driver, '//button[text()="Not Now"]', 5)

    # Notifications?
    wait_for_element_and_click(driver, '//button[text()="Not Now"]', 5)

    return driver