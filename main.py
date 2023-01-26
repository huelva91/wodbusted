from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Avoid close chrome when script end
chrome_options.add_argument("--start-maximized")


s = Service("./chromedriver/chromedriver.exe")
# ChromeDriver Linux s = Service("./chromedriver/chromedriver")

# Specify the path to the web drivers
driver = webdriver.Chrome(service=s, options=chrome_options)

# Navigate to the login page
driver.get("https://totalfitnes.wodbuster.com/account/login.aspx")

email_field = driver.find_element("id", "body_body_body_body_IoEmail")
email_field.send_keys("your_email")
email_field = driver.find_element("id", "body_body_body_body_IoPassword")
email_field.send_keys("your_pass")

loging_button = driver.find_element("id", "body_body_body_body_CtlEntrar")
loging_button.click()

time.sleep(10)
driver.close()
