from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com/investor/register')

# testing

join_investsage_title = driver.find_element(By.XPATH, '//*[@id="step1"]/div/h4')
full_name_label =  driver.find_element(By.XPATH, '//*[@id="form_step1"]/div[1]/div[1]/div/label') 
full_name_input = driver.find_element(By.XPATH,'//*[@id="name"]')
email_label = driver.find_element(By.XPATH,'//*[@id="form_step1"]/div[1]/div[2]/div/label')
email_input = driver.find_element(By.XPATH,'//*[@id="email"]')
password_label = driver.find_element(By.XPATH,'//*[@id="form_step1"]/div[1]/div[3]/div/label')
password_input =  driver.find_element(By.XPATH,'//*[@id="password"]')
confirm_password_label = driver.find_element(By.XPATH,'//*[@id="confirm-pass"]/label')
confirm_password_input = driver.find_element(By.XPATH,'//*[@id="confirm_password"]')
go_back_button = driver.find_element(By.XPATH,'//*[@id="form_step1"]/div[2]/a')
continue_to_next_step_button = driver.find_element(By.XPATH,'//*[@id="registerSubmit"]')

