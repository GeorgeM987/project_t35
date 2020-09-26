import sys, os, time
import requests, lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
#
#
#
if __name__ == "__main__":
    options = Options()
    options.headless = False
    DIR = os.path.dirname(os.path.abspath(__file__))
    PATH = os.path.join(DIR, 'geckodriver\geckodriver.exe')
    headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
    driver = webdriver.Firefox(options=options, executable_path=PATH)
    driver.get('https://www.google.com/maps/')

    def search():
        search_from = driver.find_element_by_id('searchboxinput')
        search_from.send_keys('Baia Mare')
        search_from.send_keys(Keys.RETURN)

        directions = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'iRxY3GoUYUY__button')))
        directions.send_keys(Keys.RETURN)

        reverse_dir = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'widget-directions-reverse')))
        reverse_dir.send_keys(Keys.RETURN)
        
        search_to = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input')))
        driver.execute_script("arguments[0].click();", search_to)
        search_to.send_keys('Cluj')
        search_to.send_keys(Keys.RETURN)
        return driver.current_url


    def best_route(url_):
        if url_ == driver.current_url:
            search_best_route = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'section-directions-trip-0'))).text
            return print(search_best_route)
