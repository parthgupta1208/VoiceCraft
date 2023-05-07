
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome('C:/Everything/chromedriver.exe')
    driver.get('https://www.google.com/')
    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys('wikipedia')
    search_bar.send_keys(Keys.ENTER)
    first_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="r"]/a/h3')))
    first_result.click()
except NoSuchElementException:
    pass
