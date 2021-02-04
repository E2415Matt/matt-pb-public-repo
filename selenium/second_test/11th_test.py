# if you want to use ec2 instance, please use following commands in cli to load chrome driver;

# bash:

# curl https://intoli.com/install-google-chrome.sh | bash
# google-chrome --version
# wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip
# sudo yum install unzip
# unzip chromedriver_linux64

# if you are working on local machine;

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/m.altun/clarus/devops/04feb_selenium/second_test/chromedriver")

base_url = "https://clarusway.com/"

driver.get(base_url)

element = driver.find_element_by_id("menu-item-2808")
print("has aws-devops button shown? ---> ", element.is_displayed())
time.sleep(5)
driver.quit()