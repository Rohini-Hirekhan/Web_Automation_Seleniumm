import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.find_element("xpath","//input[@placeholder='Username']").send_keys("Admin")
driver.find_element("xpath","//input[@placeholder='Password']").send_keys("admin123")
driver.find_element("xpath","//button[normalize-space()='Login']").click()
time.sleep(3)
driver.find_element("xpath","//li[1]//a[1]//span[1]").click()
time.sleep(3)
driver.find_element("xpath","//span[normalize-space()='User Management']").click()
driver.find_element("xpath","//a[normalize-space()='Users']").click()
time.sleep(3)