import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class DemoImplicitWait():
    def demo_implicit_wait(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.ID,"username").send_keys("ramu")
        driver.find_element(By.ID, "password").send_keys("ram")

impwait=DemoImplicitWait()
impwait.demo_implicit_wait()











