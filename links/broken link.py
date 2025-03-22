from selenium import webdriver
import requests

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")

alllinks=driver.find_elements("tag name","a")
count=0
print(len(alllinks))
for links in alllinks:
    url = links.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code >=400:
        print(url," is broken link")
        count+=1
    else:
        print(url,"  is valid link")
print("total no of broken links : ",count)


