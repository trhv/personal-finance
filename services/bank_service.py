import time
import csv
import os
import pandas
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from models.account_balance import AccountBalance
from models.account_movements import AccountMovements
from models.credit_card import CreditCard

class BankService():

    def __init__(self) -> None:
        self.create_driver()
        pass

    def create_driver(self):
        '''create_driver'''
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        options.add_argument('start-maximazed')
        # options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36");
        # options.add_argument('--headless')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('no-sandbox')
        options.add_argument('disable-blink-features=AutomationControlled')
        options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(options=options)

    def connect(self):
        self.driver.get('https://login.bankhapoalim.co.il/ng-portals/auth/he/')
        element = self.driver.find_element(By.ID, 'userCode')
        element.send_keys('vv74247')
        element = self.driver.find_element(By.ID, 'password')
        element.send_keys('trhv654321')
        element.send_keys(Keys.RETURN)
        wait1 = WebDriverWait(self.driver, 60)
        wait1.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'balance-and-limits')))
        print('Connected...')

    def __scrap_credit_card(self):
        # TODO - __scrap_credit_card fill data
        creditCard = CreditCard('tags', 'businessName', 'date',
                 'numPayments', 'currentPayment', 'amount', 'owner')
        creditCard.save_data()

    def __scrap_account_movements(self):
        # TODO - __scrap_account_movements fill data
        movement = AccountMovements('action', 'balance', 'date', 'amount')
        movement.save_data()

    def __scrap_account_balance(self):
        element = self.driver.find_element(
            By.XPATH, '/html/body/rb-root/poalim-header-footer-layout/main/poalim-dynamic-component-content/div/rb-homepage/section[2]/section[1]/div[1]/poalim-balance-and-limits/section/ul/li[1]/div/span[1]/span')
        spans = element.find_elements(By.TAG_NAME,'span')
        balance= float(("".join([span.text for span in spans])).replace(',',''))
        accountBalance = AccountBalance(balance)
        accountBalance.save_data()

    def scrap(self):
        # self.__scrap_credit_card()
        self.__scrap_account_balance()
        # self.__scrap_account_movements()
        pass