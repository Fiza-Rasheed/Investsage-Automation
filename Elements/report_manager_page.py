from selenium import webdriver
from selenium.webdriver.common.by import By
# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com/investor/report')

reports_manager_title = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/main/section/div/div/div[1]/div[1]/div/div/h4')
report_type_label = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/main/section/div/div/div[1]/div[2]/div[1]/div/div/label')
report_type_dropdown= driver.find_element(By.XPATH,'//*[@id="select2-report_type-container"]')
report_type_dropdown_input = driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
please_select_dropdown_option = driver.find_element(By.XPATH,'//*[@id="select2-report_type-result-zvll-0"]')
investment_details_dropdown_option = driver.find_element(By.XPATH,'//*[@id="select2-report_type-result-ftvo-investment_detail_report"]')
report_type_dropdown_arrow = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/main/section/div/div/div[1]/div[2]/div[1]/div/div/div/span/span[1]/span/span[2]')
date_range_label = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/main/section/div/div/div[1]/div[2]/div[2]/div[1]/div/label')
date_range_dropdown = driver.find_element(By.XPATH,'//*[@id="report-date-filter"]')
date_range_dropdown_arrow = driver.find_element(By.XPATH,'//*[@id="report-date-filter"]/i')
date_range_dropdown_calendar_icon = driver.find_element(By.XPATH,'//*[@id="report-date-filter"]/span/i')
date_range_dropdown_daterangepicker_text = driver.find_element(By.XPATH,'//*[@id="report-date-filter"]/span')
date_range_dropdown_today_option = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[1]')
date_range_dropdown_yesterday_option = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[2]')
date_range_dropdown_last7days_option = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[3]')
date_range_dropdown_last30days_option = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[4]')
date_range_dropdown_thismonth_option = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[5]')
date_range_dropdown_lastmonth_option = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[6]')
date_range_dropdown_customrange_option = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[7]')
apply_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/button[1]')
cancel_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/button[2]')
keyword_label =  driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/main/section/div/div/div[1]/div[2]/div[2]/div[2]/div/label')
keyword_input = driver.find_element(By.XPATH,'//*[@id="search-keyword"]')
keyword_info_text = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/main/section/div/div/div[1]/div[2]/div[2]/div[2]/div/div/span')
generate_report_button = driver.find_element(By.XPATH,'//*[@id="generate_report"]')



