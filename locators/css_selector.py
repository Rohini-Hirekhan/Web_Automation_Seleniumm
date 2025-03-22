from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
import time

driver = webdriver.Chrome()
driver.get("https://facebook.com")
driver.maximize_window()

# tag and id
driver.find_element("css selector","input#email").send_keys("abc")
driver.find_element("css selector","#email").send_keys("abc")
# time.sleep(180)
#css selector with tag and id
driver.find_element("css selector","input#inputEmail").send_keys("admin")


#tag and class
driver.find_element("css selector","input.email").send_keys("abc")
driver.find_element("css selector",".email").send_keys("abc")

#tag and attribute
driver.find_element("css selector","input[data-testid=pass]").send_keys("abc")
driver.find_element("css selector","[data-testid=pass]").send_keys("abc")

#tag,class and attribute
driver.find_element("css selector","input.email[attribute=value]")