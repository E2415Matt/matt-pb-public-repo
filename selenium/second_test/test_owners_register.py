from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import os

# Update webdriver instance of chrome-driver with adding chrome options
driver = webdriver.Chrome(executable_path="/Users/m.altun/clarus/devops/04feb_selenium/second_test/chromedriver")

# Connect to the application
APP_IP = os.environ['MASTER_PUBLIC_IP']
url = "http://"+APP_IP.strip()+":8080/"
print(url)
# do not forget to export public IP of ec2 on cli using: 'export MASTER_PUBLIC_IP=3.238.205.252'

driver.get(url)
sleep(5)

owners_link = driver.find_element_by_link_text("OWNERS")
owners_link.click()
sleep(3)

all_link = driver.find_element_by_link_text("REGISTER")
all_link.click()
sleep(3)

# Register new Owner to Petclinic App
fn_field = driver.find_element_by_name('firstName')
fn = 'Matt' + str(random.randint(0, 100))
fn_field.send_keys(fn)
sleep(3)

fn_field = driver.find_element_by_name('lastName')
fn_field.send_keys('Clarusway')
sleep(3)

fn_field = driver.find_element_by_name('address')
fn_field.send_keys('Ridge Corp. Street')
sleep(3)

fn_field = driver.find_element_by_name('city')
fn_field.send_keys('McLean')
sleep(3)

fn_field = driver.find_element_by_name('telephone')
fn_field.send_keys('+1230576803')
sleep(3)

fn_field.send_keys(Keys.ENTER)
sleep(3)
# Wait 2 second to get updated Owner List
sleep(3)

# Verify that new user is added to Owner List
if fn in driver.page_source:
    print(fn, 'is added and found in the Owners Table')
    print("Test Passed")
else:
    print(fn, 'is not found in the Owners Table')
    print("Test Failed")

driver.quit()