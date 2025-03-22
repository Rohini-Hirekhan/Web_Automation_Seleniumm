import time
from ftplib import ftpcp
from os import times
import os
from requests import options
from selenium import webdriver


location= os.getcwd()



def chrome_setup():

    # download files in desired location
    preferences ={"download.default_directory",location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome()
    return driver



driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element("xpath","//tbody/tr[1]/td[5]/a[1]").click()

time.sleep(4)

