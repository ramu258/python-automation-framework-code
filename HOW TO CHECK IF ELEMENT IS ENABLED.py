import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
class DemoElementState():
    def demo_enable_disable(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://training.openspan.com/login")
        demo_state=driver.find_element_by_xpath("//input[@id='login_button']").is_enabled()
        print(demo_state)
        driver.find_element_by_xpath("//input[@id='user_name']").send_keys("ramu")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='user_pass']").send_keys("ram12345")
        time.sleep(2)
        demo_state1=driver.find_element_by_xpath("//input[@id='login_button']").is_enabled()
        print(demo_state1)
demostate=DemoElementState()
demostate.demo_enable_disable()