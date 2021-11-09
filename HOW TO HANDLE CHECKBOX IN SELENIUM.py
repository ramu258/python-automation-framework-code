import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
class DemoCheckBoxes():
    def demo_checkbox(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        driver.find_element_by_id('interest_market_c0').click()
        time.sleep(4)
        var1=driver.find_element_by_id("interest_market_c0").is_selected()
        print(var1)
        var2=driver.find_element_by_id("interest_sell_c0").is_selected()
        print(var2)
checkbox=DemoCheckBoxes()
checkbox.demo_checkbox()