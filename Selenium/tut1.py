from selenium import webdriver

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://www.amazon.com")


driver.close() # close closes a single active tab
# driver.quit() # quit closes the browser