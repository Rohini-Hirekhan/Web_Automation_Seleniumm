from selenium import webdriver

driver = webdriver.Chrome()

#1)  count no of rows and column
driver.get("https://testautomationpractice.blogspot.com/")
# rows = driver.find_elements("xpath","//table[@name = 'BookTable']//tr")
# rows=len(rows)
# print("number of rows present : ",rows)
#
# columns = driver.find_elements("xpath","//table[@name = 'BookTable']//tr[1]//th")
# columns = len(columns)
# print("number of columns present: ",columns)


#2)  read specific row and column data
# i=driver.find_element("xpath","//table[@name = 'BookTable']//tr[5]//td[1]")
# print(i.text)#Master In Selenium

#3) read all the rows and all the columns data
rows = driver.find_elements("xpath","//table[@name = 'BookTable']//tr")
rows=len(rows)
columns = driver.find_elements("xpath","//table[@name = 'BookTable']//tr[1]//th")
columns = len(columns)
# for i in rows:
#     for j in columns:
#         print(j.text, end = "                 ")
#     print()
#
# for r in range(2,rows+1):
#     for c in range(1,columns+1):
#         data = driver.find_element("xpath", "//table[@name ='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end = "                       ")
#     print()

# 4) read data based on conditions(list books name whose author is Mukesh)
# here changing only rows and selecting column wise data so only td is changed


for r in range(2,rows+1):
        author = driver.find_element("xpath", "//table[@name = 'BookTable']//tr[" + str(r) + "]/td[2]").text
        if author == "Mukesh":
            BookName = driver.find_element("xpath", "//table[@name = 'BookTable']//tr[" + str(r) + "]/td[1]").text
            priceName = driver.find_element("xpath", "//table[@name = 'BookTable']//tr[" + str(r) + "]/td[4]").text
            print(BookName,"   ",author,"     ",priceName)



# for i in author:
#     if i.text == "Mukesh":
#         print(i.text)
#
#











# read specific row and column
# read all the rows and colm data
# read data based on conditions