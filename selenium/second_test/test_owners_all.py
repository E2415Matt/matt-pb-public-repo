from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

driver = webdriver.Chrome(executable_path="/Users/m.altun/clarus/devops/04feb_selenium/second_test/chromedriver")

# Connect to the application
APP_IP = os.environ['MASTER_PUBLIC_IP']
url = "http://"+APP_IP.strip()+":8080/"
# do not forget to export public IP of ec2 on cli using: 'export MASTER_PUBLIC_IP=3.238.205.252'

driver.get(url)

sleep(5)
owners_link = driver.find_element_by_link_text("OWNERS")
owners_link.click()
sleep(3)

all_link = driver.find_element_by_link_text("ALL")
all_link.click()
sleep(3)

# Verify that table loaded
sleep(3)
verify_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

print("Table loaded")

driver.quit()