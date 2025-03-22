from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)
# driver.find_element("xpath","//input[@id='datepicker']").send_keys("05/30.2022")

# select expected date from date picker

year = " 2025"
month = "07"
date = "16"

# capture current month and year
driver.find_element("xpath","//input[@id='datepicker']").click()

while True:
   mon = driver.find_element("xpath","//span[@class='ui-datepicker-month']").text
   yr = driver.find_element("xpath","//span[@class='ui-datepicker-year']").text

   if mon == month and yr == year:
       break;

   else:
       driver.find_element("xpath","//a[@title='Next']").click() #next arrow
       driver.find_element("xpath","").click() #pre arrow

# select date
dates = driver.find_elements("xpath","//div[@id='ui-datepicker-div'//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break