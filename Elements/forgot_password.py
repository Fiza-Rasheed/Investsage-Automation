from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com/password/reset')

# Locate an element using XPathc
forgot_password_title = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
forgot_password_text = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/p')
email_label = driver.find_element(By.XPATH,'/html/body/div[2]/section/div/div/div[1]/form/div[1]/label')
email_input= driver.find_element(By.XPATH,'//*[@id="email"]')
select_user_type_text= driver.find_element(By.XPATH,'/html/body/div[2]/section/div/div/div[1]/form/div[2]/label')
investor_radio_button = driver.find_element(By.XPATH, '//*[@id="investor_radio"]')
investor_radio_button_title = driver.find_element(By.XPATH, '//*[@id="max_funding_limit_per_user"]/div[1]/label')
vendor_radio_button = driver.find_element(By.XPATH, '//*[@id="vendor_radio"]')
vendor_radio_button_title = driver.find_element(By.XPATH, '//*[@id="max_funding_limit_per_user"]/div[2]/label')
submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/form/div[3]/button')
go_back_button = driver.find_element(By.XPATH,'/html/body/div[2]/section/div/div/div[1]/form/div[3]/a')


