# Find elements

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org")
time.sleep(2)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for time in event_times:
    print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for name in event_names:
    print(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "place": event_names[n].text
    }

print(events)

driver.quit()