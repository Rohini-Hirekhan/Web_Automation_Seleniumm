import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#create select class object and pass select cls webelement

webelement = driver.find_element("id","country")
drp = Select(webelement)

# select option from the dropdown using index,value and text
#
# drp.select_by_value("uk")
# time.sleep(5)
# drp.select_by_index(4)
# time.sleep(5)
# drp.select_by_visible_text("India")
# time.sleep(5)

# select all options from the dropdown and print its value
#
# alloptions = drp.options
# for i in alloptions:
#     print(i.text)
#
# select option from all and click on it
alloptions = drp.options
for i in alloptions:
    if i.text == 'India':
        i.click()
time.sleep(10)