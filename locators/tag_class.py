from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager


driver=webdriver.Chrome()
driver.get("https://demo.sensfrx.ai/login.php")

# tag and id
driver.find_element( "css selector","")