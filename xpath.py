import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
class DemoFindElementtByID():
    def locatee_by_demo(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_id('login-input').send_keys('ramu@ram.com')
        time.sleep(4)
findbyid=DemoFindElementtByID()
findbyid.locatee_by_demo()