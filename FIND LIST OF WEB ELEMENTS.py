import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
class DemoFindElementByXpath():
    def locate_by_xpath_demo(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://www.yatra.com/")
        count=driver.find_elements_by_tag_name('a')
        print(len(count))
        for i in count:
            print(i.text)
        time.sleep(4)
findbyxpath=DemoFindElementByXpath()
findbyxpath.locate_by_xpath_demo()