from lib2to3.fixes.fix_input import context

from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()



@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element("xpath","//input[@placeholder='Password']").send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element("xpath","//button[normalize-space()='Login']").click()




@then('User must successfully login to the Dashboard page')
def step_impl(context):
    text =  context.driver.find_element("xpath","//h6[normalize-space()='Dashboard']").text
    assert text == 'Dashboard'
   # context.driver.close()
