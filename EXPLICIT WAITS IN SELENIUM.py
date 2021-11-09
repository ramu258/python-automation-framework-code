import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
class DemoExplicitWait():
    def demo_explicit_wait(self):
        driver=webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
        wait = WebDriverWait(driver,10)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        depart_from= driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        going_to = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("New York")
        search_results = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for results in search_results:
            print(results.text)
            if "New York(JFK)" in results.text:
                results.click()
                break
        wait = WebDriverWait(driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_date']"))).click()
        origin = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        origin.click()
        driver.find_element(By.XPATH,"//td[@id='08/07/2021']").click()
        all_dates= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))\
            .find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        all_dates = driver.find_element(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "22/08/2021":
                date.click()
                break
        driver.find_element(By.XPATH,"//input[@value='Search Flights']").click()

dauto=DemoExplicitWait()
dauto.demo_explicit_wait()













