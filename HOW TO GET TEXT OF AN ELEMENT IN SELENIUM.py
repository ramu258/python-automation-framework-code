import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
class DemoGetText():
    def demo_gettext(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://www.yatra.com/")
        text=driver.find_element_by_xpath("//p[normalize-space()='Germany']").text
        text1=driver.find_element_by_link_text('Yatra for Business').text
        print(text1)
        time.sleep(2)
findbyxpath=DemoGetText()
findbyxpath.demo_gettext()