from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/losers/bse/daily/groupa")

# self - whichever elemet we want to find out itself variable is called self element
# text=driver.find_element("xpath","//a[normalize-space()='Fineotex Chemical Lt']/self::a").text
# print(text)

# parent
# text=driver.find_element("xpath","//a[normalize-space()='Fineotex Chemical Lt']/parent::td").text
# print(text)

# child
# childs = driver.find_elements("xpath","//a[normalize-space()='Fineotex Chemical Lt']/ancestor::tr/child::td")
# print(len(childs))

# ancestor
# text = driver.find_element("xpath","//a[normalize-space()='Fineotex Chemical Lt']/ancestor::tr").text
# print(text)

# descendent
descendants = driver.find_elements("xpath","//a[normalize-space()='Fineotex Chemical Lt']/ancestor::tr/descendant::*")
print(len(descendants))
