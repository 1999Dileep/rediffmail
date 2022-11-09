import time

from webdriver_manager.core import driver

from features.pageobjects.Base import BaseSettingsPage
from selenium.webdriver.common.action_chains import ActionChains


class SendmailPage(BaseSettingsPage):

    def __init__(self,driver):
        super().__init__(driver)

    def clickWriteMail(self):
        self.DynamicImplicitWait(40)
        self.ClickLinks("writeMail_XPATH")
        time.sleep(10)

    def setTo(self, to):
        self.DynamicImplicitWait(40)
        self.TypeEditBoxEmail("toField_XPATH", to)
        time.sleep(10)

    def setSubjectArea(self, subject):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("subject_XPATH",subject)
        time.sleep(5)

    def ClickboldButton(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("Boldtext_XPATH")
        time.sleep(5)

    def ClickItalicButton(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("ClickItalic_XPATH")
        time.sleep(5)

    def setComposeArea(self,compose):
        self.SwitchFrameAddress("frameCompose_CSSSELECTOR")
        self.TypeEditBox("composeArea_XPATH",compose)
        time.sleep(10)

    def clickSaveMail(self):
        self.DynamicImplicitWait(40)
        self.SwitchOutFrameAddress()
        self.ClickButton("save_XPATH")
        time.sleep(10)

    def Draft(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("Draft_XPATH")
        time.sleep(10)

    def CheckBox(self):
        self.DynamicImplicitWait(40)
        self.ClickCheckbox("DeleteCheckBox_XPATH")
        time.sleep(10)

    def Delete(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("Delete_XPATH")
        time.sleep(10)
        self.ClickButton("OK_XPATH")
        time.sleep(10)

    def clickLogout(self):
        self.DynamicImplicitWait(40)
        self.ClickLinks("logout_XPATH")
        time.sleep(10)

    def validlogout(self, expectedTextVal):
        self.DynamicImplicitWait(40)
        self.AssertText("logoutText_XPATH", expectedTextVal)
