import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
btn = driver.find_element("xpath","//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(btn).click().perform()
time.sleep(3)