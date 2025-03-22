import time

from selenium import webdriver

# disable the notification pop up
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")


driver = webdriver.Chrome(options = ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(5)


