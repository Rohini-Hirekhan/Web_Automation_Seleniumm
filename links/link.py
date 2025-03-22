import time

from selenium import webdriver



driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
# driver.find_element("link text","Digital downloads").click()

# total no of link
web=driver.find_elements("tag name","a")
print(len(web))

print(len(driver.find_elements("xpath","//a")))
link = driver.find_elements("xpath","//a")
for i in link:
    print(i.text)
