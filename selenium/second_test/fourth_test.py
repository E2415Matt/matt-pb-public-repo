# if you want to use ec2 instance, please use following commands in cli to load chrome driver;
# bash:

# curl https://intoli.com/install-google-chrome.sh | bash
# google-chrome --version
# wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip
# sudo yum install unzip
# unzip chromedriver_linux64

from selenium import webdriver
driver = webdriver.Chrome(executable_path="/Users/m.altun/clarus/devops/04feb_selenium/second_test/chromedriver")
base_url = "https://clarusway.com/"
expected_title = "Online Career IT Training School - Clarusway"
actual_title = ""
driver.get(base_url)
actual_title = driver.title

page_source = driver.page_source
print("page source : \n", page_source)

# if actual_title == expected_title:
#     print("Test Passed")
# else:
#     print("Test Failed")
#     print(actual_title)

driver.quit()
