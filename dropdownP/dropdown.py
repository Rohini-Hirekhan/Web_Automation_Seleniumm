from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=account/register")
wait=WebDriverWait(driver,10)
drp_country=wait.until(EC.presence_of_element_located(driver.find_element("xpath","//select[@id='input-country']")))
drp= Select(drp_country)
drp.select_by_visible_text("India")

# we will have to give it manually count start from option so it will mostly equivalent to value
drp.select_by_index("13")

drp.select_by_value("10")

# capture all the options and print them
alloptions=drp.options
print(alloptions)

# print all options
for i in alloptions:
    print(i.text)

# select option from dropdown without using built in function

