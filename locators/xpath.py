import time

from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver = webdriver.Chrome()

driver.get("https://demo.sensfrx.ai/login.php")


# xpath
driver.find_element("xpath","//input[@id='inputEmail']").send_keys("admin")

# xpath with contains
# driver.find_element("xpath","//input[contains(@id,'input')]").send_keys("admin7")

# xpath with starts-with
driver.find_element("xpath","//input[starts-with(@name,'pass')]").send_keys("admin")

# xpath with text()
driver.find_element("xpath","//button[text()='Login']").click()
time.sleep(30)
