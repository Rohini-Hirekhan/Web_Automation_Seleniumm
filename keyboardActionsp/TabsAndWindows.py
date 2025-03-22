from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
#
# regilink = Keys.CONTROL+Keys.RETURN
# driver.find_element("link text","Register").send_keys(regilink)

# driver.switch_to.new_window('tab')

driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com")