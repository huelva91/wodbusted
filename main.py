from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

email = config["login"]["email"]
password = config["login"]["password"]


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Avoid close chrome when script end
chrome_options.add_argument("--start-maximized")


#s = Service("./chromedriver/chromedriver.exe")
# ChromeDriver Linux
s = Service("./chromedriver/chromedriver")

# Specify the path to the web drivers
driver = webdriver.Chrome(service=s, options=chrome_options)

# Navigate to the login page
driver.get("https://totalfitnes.wodbuster.com/account/login.aspx")

email_field = driver.find_element("id", "body_body_body_body_IoEmail").send_keys(email)
email_field = driver.find_element("id", "body_body_body_body_IoPassword").send_keys(password)

loging_button = driver.find_element("id", "body_body_body_body_CtlEntrar").click()


driver.get("https://totalfitnes.wodbuster.com/athlete/reservas.aspx")
time.sleep(0.1)

button_next_day = driver.find_element("xpath", "//*[@id='calendar']/div/div[1]/a[2]").click()
time.sleep(0.1)
button_next_day2 = driver.find_element("xpath", "//*[@id='calendar']/div/div/a[2]").click()
time.sleep(0.1)

button_train_7 = driver.find_element("xpath", "//*[@id='calendar']/div/div[3]/div/div[1]/div/div[3]/button").click()


time.sleep(10)
driver.close()
