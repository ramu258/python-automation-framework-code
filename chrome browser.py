import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="G:\\SELENIUM\\BWOSERS\\chromedriver.exe")
driver.get("https://www.amazon.com")
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").click()
time.sleep(4)
print(driver.title)

