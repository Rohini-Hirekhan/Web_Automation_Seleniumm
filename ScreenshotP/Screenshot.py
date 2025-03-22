from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot("C:\\POC\\homepage.png")
# driver.save_screenshot(os.getcwd()+'\\home.png')
driver.get_screenshot_as_file(os.getcwd()+'\\asp.png')