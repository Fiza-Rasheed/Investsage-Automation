from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com')

# Locate an element using XPathc
login_title = driver.find_element(By.XPATH, "/html/body/div[2]/section/div/div/div[1]/div[2]/div/h4")
email_label = driver.find_element(By.XPATH, '//*[@id="user-login"]/div[1]/label')
email_input = driver.find_element(By.XPATH, '//*[@id="email"]')










