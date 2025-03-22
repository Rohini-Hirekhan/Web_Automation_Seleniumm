import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.find_element("xpath","//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(3)

# current_window_handle -> return windowID of single browser window
# window_handles -> return window ids of multiple browser window

# window_id = driver.current_window_handle
# print(window_id)
window_ids = driver.window_handles
# parentwindowid = window_ids[0]
# childwindowid = window_ids[1]
#
# print(parentwindowid,childwindowid)
# driver.switch_to.window(childwindowid)
# print("title of child window",driver.title)
# driver.switch_to.window(parentwindowid)
# print("title of parent window",driver.title)
# time.sleep(3)

for i in window_ids:
    driver.switch_to.window(i)
    print(driver.title)
    # if driver.title == 'Orange hRM'
