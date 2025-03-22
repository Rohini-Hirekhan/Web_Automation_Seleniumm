import time

from openpyxl.styles.builtins import title
from selenium import webdriver
import openpyxl
from Data_Driven_Testing import XLUtils
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
file = "C:\\POC\\ddt.xlsx"
rows=XLUtils.getRowCount(file,"Sheet1")
# print(rows)

for r in range(2,rows+1):
    # reading data from excel
    principle=XLUtils.ReadData(file,"Sheet1",r,1)
    roi=XLUtils.ReadData(file, "Sheet1", r, 2)
    per1=XLUtils.ReadData(file, "Sheet1", r, 3)
    per2=XLUtils.ReadData(file, "Sheet1", r, 4)
    fre = XLUtils.ReadData(file, "Sheet1", r, 5)
    exp_mvalue = XLUtils.ReadData(file, "Sheet1", r, 6)
#   passing data to the application
    driver.find_element("xpath","//input[@id='principal']").send_keys(principle)
    driver.find_element("xpath","//input[@id='interest']").send_keys(roi)
    driver.find_element("xpath","//input[@id='tenure']").send_keys(per1)
    obj1=Select(driver.find_element("xpath","//select[@id='tenurePeriod']"))
    obj1.select_by_visible_text(per2)
    obj2 = Select(driver.find_element("xpath","//select[@id='frequency']"))
    obj2.select_by_visible_text(fre)
    time.sleep(3)
    overlay =driver.find_element("xpath","//div[@class='cal_div']//a[1]//img")
    driver.execute_script("arguments[0].click();", overlay)
    time.sleep(3)

    ActValue=driver.find_element("xpath","//span[@id='resp_matval']//strong").text


    time.sleep(3)
#  Validation

    if float(exp_mvalue) == float(ActValue):
        print("test passed")
        XLUtils.WriteData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        XLUtils.WriteData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)

    overlay1=driver.find_element("xpath","//*[@id='fdMatVal']/div[2]/a[2]")
    driver.execute_script("arguments[0].click();", overlay1)




