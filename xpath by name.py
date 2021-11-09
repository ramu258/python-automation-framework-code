import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
class DemoFindElementtByIDandName():
    def locatee_by_demo(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_Name('login-input').send_keys('Ramu.0')
        time.sleep(20)
findbyid=DemoFindElementtByIDandName()
findbyid.locatee_by_demo()