import time

from selenium import webdriver



driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# 1) select all checkboxes
count=driver.find_elements("xpath","//input[@type= 'checkboxP' and contains(@id,'day')]")
# print(len(count)) #12

# 1st approach
# for i in count:
#     i.click()
# time.sleep(15)

# 2nd approach
# for i in range(len(count)):
#     count[i].click()
# time.sleep(15)

# selected particular option
# driver.find_element("xpath","//input[@id='sunday']").click()
# time.sleep(15)




# 2) select checkboxP on own choice
# - step1 - collect all checkboxP  then out of it select one which we want select
# checkboxes_value = driver.find_elements()
# for i in count:
#     weekname = i.get_attribute("id")
#     if weekname == 'monday':
#         i.click()
#


# 3) select last 4 checkboxes
n1=len(count)
# print(n1)
# for i in range(n1-2,n1): #range(5,7) -> 6,7
#     count[i].click()
# time.sleep(15)
#     if
# 4) select 1st 2 checkboxP
# for i in range(n1):
#     if i<2:
#         count[i].click()
# time.sleep(15)

# 5) clear all checkboxP
for i in count:
    i.click()
for i in count:
    if i.is_selected():
        i.click()
time.sleep(5)
# for i in range(6,7):
#     print(i)

