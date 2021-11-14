# Course: CSC-107-A
# Name: Daniel Bennett
# ID: 0593616
# E-mail: ddbennett@cn.edu

# jsonConvert
# This class is designed to convert the .json file into a Python Dictionary, and send the data into
# the main file when called to be used as a variable for the information.
# This will have a connection to the web driving class.

# IMPORTS
from json import *


class jsonConvert(object):

    def __init__(self):
        self.login = r"json/loginInfo.json"  # Sets JSON file location

    # loadJson opens and returns the JSON data through a Python Dictionary.
    def loadJson(self):
        loginInfo = load(open(self.login))
        return loginInfo

    # dumpJson takes the Python Dictionary and turns it back into JSON, writes it to the file, and then closes it. "Saving"
    def dumpJson(self, dict):
        with open(self.login, "w") as f:
            f.write(dumps(dict))
            f.close()
