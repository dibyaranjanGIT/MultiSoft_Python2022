## How to interact using selenium
## How to type using the Keys class and click on the buttons

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(wiki_url)

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

result = driver.find_element(By.ID, "searchButton")
result.click()


driver.quit()