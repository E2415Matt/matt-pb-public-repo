# Import necessary library packages for chrome driver
from selenium import webdriver

# Create the instance of webdriver and show the path of chrome-driver
driver = webdriver.Chrome(executable_path="/Users/m.a/devops/selenium/chromedriver")

# Set web site base URL and the expected title of the web site
base_url = "https://metmar.co.uk"

expected_title = "Met Mar Ltd"
actual_title = ""
# Initiate the actual title of website and set it empty
actual_title = ""

# Request from the chrome-driver to launch Chrome Browser
# And direct it to the base URL
driver.get(base_url)

# Get the actual value of the title
actual_title = driver.title

# Compare the actual title of the page with the expected one
# Then, print "Test Passed" if equal, print "Test Failed" if not.
if actual_title == expected_title:
    print("Test Passed")
else:
    print("Test Failed")
    print(actual_title)

# Close the chrome-driver
driver.close()