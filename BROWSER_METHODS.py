import time
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
class DemoSeleniumLearning():
    def Demo_Browser_Methods(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://www.yatra.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.get("https://www.yatra.com/offer/dom/listing/domestic-flight-deals")
        driver.find_element_by_link_text('Bus').click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.minimize_window()
        time.sleep(4)
        driver.quit()
demobrowser=DemoSeleniumLearning()
demobrowser.Demo_Browser_Methods()
