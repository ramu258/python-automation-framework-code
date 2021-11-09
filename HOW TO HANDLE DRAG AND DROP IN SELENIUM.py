import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class DemoDragDrop():
    def demo_drag_drop(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        ele1 = driver.find_element(By.ID,"draggable")
        ele2 = driver.find_element(By.ID,"droppable")
        # ActionChains(driver).drag_and_drop(ele1,ele2).perform()
        ActionChains(driver).drag_and_drop_by_offset(ele1,100,80).perform()
        time.sleep(6)

dd=DemoDragDrop()
dd.demo_drag_drop()










