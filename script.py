from notifier_botty import login_to_chegg, refresh_chegg, telegram_bot_sendtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta
import pytz
import requests
import multiprocessing


# Account credentials (you can add more accounts here)
accounts = [
    {"username": "himanshubhardwajsunny@gmail.com", "password": "p0lin528500@D", "user_bot_chatID": '1437550690', "account_name": "Vikas Calculus", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "himanshubhardwaj528500@gmail.com", "password": "p0lin528500@D", "user_bot_chatID": '1437550690', "account_name": "Ankit Calculus", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "amitsarohaji990@gmail.com", "password": "p0lin528500@D", "user_bot_chatID": '1437550690', "account_name": "Amit advance", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "kunduparshant06@gmail.com", "password": "p0lin528500@D", "user_bot_chatID": '1437550690', "account_name": "Nitin advance", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "sunny907606@gmail.com", "password": "Sunny@19", "user_bot_chatID": '1437550690', "account_name": "Sunny Advance", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    # Add more accounts if necessary
]

accept_option = True
start_time = 0  # Starting time. Default 0. In 24-hour format
end_time = 25  # Ending time. Default 25. In 24-hour format


def refresh_account(account):
    username = account["username"]
    password = account["password"]
    user_bot_chatID = account["user_bot_chatID"]
    account_name = account["account_name"]
    user_bot_token = account["user_bot_token"]  # Same token for all accounts

    # Set up Chrome WebDriver for this account
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Each account gets its own Chrome instance
    driver = webdriver.Chrome(options=options)

    # Attempt to log in
    flag_login = True
    while flag_login:
        flag_login = login_to_chegg(username, password, driver,account_name)


    # Start refreshing for the account
    refresh_chegg(driver, accept_option, start_time, end_time, user_bot_token, user_bot_chatID, account_name)  
    


if __name__ == "__main__":
    # Create a process for each account
    processes = []
    for account in accounts:
        process = multiprocessing.Process(target=refresh_account, args=(account,))
        processes.append(process)
        process.start()

    # Optionally join the processes to ensure the script waits for all to finish (though in infinite loops, this won't happen)
    for process in processes:
        process.join()
