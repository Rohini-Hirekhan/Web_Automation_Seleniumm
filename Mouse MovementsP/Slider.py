from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
# inspect slider element
min = driver.find_element("xpath","//body//div//span[1]")
max = driver.find_element("xpath","//body//div//span[2]")

# find location of that webelement
print(min.location)
print(max.location)

# perform action by using actionchains obj method - drag_and_drop_by_offset(webelement,x-offset,y-offset).perform()
act = ActionChains(driver)
act.drag_and_drop_by_offset(min,100,0).perform()
act.drag_and_drop_by_offset(max,-60,0).perform()

# print webelements location
print(min.location)
print(max.location)




