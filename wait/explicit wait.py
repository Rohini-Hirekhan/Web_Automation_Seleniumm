from re import search

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
# explicit wait - it is condition based wait
# implememntation - we have to declare webdriverwait first then by using this object we can use
# condition
# poll frequesncy - it will go in 2 sec to check element is found or not till 10s
# 10 - maximum time out - if element not found in 10s it will give exception
# we can handle that exception by defining it  - ignored_exceptions=[Exception]

driver.get("https://youtube.com")
# search = ("xpath","//input[@placeholder = 'search']")

wait = WebDriverWait(driver,20,poll_frequency=2)

# it is condition untill we found element (no need to wright findelement)
ele = wait.until(EC.presence_of_element_located(("xpath","//input[@placeholder = 'search']")))
ele.send_keys("sdet by pavan")

