# Course: CSC-107-A
# Name: Daniel Bennett
# ID: 0593616
# E-mail: ddbennett@cn.edu

# jsonConvert
# This class is designed to convert the .json file into a Python Dictionary, and send the data into
# the main file when called to be used as a variable for the information.
# This will have a connection to the web driving class.
from json import *


class jsonConvert(object):

    def __init__(self):
        self.login = r"json/loginInfo.json"

    def loadJson(self):
        loginInfo = load(open(self.login))
        return loginInfo

    def dumpJson(self, dict):
        with open(self.login, "w") as f:

            f.write(dumps(dict))
            f.close()
