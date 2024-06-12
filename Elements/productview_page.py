from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com/investor/register')


#finding xpath of elements 


#image section
batch_code_title = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/section/div[1]/div[1]/div[1]/div[1]/h2')
batch_code_icon = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[1]/div[1]/div[1]/h2/i')
batch_status_title = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[1]/div[1]/div[2]/p')
batch_status_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[1]/div[1]/div[2]/p/span')
batch_main_image = driver.find_element(By.XPATH,'//*[@id="carouselVertical"]/div/div[2]/div/div[2]/img')
batch_image1 = driver.find_element(By.XPATH,'//*[@id="carouselVertical"]/div/div[1]/div/button[1]/img')
batch_image2 = driver.find_element(By.XPATH,'//*[@id="carouselVertical"]/div/div[1]/div/button[2]/img')
batch_image3 = driver.find_element(By.XPATH,'//*[@id="carouselVertical"]/div/div[1]/div/button[3]/img')
batch_image_next_arrow= driver.find_element(By.XPATH,'//*[@id="carouselVertical"]/div/div[1]/button[1]/i')
batch_image_previous_arrow = driver.find_element(By.XPATH,'//*[@id="carouselVertical"]/div/div[1]/button[2]/i')

#investment amount section 
investment_amount_title = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/h2/i')
investment_amount_icon = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/h2')
required_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/div[1]/div[1]/span')
required_amount_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/div[1]/div[1]/p')
funded_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/div[1]/div[2]/span')
funded_amount_text= driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/div[1]/div[2]/p')
progress_bar = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/div[2]')
complete_percentage_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/div[3]/div[1]')
no_of_available_units_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/div[3]/div[2]')
no_of_investments_text= driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/div[4]/div[1]')
days_left_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/div[4]/div[2]')
days_left_clock_icon = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[1]/div/div[4]/div[2]/i')

#batch and product details  section
batch_and_product_details_title = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/h3')
batch_and_product_details_icon = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/h3/i')
batch_code_title = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[1]/th')
batch_code_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[1]/td')
investment_required_title = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/th')
investment_required_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td')
batch_quantity_title = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[3]/th')
batch_quantity_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[3]/td')
product_title_title = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[3]/td')
product_title_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[4]/td')
purchase_price_title = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[5]/th')
purchase_price_text = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[5]/td')
selling_price_title = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[6]/th')
min_selling_price = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[6]/td[1]')
max_selling_price = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/main/section/div[1]/div[2]/div[2]/div/table/tbody/tr[6]/td[2]')
avg_selling_price = driver.find_element(By.XPATH,'')
cost_of_selling_title = driver.find_element(By.XPATH,'')
cost_of_Selling_tooltip = driver.find_element(By.XPATH,'')
cost_of_selling_text = driver.find_element(By.XPATH,'')

#wallet section
wallet_title = driver.find_element(By.XPATH,'')
wallet_icon = driver.find_element(By.XPATH,'')
balance_text = driver.find_element(By.XPATH,'')
payment_info_title = driver.find_element(By.XPATH,'')
quantity_label = driver.find_element(By.XPATH,'')
quantity_input_field= driver.find_element(By.XPATH,'')
invest_now_button = driver.find_element(By.XPATH,'')
quantity_input_no_of_units= driver.find_element(By.XPATH,'')
quantity_minus_button = driver.find_element(By.XPATH,'')
quantity_plus_button = driver.find_element(By.XPATH,'')
quantity_units_text = driver.find_element(By.XPATH,'')
investment_amount_input = driver.find_element(By.XPATH,'')
investment_amount_GBPsign = driver.find_element(By.XPATH,'')

#product overview



#product statistics
product_statistics_tab = driver.find_element(By.XPATH,'')
quartely_gross_profit_title = driver.find_element(By.XPATH,'')
quartely_gross_profit_icon = driver.find_element(By.XPATH,'')
quartely_gross_profit_para = driver.find_element(By.XPATH,'')
quartely_gross_profit_amount = driver.find_element(By.XPATH,'')
quartely_sold_title = driver.find_element(By.XPATH,'')
quartely_sold_icon = driver.find_element(By.XPATH,'')
quartely_sold_para = driver.find_element(By.XPATH,'')
quartely_sold_units = driver.find_element(By.XPATH,'')
daily_consumptions_title = driver.find_element(By.XPATH,'')
daily_consumptions_icon = driver.find_element(By.XPATH,'')
daily_consumptions_para = driver.find_element(By.XPATH,'')
daily_consumptions_units = driver.find_element(By.XPATH,'')
average_selling_price_title = driver.find_element(By.XPATH,'')
average_selling_price_icon = driver.find_element(By.XPATH,'')
average_selling_price_para = driver.find_element(By.XPATH,'')
average_selling_price_amount = driver.find_element(By.XPATH,'')

#financial calculator 
financial_calculator_tab = driver.find_element(By.XPATH,'')
investment_calculator_heading = driver.find_element(By.XPATH,'')
batch_investment_subheading = driver.find_element(By.XPATH,'')
financials_heading = driver.find_element(By.XPATH,'')
selling_price_range_subheading = driver.find_element(By.XPATH,'')
selling_price_progress_bar = driver.find_element(By.XPATH,'')
min_selling_price = driver.find_element(By.XPATH,'')
max_selling_price = driver.find_element(By.XPATH,'')
number_of_units_subheading = driver.find_element(By.XPATH,'')
min_units = driver.find_element(By.XPATH,'')
max_units = driver.find_element(By.XPATH,'')







