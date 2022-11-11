import logging
import time
import allure
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities import configreader
from Utilities.LogUtil import Logger

from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.SavemailPage import SavemailPage

log = Logger(__name__, logging.INFO)


@given(u'we navigate to Rediffmail account')
def step_impl(context):
    context.reg = LoginPage(context.driver)
    context.reg.open(configreader.ConfigReader("base info", "URL"))
    log.logger.info("Navigated to Rediffmail Login Page")

@when(u'we validate the username text')
def step_impl(context):
    context.reg.validUsernameText("Username")
    log.logger.info("Username Text Validated")

@when(u'we type in the "{username}" edit box')
def step_impl(context, username):
    context.reg.setUsername(username)
    log.logger.info("Username field typed")

@when(u'we validate the password text')
def step_impl(context):
    context.reg.validPasswordText("Password")
    log.logger.info("Password Text Validated")

@when(u'we type in the "{password}" field')
def step_impl(context, password):
    context.reg.setPassword(password)
    log.logger.info("Password field typed")

@when(u'we click on the sign in button')
def step_impl(context):
    context.reg.clickSignIn()
    log.logger.info("Signin button clicked")

@then(u'we validate inbox page opens')
def step_impl(context):
    context.reg.validWriteMailText("Write mail")
    log.logger.info("Write mail text typed")

@given(u'we click in write mail link')
def step_impl(context):
    context.save = SavemailPage(context.driver)
    context.save.clickWriteMail()
    log.logger.info("Write Mail Clicked")

@when(u'we fill the "{to}" field')
def step_impl(context, to):
    time.sleep(6)
    context.save.setTo(to)
    log.logger.info("To field typed")

@when(u'we type the "{subject}" area')
def step_impl(context, subject):
    context.save.setSubjectArea(subject)
    log.logger.info("Subject field typed")

@when(u'we click on the Bold button')
def step_impl(context):
    context.save.ClickboldButton()
    log.logger.info("Clicked on Bold Button")

@when(u'we click on the Italic button')
def step_impl(context):
    context.save.ClickItalicButton()
    log.logger.info("Clicked on Italic Button")

@when(u'type in "{compose}" area')
def step_impl(context,compose):
    context.save.setComposeArea(compose)
    log.logger.info("Compose field typed")

@when(u'click on save button')
def step_impl(context):
    context.save.clickSaveMail()
    log.logger.info("Save Button Clicked")

@when(u'Click on Draft Button')
def step_impl(context):
    context.save.Draft()
    log.logger.info("Clicked on Draft Button")


@when(u'click on Delete Check Button')
def step_impl(context):
   context.save.CheckBox()
   log.logger.info("Clicked on CheckBox")

@when(u'Click on Delete Button')
def step_impl(context):
    context.save.Delete()
    log.logger.info("Clicked on Delete")

@when(u'we click on logout link')
def step_impl(context):
    context.save.clickLogout()
    log.logger.info("Logout link clicked")

@then(u'we validate that we have logded out of rediffmail account')
def step_impl(context):
    context.save.validlogout("You have successfully signed out of Rediffmail.")
    log.logger.info("Validate text after logout")
