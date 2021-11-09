from selenium import webdriver
driver = webdriver.Opera(executable_path="G:\\SELENIUM\\BWOSERS\\operadriver_win64\\operadriver.exe")
driver.get("https://www.amazon.com")
driver.maximize_window()
print(driver.title)

