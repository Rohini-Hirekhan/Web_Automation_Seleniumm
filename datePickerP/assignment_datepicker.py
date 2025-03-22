# select all options from the form then validate selected payment is appeared or not
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
time.sleep(2)

# select radio btn option
# extract all data from table from that select column value extract it then compare

rd=driver.find_element("xpath","//input[@id='product_550']").click()
print(rd.text)
time.sleep(2)

total=driver.find_element("xpath","//table[@class='shop_table woocommerce-checkout-review-order-table']//tr//td[2]").text
if rd.text == total:
    print("total value is correct")
else:
    print("incorrect")

