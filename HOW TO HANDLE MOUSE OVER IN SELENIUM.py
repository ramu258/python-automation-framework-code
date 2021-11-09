import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class DemoMouseOver():
    def demo_mouse_events(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        morebutton=driver.find_element(By.XPATH,"//span[@class='more-arr']")
        myaccount_link= driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
        achains=ActionChains(driver)
        achains.move_to_element(myaccount_link).perform()
        time.sleep(3)
        achains = ActionChains(driver)
        achains.move_to_element(morebutton).perform()
        time.sleep(3)
        driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
        time.sleep(3)

dmouse=DemoMouseOver()
dmouse.demo_mouse_events()






