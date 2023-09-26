import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def sendEmail(email_address, message):
    driver=webdriver.Firefox()
    driver.get('https://www.gmail.com')
    email_field=driver.find_element(By.ID,'identifierId')
    email_field.send_keys('brahim.touti15@gmail.com')
    email_field.send_keys(Keys.ENTER)
    driver.implicitly_wait(1)
    password_field=driver.find_element(By.CLASS_NAME,'whsOnd zHQkBf')
    password_field.send_keys('Aqwxsz1928')
    composite_button=driver.find_element(By.CLASS_NAME,'T-I T-I-KE L3')
    composite_button.click()
    driver.implicitly_wait(2)
    to_field=driver.find_element(By.ID,':to')
    to_field.send_keys(email_address)
    body_input=driver.find_element(By.ID,':r2')
    body_input.send_keys(message)
    send_button=driver.find_element(By.ID,':PJ')
    send_button.click()
    time.sleep(7)
    driver.quit()

sendEmail('brahim.touti15@gmail.com','hello')