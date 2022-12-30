## Find element by name
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org")

search_bar = driver.find_element(By.NAME, "q")

bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


driver.quit()