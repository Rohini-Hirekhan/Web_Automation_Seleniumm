import time

from selenium import webdriver
from behave import *

@given('launch chrome browser')
def Launch_Browser(context):
    context.driver = webdriver.Chrome()



@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)


@then('verify that the loop present on page')
def verifyLogo(context):
    status=context.driver.find_element("xpath","//img[@alt='company-branding']").is_dispalyed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()

