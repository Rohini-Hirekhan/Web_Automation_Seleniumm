import time
from os import times

from selenium import webdriver


driver = webdriver.Chrome()
# driver.get("https://google.com")
# driver.implicitly_wait(15)
# # it will applicable to all below statements
# # it will wait max 15 sec for element if element not found will get exception
# # but if we get element <15s then it will not wait for again 15s it will execute next statement.
# webelement = driver.find_element("xpath","//textarea[@id='APjFqb']")
# webelement.send_keys("selenium")
# webelement.submit()
# time.sleep(30)

driver.get("https://youtube.com")
driver.find_element("xpath","//input[@placeholder = 'search' and @name='search_query]").send_keys("sdet")
driver.find_element("xpath","//button[@class='ytSearchboxComponentSearchButton']").send_keys("sel")