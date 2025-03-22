import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element("xpath","//input[@id='dob']").click()
time.sleep(3)

# select month
obj=Select(driver.find_element("xpath","//select[@aria-label='Select month']"))
obj.select_by_visible_text("Jul")
# select year
obj2 = Select(driver.find_element("xpath","//select[@aria-label='Select year']"))
obj2.select_by_visible_text("1996")
time.sleep(3)
# select date - extract all date from the table then compare with expected result

dates = driver.find_elements("xpath","//div[@id='ui-datepicker-div']//table//tr//td//a")
for i in dates:
    if i.text == "16":
        i.click()
        break
time.sleep(3)
