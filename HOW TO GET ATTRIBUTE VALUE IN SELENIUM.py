import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
class DemoGetAttributeValue():
    def demo_getvalue(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://www.yatra.com/")
        attr_value=driver.find_element_by_xpath("//input[@id='BE_flight_origin_city']").get_attribute("id")
        print(attr_value)
        time.sleep(2)
attrobj=DemoGetAttributeValue()
attrobj.demo_getvalue()