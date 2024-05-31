from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com')

# Locate an element using XPathc
login_title = driver.find_element(By.XPATH, "/html/body/div[2]/section/div/div/div[1]/div[2]/div/h4")
email_label = driver.find_element(By.XPATH, '//*[@id="user-login"]/div[1]/label')
email_input = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("myemail@example.com")
password_label = driver.find_element(By.XPATH,'//*[@id="user-login"]/div[2]/label')
password_input = driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("mypassword")
select_user_type_text = driver.find_element(By.XPATH,'//*[@id="user-login"]/div[3]/label')
investor_radio_button = driver.find_element(By.XPATH, '//*[@id="investor_radio"]')
investor_radio_button_title = driver.find_element(By.XPATH, '//*[@id="max_funding_limit_per_user"]/div[1]/label')
vendor_radio_button = driver.find_element(By.XPATH, '//*[@id="vendor_radio"]')
vendor_radio_button_title = driver.find_element(By.XPATH, '//*[@id="max_funding_limit_per_user"]/div[2]/label')
forgot_Password_link = driver.find_element(By.XPATH, '//*[@id="user-login"]/div[4]/a')
forgot_Password_icon= driver.find_element(By.XPATH,'//*[@id="user-login"]/div[4]/a/i')
lets_go_button= driver.find_element(By.XPATH,'//*[@id="user-login"]/button').click()
become_an_investor_button= driver.find_element(By.XPATH,'//*[@id="user-login"]/div[5]/a[2]')
become_a_vendor_button= driver.find_element(By.XPATH,'//*[@id="user-login"]/div[5]/a[1]')















