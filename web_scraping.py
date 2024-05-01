from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Find the search box element
search_box = driver.find_element(By.NAME,"q")

class_name= "mnr-c c3mZkd pla-unit"
# Input your search query
search_query = "MACBOOK"
search_box.send_keys(search_query)
# Press Enter to perform the search
search_box.send_keys(Keys.RETURN)

main = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "main"))
)

time.sleep(2)
print(main.text)
panels=main.find_elements(By.CLASS_NAME,'mnr-c.c3mZkd.pla-unit')
print(panels)
print("INFO....")
for panel in panels:
    print("PANEL")
    print(panel.text)
    break

time.sleep(10)

driver.quit()


