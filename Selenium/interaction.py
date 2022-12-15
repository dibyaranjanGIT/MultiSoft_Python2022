from selenium import webdriver
from selenium.webdriver.common.keys import Keys

wiki_url = "https://en.wikipedia.org/wiki/Main_Page"

chrome_driver_path =  "D:\Softwares\SeleniumChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(wiki_url)
# result = driver.find_element_by_css_selector("#mp-otd a")

# result = driver.find_element_by_link_text("September 10")
# print(result.text)

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# result.click()

# driver.quit()