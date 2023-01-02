## The cookie clicker gaem
# url = http://orteil.dashnet.org/experiments/cookie/

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(url)


cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 60*5   # 5 minutes from now
while True:
    if time.time() > timeout:
        break
    cookie.click()