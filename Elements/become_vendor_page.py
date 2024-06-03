from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com/vendor/register')

join_investsage_title = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
full_name_label = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
full_name_input = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
email_label = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
email_input = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
phone_number_label = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
phone_number_dropdown = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
phone_number_input =  driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
password_label = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
password_input = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
retype_password_label = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
retype_password_input = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
go_back_button = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')
lets_go_button = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div[1]/div[2]/h1')


