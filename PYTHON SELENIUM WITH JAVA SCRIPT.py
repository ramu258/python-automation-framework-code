import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
class DemoJs():
    def demo_JavaScript(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://training.rcvacademy.com/")






