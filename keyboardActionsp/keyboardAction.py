from selenium import webdriver
from selenium.webdriver import ActionChains,Keys

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")

input1 = driver.find_element("xpath","//textarea[@id='inputText1']")
input2 = driver.find_element("xpath","//textarea[@id='inputText2']")


input1.send_keys("welcome to selenium")
act = ActionChains(driver)

# input1 --->cntr+A select the text
# act.key_down(Keys.CONTROL)
# act.send_keys('a')
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_down(Keys.CONTROL).perform()

# input1  -> cntr+c
# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform()


act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# press tab key navigate to 2nd input2
# act.send_keys(Keys.TAB)
# act.perform()

act.send_keys(Keys.TAB).perform()


# input2 -> cntr+v
# act.key_down(Keys.CONTROL)
# act.send_keys("v")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

