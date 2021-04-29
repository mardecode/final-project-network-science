# import selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opts = Options()
opts.add_argument("user-agent=Googlebot")


# options.binary_location = binary_location

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

driver = webdriver.Chrome(executable_path=driver_location, options=opts)
driver.get('https://www.tiktok.com/trending')

driver.add_cookie({"name": "s_v_web_id", "value": "verify_knzfhaj0_N7Id3rOa_aa2Z_4lmj_AZel_C7kgfcqjpiJe"})
  
print(driver.title)
time.sleep(2)



