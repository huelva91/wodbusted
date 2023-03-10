import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.support.wait import WebDriverWait


def init_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # Avoid close chrome when script end
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")

    s = Service("./chromedriver/chromedriver.exe")
    # ChromeDriver Linux
    # s = Service("./chromedriver/chromedriver")

    # Specify the path to the web drivers
    driver = webdriver.Chrome(service=s, options=chrome_options)
    return driver


def login(driver, email, password):
    # Navigate to the login page
    driver.get("https://totalfitnes.wodbuster.com/account/login.aspx")

    driver.find_element(By.ID, "body_body_body_body_IoEmail").send_keys(email)
    driver.find_element(By.ID, "body_body_body_body_IoPassword").send_keys(password)

    driver.find_element(By.ID, "body_body_body_body_CtlEntrar").click()


def get_weekday():
    current_date = datetime.datetime.now()
    return current_date.weekday()


def navigate_reservations(driver):
    driver.get("https://totalfitnes.wodbuster.com/athlete/reservas.aspx")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='calendar']/div/div[1]/a[2]")))


def select_next_day(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='calendar']/div/div[1]/a[2]")))
    driver.find_element(By.XPATH, "//*[@id='calendar']/div/div[1]/a[2]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='calendar']/div/div[1]/a[2]")))
    driver.find_element(By.XPATH, "//*[@id='calendar']/div/div[1]/a[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//*[@id='calendar']/div/div/a[2]").click()
    print("hi")


def select_class(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='calendar']/div/div[16]/div/div/div/div[3]/button")))

    driver.find_element(By.XPATH,
                        "//*[@id='calendar']/div/div[16]/div/div/div/div[3]/button").click()


def close_conecction(driver):
    driver.close()
