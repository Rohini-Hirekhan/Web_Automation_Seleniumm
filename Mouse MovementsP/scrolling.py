import time
from asyncio import timeout

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

#1) scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)","")
# check whether it is moved or not
value = driver.execute_script("return window.pageYOffset;")
print("no of pixels moved ",value)
time.sleep(3)

#2) scroll down till webelement is visible
# inspect element
flag = driver.find_element("xpath","//img[@alt='Flag of India']")
# execute scroll till that element
driver.execute_script("arguments[0].scrollIntoView();",flag)
value = driver.execute_script("return window.pageYOffset;")
print("no of pixels moved ",value)

# 3) scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("no of pixels moved ",value)

# 4) scroll up to starting page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("no of pixels moved ",value)




