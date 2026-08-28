from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

url = "https://quotes.toscrape.com/js-delayed/"
driver.implicitly_wait(2)
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))
sleep(2)
quotes = driver.find_elements(By.CSS_SELECTOR, "div.quote")
print(len(quotes))