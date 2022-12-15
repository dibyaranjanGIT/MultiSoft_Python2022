from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path =  "D:\Softwares\SeleniumChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url)

cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 60*5   # 5 minutes from now
while True:
    test = 0
    if test == 5 or time.time() > timeout:
        break
    test = test - 1
    cookie.click()