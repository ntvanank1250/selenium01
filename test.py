from selenium import webdriver 
import time 
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=chrome_options)
driver.get("http://www.baidu.com") 
print(driver.title) 
driver.find_element_by_id("kw").send_keys("selenium") 
driver.find_element_by_id("su").click() 
time.sleep(3) 
driver.close()

