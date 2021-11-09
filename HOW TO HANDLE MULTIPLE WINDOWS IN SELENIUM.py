import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class DemoMultipleWindows():
    def demo_windows(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent_handle=driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH,"//a[@title='Web Check-in']//img[@class='conta iner large-banner']").click()
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH,"//span[normalize-space()='Singapore Airlines']").click()
                time.sleep(4)
                driver.get("https://www.singaporeair.com/en_UK/plan-and-book/your-booking/checkin/")
                driver.find_element_by_xpath("//input[@id='last-name']").send_keys("ramu")
                time.sleep(4)
                driver.close()
                time.sleep(2)
                break
        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH,"//a[@title='Web Check-in']//img[@class='conta iner large-banner']").click()

dmultiplewindows=DemoMultipleWindows()
dmultiplewindows.demo_windows()





