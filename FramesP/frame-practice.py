from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.find_element("link text","org.openqa.selenium").click()