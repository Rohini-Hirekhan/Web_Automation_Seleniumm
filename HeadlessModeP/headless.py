from selenium import webdriver




def headless_chrome():
    driver = webdriver.Chrome()
    ops = webdriver.ChromeOptions()
    ops.headless = True
    return driver

def headless_Edge():
    driver = webdriver.Edge()
    ops = webdriver.EdgeOptions()
    ops.headless = True
    return driver


def headless_Firefox():
    driver = webdriver.Firefox()
    ops = webdriver.FirefoxOptions()
    ops.headless = True
    return driver

driver = headless_chrome()
# driver= headless_Edge()
# driver = headless_Firefox()

driver.get("https://demo.nopcommerce.com/")
print(driver.current_url)
print(driver.title)