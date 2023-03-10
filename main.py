from functions import *
import schedule
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

email = config["login"]["email"]
password = config["login"]["password"]
driver = init_driver()

login(driver, email, password)
navigate_reservations(driver)
select_next_day(driver)
schedule.every().day.at("23:06").do(select_class(driver))

time.sleep(10)
close_conecction(driver)
