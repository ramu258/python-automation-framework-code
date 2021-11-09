import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class DemoSliders():
    def demo_sliders(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://www.snapdeal.com/products/mobiles-cases-covers?q=Occasion_s%3ANewlaunch%7CPrice%3A229%2C345%7C&sort=plrty")
        driver.maximize_window()
        # ele1=driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
        ele2 = driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
        # METHOD 1 LEFT HAND SIDE MOVING
        # ActionChains(driver).drag_and_drop_by_offset(ele1,60,0).perform()
        # METHOD 2 LEFT HAND SIDE MOVING
        #ActionChains(driver).click_and_hold(ele1).pause(1).move_by_offset(50,0).release().perform()
        # METHOD 1 RIGHT HAND SIDE MOVING
        # ActionChains(driver).drag_and_drop_by_offset(ele2,-60,0).perform()
        # METHOD 2 RIGHT HAND SIDE MOVING
        ActionChains(driver).click_and_hold(ele2).pause(1).move_by_offset(-50,0).release().perform()


        time.sleep(4)

dslider = DemoSliders()
dslider.demo_sliders()








