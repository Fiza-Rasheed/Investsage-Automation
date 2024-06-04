from selenium import webdriver
from selenium.webdriver.common.by import By
# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://investsage.com/investor/product')

products_title = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/main/div[1]/div/div/h4')
available_button = driver.find_element(By.XPATH, '//*[@id="available-tab"]')
upcoming_button = driver.find_element(By.XPATH, '//*[@id="upcoming-tab"]')
funded_button = driver.find_element(By.XPATH,'//*[@id="funded-tab"]')
exited_button = driver.find_element(By.XPATH,'//*[@id="exited-tab"]')

#available tab, Upcoming tab and Funded tab
code_heading =driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[1]')
code_text = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[1]/span')
gbp_amount_text = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[1]')
percent_funded_text = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]')
progress_bar = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[3]')
batch_code_title = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[1]/span[1]')
batch_code_text = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[1]/span[2]')
funding_start_date_title = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[2]/span[1]')
funding_start_date_text =driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[2]/span[2]')
funding_end_date_title = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[3]/span[1]')
funding_end_date_text = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[3]/span[2]')
est_sale_start_date_title = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[4]/span[1]')
est_sale_start_date_text= driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[4]/span[1]')
product_purchase_price_title = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[5]/span[1]')
product_purchase_price_text = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[5]/span[2]')
total_investment_units_title = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[6]/span[1]')
total_investment_units_text =  driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[6]/span[2]')
total_investment_required_title = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[7]/span[1]')
total_investment_units_text = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/div[4]/ul/li[7]/span[2]')
more_details_button = driver.find_element(By.XPATH,'//*[@id="myTabContent"]/div/div/div/div/div[1]/div[2]/div/h5/a')
batch_main_image=  driver.find_element(By.XPATH,'//*[@id="carouselVertical"]/div/div[2]/div/div[1]/img')
move_up_arrow = driver.find_element(By.XPATH,'//*[@id="carouselVertical"]/div/div[1]/button[1]')
move_down_arrow = driver.find_element(By.XPATH,'//*[@id="carouselVertical"]/div/div[1]/button[2]')
batch_image_1 = driver.find_element(By.XPATH,'//*[@id="carouselVertical"]/div/div[1]/div/button[1]/img')
batch_image_2 = driver.find_element(By.XPATH, '//*[@id="carouselVertical"]/div/div[1]/div/button[2]/img')
batch_image_3 = driver.find_element (By.XPATH, '//*[@id="carouselVertical"]/div/div[1]/div/button[3]/img')


