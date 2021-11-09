import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
class DemoFindElementByCssSelector():
    def locate_by_cssselector_demo(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://www.amazon.in/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles_9292c6cb7b394d30b2467b8f631090a7")
        driver.find_element_by_css_selector("#twotabsearchtextbox']").send_keys('test@test.com')
        time.sleep(4)
findbyxpath=DemoFindElementByCssSelector()
findbyxpath.locate_by_cssselector_demo()