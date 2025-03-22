from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver  =webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
# driver.find_element("id","pollanswers-2").click()
# driver.find_element("name","pollanswers-1").click()
# driver.find_element("class name","search-box-text ui-autocomplete-input").click()

# driver.find_element("link text","Computers").click()
# driver.find_element("partial link text","Electro").click()
#
ele=driver.find_elements("tag name","a")
print(len(ele))
for i in ele:
    print(ele[i])# name
# class name
# tag name
# link text
# partial link text
#css selector
# xpath