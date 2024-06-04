from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com/investor/wallet')

#tile 01
my_investments_icon = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div[1]/p/i')
my_investment_heading = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div[2]/a')
no_of_units =  driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/a')
invested_amount_subheading= driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[1]/div/div/div[2]/div/span[1]')
invested_amount_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[1]/div/div/div[2]/div/div/p/span[1]')
shares_heading =  driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[1]/div/div/div[2]/div/span[2]')
shares_text =  driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[1]/div/div/div[2]/div/div/p/span[2]')
shares_text_arrow = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div[1]/div[1]/div/div/div[2]/div/div/p/span[2]/i')

#tile 02
estimated_sales_Profit_icon = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/p/i')
estimated_sales_profit_heading=   driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/a')
your_profit_by_total_profit_subheading =  driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[2]/div/div/div[2]/div/span[1]')
your_profit_by_total_profit_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[2]/div/div/div[2]/div/div/p/span')

#tile 03
sold_units_icon = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[3]/div/div/div[1]/div/div/div[1]/p/i')
sold_units_heading = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div[1]/div[3]/div/div/div[1]/div/div/div[2]/a')
sold_units_by_total_units_subheading = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div[1]/div[3]/div/div/div[2]/div/span[1]')
sold_units_by_total_units_text = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div[1]/div[3]/div/div/div[2]/div/div/p/span')

#tile 04
net_roi_icon = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div[1]/div[4]/div/div/div[1]/div/div/div[1]/p/i')
net_roi_heading = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div[1]/div[4]/div/div/div[1]/div/div/div[2]/a')
percentage_subheading = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div[1]/div[4]/div/div/div[2]/div/span[1]')
percentage_text = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div[1]/div[4]/div/div/div[2]/div/div/p')
percentage_text_arrow = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div/div/div[1]/div[4]/div/div/div[2]/div/div/p/span')


# order details table 
order_details_heading = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div/div/div[2]/div[1]/div/div/h4')
show_entries_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table_length"]/label')
show_entries_dropdown = driver.find_element(By.XPATH, '//*[@id="batch_details_table_length"]/label/select')
show_entries_info = driver.find_element(By.XPATH, '//*[@id="batch_details_table_info"]')
search_label = driver.find_element(By.XPATH, '//*[@id="batch_details_table_filter"]/label')
search_input = driver.find_element(By.XPATH, '//*[@id="batch_details_table_filter"]/label/input')
previous_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table_previous"]')
next_text =  driver.find_element(By.XPATH, '//*[@id="batch_details_table_next"]')
s_no_heading = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[1]')
order_id_heading = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[2]')
order_units_heading = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[3]')
selling_price_heading = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[4]')
selling_cost_heading = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[5]')
purchase_cost_headig = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[6]')
total_profit_heading = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[7]')
investor_gross_profit_heading =  driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[8]')
investsage_fee_heading = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[9]')
net_profit_heading = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[10]')
net_roi_heading = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[11]')
order_date_heading = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/thead/tr/th[12]')
s_no_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[1]')
order_id_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[2]')
order_units_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[3]')
selling_price_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[4]')
selling_cost_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[5]')
purchase_cost_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[6]')
total_profit_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[7]')
investor_gross_profit_text =  driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[8]')
investsage_fee_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[9]')
net_profit_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[10]')
net_roi_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[11]')
order_date_text = driver.find_element(By.XPATH, '//*[@id="batch_details_table"]/tbody/tr[1]/td[12]')


