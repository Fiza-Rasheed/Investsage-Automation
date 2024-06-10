from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com/investor/register')


#personal info section
personal_info_tab = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div/ul/li[1]/a')
personal_info_title =  driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/h5')
personal_info_icon =  driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/h5/i')
full_name_label =  driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[1]/div[1]/div/label')
full_name_input =   driver.find_element(By.XPATH, '//*[@id="user_name"]')
email_label =  driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[2]/div/div/label')
email_input =  driver.find_element(By.XPATH, '//*[@id="email"]')
mobile_number_label =   driver.find_element(By.XPATH, '//*[@id="user_name"]')
mobile_number_dropdown =   driver.find_element(By.XPATH, '//*[@id="select2-countrySelect-container"]')
mobile_number_dropdown_arrow =  driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[1]/div[2]/div/div/div[1]/span/span[1]/span/span[2]')
mobile_number_dropdown_flag =  driver.find_element(By.XPATH, '//*[@id="select2-countrySelect-container"]/span/i')
mobile_number_dropdown_text =  driver.find_element(By.XPATH, '//*[@id="select2-countrySelect-container"]/span')
mobile_number_input =   driver.find_element(By.XPATH, '//*[@id="mobile_no"]')
what_is_your_employment_status_label = driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[3]/div[1]/div[2]/label')
what_is_your_employment_status_dropdown =   driver.find_element(By.XPATH, '//*[@id="employment_status"]')
please_select_employment_status_option = driver.find_element(By.XPATH, '//*[@id="employment_status"]/option[1]')
employed_employment_status_option =  driver.find_element(By.XPATH, '//*[@id="employment_status"]/option[2]')
self_employed_employment_status_option =  driver.find_element(By.XPATH, '//*[@id="employment_status"]/option[3]')
student_employment_status_option =   driver.find_element(By.XPATH, '//*[@id="employment_status"]/option[4]')
homemaker_employment_status_option =  driver.find_element(By.XPATH, '//*[@id="employment_status"]/option[5]')
retired_employment_status_option =  driver.find_element(By.XPATH, '//*[@id="employment_status"]/option[6]')
wealth_source_dropdown_label  =  driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[3]/div[2]/div[3]/label')
wealth_source_dropdown_input = driver.find_element(By.XPATH, '//*[@id="wealth_source"]')
select_option_wealth_source_dropdown_option = driver.find_element(By.XPATH, '//*[@id="wealth_source"]/option[1]')
savings_from_employment_earnings_option =   driver.find_element(By.XPATH, '//*[@id="wealth_source"]/option[2]')
investments_wealth_source_option =  driver.find_element(By.XPATH, '//*[@id="wealth_source"]/option[3]')
winnings_wealth_source_option =  driver.find_element(By.XPATH, '//*[@id="wealth_source"]/option[4]')
inheritance_wealth_source_option =   driver.find_element(By.XPATH, '//*[@id="wealth_source"]/option[5]')
what_is_your_employers_name_label =  driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[3]/div[2]/div[1]/label')
what_is_your_employers_name_input =  driver.find_element(By.XPATH, '//*[@id="employer_name"]')
what_is_your_employers_address_label =  driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[3]/div[1]/div[2]/label')
what_is_your_employers_address_input =  driver.find_element(By.XPATH, '//*[@id="employer_address"]')
country_of_employment_dropdown_label =  driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[3]/div[2]/div[2]/label')
country_of_employment_dropdown_input =   driver.find_element(By.XPATH, '//*[@id="country_of_employment"]')
what_is_your_job_title_label =  driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[3]/div[1]/div[3]/label')
what_is_your_job_title_input =  driver.find_element(By.XPATH, '//*[@id="jobtitle"]')
what_is_your_employment_industry_dropdown_label =   driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[3]/div[1]/div[4]/label')
what_is_your_employment_industry_dropdown_input =  driver.find_element(By.XPATH, '//*[@id="employment_industry"]')
save_button = driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[4]/button')
save_button_icon = driver.find_element(By.XPATH, '//*[@id="personal-details-form"]/div[4]/button/i')






#change password tab
change_password_tab = driver.find_element(By.XPATH, '//*[@id="mp_new_password"]')
change_password_title = driver.find_element(By.XPATH, '//*[@id="change-password"]/h5')
change_password_icon = driver.find_element(By.XPATH, '//*[@id="change-password"]/h5/i')
old_password_label = driver.find_element(By.XPATH, '//*[@id="change-password"]/div[1]/div/div/label')
old_password_input = driver.find_element(By.XPATH, '//*[@id="old-password"]')
new_password_label = driver.find_element(By.XPATH, '//*[@id="change-password"]/div[2]/div[1]/div/label')
new_password_input =  driver.find_element(By.XPATH, '//*[@id="password"]')
re_type_password_label = driver.find_element(By.XPATH, '//*[@id="confirm-pass"]/label')
re_type_password_input =  driver.find_element(By.XPATH, '//*[@id="password"]')
save_button = driver.find_element(By.XPATH, '//*[@id="change-password"]/div[3]/button')
save_button_icon = driver.find_element(By.XPATH, '//*[@id="change-password"]/div[3]/button/i')


#bank details tab
bank_details_tab = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div/ul/li[3]/a')
bank_details_title = driver.find_element(By.XPATH, '//*[@id="bank-details-form"]/h5')
bank_details_icon = driver.find_element(By.XPATH, '//*[@id="bank-details-form"]/h5/i')
bank_name_label = driver.find_element(By.XPATH, '//*[@id="bank-details-form"]/div/div[1]/div/label')
bank_name_input = driver.find_element(By.XPATH, '//*[@id="bank-name"]')
sort_code_label = driver.find_element(By.XPATH, '//*[@id="bank-details-form"]/div/div[2]/div/label')
sort_code_input = driver.find_element(By.XPATH, '//*[@id="routing_number"]')
account_title_label = driver.find_element(By.XPATH, '//*[@id="bank-details-form"]/div/div[3]/div[1]/div/label')
account_title_input = driver.find_element(By.XPATH, '//*[@id="account_title"]')
iban_label =  driver.find_element(By.XPATH, '//*[@id="bank-details-form"]/div/div[3]/div[2]/div/label')
iban_input = driver.find_element(By.XPATH, '//*[@id="account_number"]')
save_button_icon = driver.find_element(By.XPATH, '//*[@id="bank-details-form"]/div/div[4]/button/i')
save_button =  driver.find_element(By.XPATH, '//*[@id="bank-details-form"]/div/div[4]/button')