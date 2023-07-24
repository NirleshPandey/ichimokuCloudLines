import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opstra.definedge.com/")
wait = WebDriverWait(driver, 5)
sign_btn = driver.find_element(by=By.CSS_SELECTOR,value=".v-toolbar_content .hidden-xs-only:nth-child(5) .v-btn_content")
sign_btn.click()
username = driver.find_element(by=By.ID, value="username")
username.send_keys("nirleshpandey7@gmail.com")
password = driver.find_element(by=By.ID, value="password")
password.send_keys("Nirlesh@123")
time.sleep(5)
login = driver.find_element(by=By.ID, value="kc-login")
login.click()
Cnt_with_login= driver.find_element(by=By.CSS_SELECTOR,value="[class='text-none mt-3 v-btn v-btn--large v-btn--outline v-btn--depressed v-btn--round v-btn--router theme--light white--text'] .v-btn__content")
Cnt_with_login.click()
time.sleep(5)
Option = driver.find_element(by=By.CSS_SELECTOR,value=".v-expansion-panel__header .text-xs-center")
Option.click()
#Changing type from 1-10 get different dates csv
Next_Bttn = driver.find_element(by=By.CSS_SELECTOR,value='.md1:nth-of-type(10) .v-btn__content')
Next_Bttn.click()
table_element = driver.find_element(by=By.CSS_SELECTOR,value='table')
table_html = table_element.get_attribute('outerHTML')
from bs4 import BeautifulSoup

soup = BeautifulSoup(table_html, 'html.parser')
data_list = []

# Find all table rows (tr elements) in the table
rows = soup.find_all('tr')

for row in rows:
    # Find all cells (td elements) in each row
    cells = row.find_all(['td', 'th'])

    # Extract data from each cell and add it to the data_list as a row
    row_data = [cell.get_text(strip=True) for cell in cells]
    data_list.append(row_data)

# Save the data_list to a CSV file
csv_file_path = '26NOV2024.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data_list)

print(f"Data saved to {csv_file_path}.")