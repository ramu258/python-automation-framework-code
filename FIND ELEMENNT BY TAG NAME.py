import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
class DemoFindElementByXpath():
    def locate_by_xpath_demo(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_class_name('email-login-box').send_keys('ram@ramu.com')
        time.sleep(4)
findbyxpath=DemoFindElementByXpath()
findbyxpath.locate_by_xpath_demo()