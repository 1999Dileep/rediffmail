import time

from Utilities import configreader
from features.pageobjects.Base import BaseSettingsPage


class LoginPage(BaseSettingsPage):

    def __init__(self,driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)
        time.sleep(5)
        self.DynamicImplicitWait(40)


    def validUsernameText(self, expectedText):
        self.DynamicImplicitWait(40)
        self.AssertText("usernaneText_XPATH", expectedText)
        time.sleep(4)

    def setUsername(self, username):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("username_ID",username)
        time.sleep(4)

    def validPasswordText(self, expectedTextVal):
        self.DynamicImplicitWait(40)
        self.AssertText("passwordText_XPATH", expectedTextVal)
        time.sleep(4)

    def setPassword(self, password):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("password_ID",password)
        time.sleep(4)

    def clickSignIn(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("signinButton_NAME")
        time.sleep(4)

    def validWriteMailText(self, expectedTextVal):
        self.DynamicImplicitWait(40)
        self.AssertText("writeMailText_XPATH", expectedTextVal)
        time.sleep(4)




