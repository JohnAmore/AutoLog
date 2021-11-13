# Course: CSC-107-A
# Name: Daniel Bennett
# ID: 0593616
# E-mail: ddbennett@cn.edu
import time

from selenium import webdriver
from selenium import *
from os import *
from selenium.webdriver.chrome.options import *


# webDrive
# This class is designed to open Chrome and use the login information returned from jsonConvert.py
# to login on select websites.
from selenium.webdriver.common.by import By


class webDrive(object):
    def __init__(self):
        print('')

    def login(self, url, user, password, userHTML, passHTML, buttonHTML):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(r"driver/chromedriver", chrome_options=chrome_options)  # Web Driver Instantiation
        driver.get(url)  # Link for website
        username_tag = driver.find_element(By.XPATH, userHTML)
        pass_tag = driver.find_element(By.XPATH, passHTML)
        button_tag = driver.find_element(By.XPATH, buttonHTML)
        # These will enter the fields and click the sign in button.
        username_tag.send_keys(user)
        pass_tag.send_keys(password)

        button_tag.submit()

