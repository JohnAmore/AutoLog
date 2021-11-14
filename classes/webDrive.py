# Course: CSC-107-A
# Name: Daniel Bennett
# ID: 0593616
# E-mail: ddbennett@cn.edu

# IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.by import By


# Class webDrive
# This class is designed to open Chrome and use the login information returned from jsonConvert.py
# to login on select websites.

class webDrive(object):
    def __init__(self):
        print('')

    # LOGIN FUNCTION
    def login(self, url, user, password, userHTML, passHTML, buttonHTML):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach",
                                               True)  # This and the line above allows the Chrome browser to detach from the program and become its own entity.
        driver = webdriver.Chrome(r"driver/chromedriver", chrome_options=chrome_options)  # Web Driver Instantiation
        driver.get(url)  # Link for website
        username_tag = driver.find_element(By.XPATH, userHTML)  # HTML ELEMENT FOR USERNAME FIELD
        pass_tag = driver.find_element(By.XPATH, passHTML)  # HTML ELEMENT FOR PASSWORD FIELD
        button_tag = driver.find_element(By.XPATH, buttonHTML)  # HTML ELEMENT FOR LOGIN BUTTON
        # These will enter the fields and click the sign in button.
        username_tag.send_keys(user)
        pass_tag.send_keys(password)

        button_tag.submit()
