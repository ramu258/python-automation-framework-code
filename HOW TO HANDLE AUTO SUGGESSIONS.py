import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
class DemoAutoSuggest():
    def demo_auto_suggest(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        driver.get("https://www.yatra.com/")
        depart_from= driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(4)
        going_to = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        search_results=driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for results in search_results:
            print(results.text)
            if "New York(JFK)" in results.text:
                results.click()
                time.sleep(4)
                break

dauto=DemoAutoSuggest()
dauto.demo_auto_suggest()








