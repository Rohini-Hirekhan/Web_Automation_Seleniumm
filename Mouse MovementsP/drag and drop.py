import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source = driver.find_element("xpath","//div[@id='box6']")
destination = driver.find_element("xpath","//div[@id='box102']")

act = ActionChains(driver)
act.drag_and_drop(source,destination).perform()
time.sleep(4)