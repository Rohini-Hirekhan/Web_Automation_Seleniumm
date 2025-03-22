from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver

driver = webdriver.Chrome()
# driver.get("https://google.com")
# print(driver.current_url)
# print(driver.page_source)

driver.get("https://www.snapdeal.com")
driver.get("http://www.amazon.com")
driver.back()
driver.forward()
driver.refresh()


# import selenium
# print(selenium.__version__)

