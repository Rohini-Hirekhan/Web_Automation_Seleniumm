import time

from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element("xpath","//span[@id='select2-billing_country-container']").click()
time.sleep(3)
countrylist=driver.find_elements("xpath","//*[@id='select2-billing_country-results']/li")
for i in countrylist:
    if i.text == 'India':
        i.click()
        break
time.sleep(4)