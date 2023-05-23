
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome(executable_path='C:/Everything/chromedriver.exe')
    driver.get("https://www.youtube.com/")
    
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_bar.send_keys("programming videos")
    search_bar.submit()
    
    WebDriverWait(driver, 10).until(EC.title_contains("programming videos"))
    
except Exception as e:
    print(e)
finally:
    while len(driver.window_handles) > 0: pass
driver.quit()
