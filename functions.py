from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def init_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # Avoid close chrome when script end
    chrome_options.add_argument("--start-maximized")

    # s = Service("./chromedriver/chromedriver.exe")
    # ChromeDriver Linux
    s = Service("./chromedriver/chromedriver")

    # Specify the path to the web drivers
    driver = webdriver.Chrome(service=s, options=chrome_options)
    return driver
def login(driver, email, password):
    # Navigate to the login page
    driver.get("https://totalfitnes.wodbuster.com/account/login.aspx")

    email_field = driver.find_element("id", "body_body_body_body_IoEmail").send_keys(email)
    email_field = driver.find_element("id", "body_body_body_body_IoPassword").send_keys(password)

    loging_button = driver.find_element("id", "body_body_body_body_CtlEntrar").click()

def navigate_reservations(driver):
    driver.get("https://totalfitnes.wodbuster.com/athlete/reservas.aspx")
    time.sleep(0.1)


def select_next_day(driver):
    button_next_day = driver.find_element("xpath", "//*[@id='calendar']/div/div[1]/a[2]").click()
    time.sleep(0.1)
def close_conecction(driver):
    driver.close()