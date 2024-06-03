from selenium import webdriver
from selenium.webdriver.common.by import By
# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com/support/ticket/list')



tickets_heading = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div/div/div[1]/div/div/h4')
create_ticket_button = driver.find_element(By.XPATH,'//html/body/div/div[2]/div/main/section/div[1]/div/div/div[1]/div/a')
search_label = driver.find_element(By.XPATH,'//*[@id="vendor_ticket_listing_filter"]/label')
search_input = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing_filter"]/label/input')
search_entries_label = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing_length"]/label')
search_entries_dropdown = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing_length"]/label/select')
s_no_heading = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[1]')
name_heading = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[2]')
ticket_no_heading= driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[3]')
email_heading =  driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[4]')
subject_heading = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[5]')
type_heading = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[6]')
entity_heading = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[7]')
priority_heading = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[8]')
status_heading = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[9]')
created_at_heading = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[10]')
action_heading = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing"]/thead/tr/th[11]')
previous_text = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing_previous"]')
next_text = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing_next"]')
showing_entries_info_text = driver.find_element(By.XPATH, '//*[@id="vendor_ticket_listing_info"]')
