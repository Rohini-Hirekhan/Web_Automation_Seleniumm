from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# capture cookies from the browser
cookies = driver.get_cookies()
print("size of cookies : ",len(cookies))

# print details of all cookies
# for i in cookies:
    # print(i)
    # print(i.get('name'),":",i.get('value'))

# add new cookie to the browser
driver.add_cookie({"name":"MyCookie","value":"123456"})
cookies = driver.get_cookies()
print("size of cookie after adding new one : ",len(cookies))

# delete specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("size of cookie after deleted one : ",len(cookies))

# delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("size of cookie after deleted all : ",len(cookies))