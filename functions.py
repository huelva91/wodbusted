import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs


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
    driver.get("https://wodbuster.com/account/login.aspx?cb=drakkar")

    driver.find_element(By.ID, "body_body_CtlLogin_IoEmail").send_keys(email)
    driver.find_element(By.ID, "body_body_CtlLogin_IoPassword").send_keys(password)

    driver.find_element(By.ID, "body_body_CtlLogin_CtlAceptar").click()
    time.sleep(2)
    driver.find_element(By.ID, "body_body_CtlConfiar_CtlSeguro").click()


def get_weekday():
    current_date = datetime.datetime.now()
    return current_date.weekday()


def navigate_reservations(driver):
    time.sleep(1)
    driver.get("https://drakkar.wodbuster.com/athlete/reservas.aspx")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='calendar']/div/div[1]/a[3]")))
    #driver.find_element(By.XPATH, "//*[@id='calendar']/div/div[1]/a[3]").click()
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='calendar']/div/div[1]/a[2]")))
    print (current_url(driver))
    print("dia de la semana" + str(get_weekday()))
    driver.get(current_url(driver))
    boton = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div[2]/div/div/div[2]/div[4]/div/div/div[17]/div/div/div/div[3]/button")
    print(boton)



def current_url(driver):
    current_url = driver.current_url
    # URL proporcionada

    # Analiza la URL
    parsed_url = urlparse(current_url)

    # Obtiene los parámetros de consulta como un diccionario
    query_params = parse_qs(parsed_url.query)

    # Extrae el valor del parámetro 't'
    numero = query_params.get('t', [None])[0]

    numero2 = int(numero)
    url_final = f"https://drakkar.wodbuster.com/athlete/reservas.aspx?t={numero2}"
    return url_final


def select_next_day(driver):
    #numero magico 86400
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='calendar']/div/div[1]/a[2]")))
    driver.find_element(By.XPATH, "//*[@id='calendar']/div/div[1]/a[2]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='calendar']/div/div[1]/a[2]")))
    driver.find_element(By.XPATH, "//*[@id='calendar']/div/div[1]/a[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//*[@id='calendar']/div/div/a[2]").click()
    print("hi")


def select_class(driver):
    print("hola")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='calendar']/div/div[16]/div/div/div/div[3]/button")))
    current_url = driver.current_url()
    # URL proporcionada

    # Analiza la URL
    parsed_url = urlparse(current_url)

    # Obtiene los parámetros de consulta como un diccionario
    query_params = parse_qs(parsed_url.query)

    # Extrae el valor del parámetro 't'
    numero = query_params.get('t', [None])[0]


    print(numero)


    driver.find_element(By.XPATH,
                        "//*[@id='calendar']/div/div[16]/div/div/div/div[3]/button").click()


def close_conecction(driver):
    driver.close()
