from selenium import webdriver
from selenium.webdriver.common.keys import Keys

sign_page = "http://secure-retreat-92358.herokuapp.com/"

chrome_driver_path =  "D:\Softwares\SeleniumChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(sign_page)

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

first_name.send_keys("Dibyaranjan")
last_name.send_keys("Jena")
email.send_keys("dibyaranjanprm.51@gmail.com")

click_submit = driver.find_element_by_css_selector(".btn-primary")
click_submit.click()