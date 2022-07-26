from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=chrome_options)
# driver = webdriver.Chrome(path)

driver.get("https://www.chessbazaar.com/admin_kVRLsI/")
# print(driver.title)

search = driver.find_element_by_id("username")
search.send_keys("arjun")
search = driver.find_element_by_id("login")
search.send_keys('arjun@1234')
print("dang dang nhap magento")
search.send_keys(Keys.RETURN)
product_list = [2001,2086,2452,2467,2663,2785,2786,2787,2838,2839,2840,2862,2879,2888,2896,2916,2922,2923,2924,2947,3011,3030,3149,3151,3198,3201,3205,3218,3757,3776,3779]
# url = "https://excelstaging1.net/admin/catalog/product/edit/id/{product_id}/key/48a4ca88951f7443aa8602d6c5c15d40eb538a488071f484dca20a2e86687433/type/simple/store/1/back/edit/"# print(url)
# driver.get(url)
# search = driver.find_element_by_id("save-button")
# print(search.text)
dont_save_list = list()
flag = 0
lens = len(product_list)
for product_id in product_list:
    url = f"https://www.chessbazaar.com/admin_kVRLsI/catalog/product/edit/id/{product_id}/key/7847c77ee97143dc863aa9ee95a2fed2bf272296fb2b724e01caa3fdccc322f9/"
    print(product_id)
    driver.get(url)
    search = driver.find_element_by_id("save-button")
    search.send_keys(Keys.RETURN)
    print("sleeping 10s....")
    print(f"saving: {product_id}")
    flag += 1
    print(f"{flag}/{lens}")
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "message")))
    except:
        print(f"khong save duoc: {product_id}")
        dont_save_list.append(product_id)
    else:
        print(f"da save: {product_id}")
    finally:
        print("het 10s")

print(dont_save_list)   
driver.close()