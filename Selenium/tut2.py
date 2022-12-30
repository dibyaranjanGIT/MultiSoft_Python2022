## Finding elements
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.in/Redmi-SonicBass-Wireless-Earphones-INLYEJ02LS/dp/B08S3B7J29?ref_=Oct_DLandingS_D_e77b7a93_60&th=1")

## delay added to give time for all elements to load

time.sleep(3)
documentation = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(f"The price is :$", documentation.text)

driver.quit()
