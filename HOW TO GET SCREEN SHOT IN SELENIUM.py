import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdrivermanager.chrome import ChromeDriverManager
class DemoScreenShot():
    def demo_screen_capture(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        continuedemo = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        continuedemo.screenshot(".\\test.png")
        continuedemo.click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\PYTHON-SELENIUM\\error.png")
        driver.save_screenshot(".test\\test1.png")

ddscrenshot=DemoScreenShot()
ddscrenshot.demo_screen_capture()





