from selenium import webdriver

chrome_driver_path =  "D:\Softwares\SeleniumChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)



# driver.get("https://www.python.org/")
# documentation = driver.find_element_by_xpath("//*[@id=\"content\"]/div/section/div[1]/div[3]/p[2]/a")
# print(documentation.text)


# driver.get("https://www.amazon.in/dp/B084DWH53T/?pf_rd_r=ZX2BQ986893ZKDB3D6XH&pf_rd_p=3f4c7aa2-7c34-4a02-9cbf-841867ff4b8d&pd_rd_r=cab03f4d-50c8-4c98-8145-145b8ff267b4&pd_rd_w=7vTUT&pd_rd_wg=I0rlO&ref_=pd_gw_unk")
# documentation = driver.find_element_by_xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]')
# print(documentation.text)

#driver.close()
driver.quit()

