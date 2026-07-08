import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

print("--- Easy method to read Excel data using pandas ---")

# 1. Read the credentials from Excel
df = pd.read_excel('credentials.xlsx')

# Extract username and password from the first row
excel_username = str(df.iloc[0]['Username'])
excel_password = str(df.iloc[0]['Password'])

# 2. Initialize the Chrome Browser
driver = webdriver.Chrome()

try:
    # 3. Open the target website
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    time.sleep(2)  # Allow page to load

    # 4. Locate Username and Password fields and input data
    username_field = driver.find_element(By.NAME, "userid")
    password_field = driver.find_element(By.NAME, "pswrd")

    username_field.send_keys(excel_username)
    password_field.send_keys(excel_password)

    print(f"Successfully entered username: {excel_username}")

    # 5. Locate and click the Login/Submit button
    # The login button on omayo is typically inside a form table or an input button
    login_button = driver.find_element(By.XPATH, "//input[@type='submit' or @value='Login']")
    login_button.click()

except Exception as e:
    print("An error occurred during automation:", e)

# print("--- loop through data, Starting Data-Driven Testing with pandas ---")
#
# # 1. Load the Excel file into a pandas DataFrame
# df = pd.read_excel('credentials.xlsx')
#
# # 2. Initialize the Chrome Browser (We open it once outside the loop)
# driver = webdriver.Chrome()
#
# try:
#     # 3. Open the website once
#     driver.get("https://omayo.blogspot.com/")
#     driver.maximize_window()
#     time.sleep(2)
#
#     # 4. HERE IS WHERE YOU ADD THE LOOP:
#     # It will read each row from your Excel file one by one
#     for index, row in df.iterrows():
#         excel_username = row['Username']
#         excel_password = row['Password']
#
#         print(f"Processing row {index + 1}: Submitting {excel_username}")
#
#         # Find the Username and Password input fields
#         username_field = driver.find_element(By.NAME, "userid")
#         password_field = driver.find_element(By.NAME, "pswrd")
#
#         # Clear any previous text in the boxes before typing new data
#         username_field.clear()
#         password_field.clear()
#
#         # Type the credentials retrieved via pandas
#         username_field.send_keys(str(excel_username))
#         password_field.send_keys(str(excel_password))
#
#         # Find the login button and click it
#         login_button = driver.find_element(By.XPATH, "//input[@type='submit' or @value='Login']")
#         login_button.click()
#
#         # Pause for a brief moment to watch it work before moving to the next row
#         time.sleep(3)
#
#     print("All rows from Excel have been processed!")
#
# except Exception as e:
#     print("An error occurred during execution:", e)