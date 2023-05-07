
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome('C:/Everything/chromedriver.exe')
    driver.get("https://www.youtube.com/")
    driver.maximize_window()

    search_textbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_textbox.send_keys("python programming")
    search_textbox.submit()

    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a#video-title"))
    )
    first_video.click()
    
    like_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#top-level-buttons ytd-toggle-button-renderer.style-scope:nth-of-type(1)"))
    )
    like_button.click()

except Exception as e:
    print(e)

finally:
    while len(driver.window_handles) > 0: pass
driver.quit()
