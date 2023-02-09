from functions import *
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

email = config["login"]["email"]
password = config["login"]["password"]
driver = init_driver()

login(driver,email, password)
navigate_reservations(driver)
select_next_day(driver)
close_conecction(driver)

