import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Alert - we have to inspect element of pop up then we can perform action on it
# Actions can be performed on pop up- 1)capture text 2)enter value 3)ok or cancel

driver.find_element("xpath","//button[text()='Click for JS Prompt']").click()
# switch to alert and access pop up with the help of created object
alert_win = driver.switch_to.alert
# print text on pop up
print(alert_win.text)
# enter a value on popup
alert_win.send_keys("love u")

# click on ok
# alert_win.accept()

# click on cancel button
alert_win.dismiss()

time.sleep(5)

