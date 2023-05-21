import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from datetime import datetime


@pytest.fixture()
def test_setup():
    global driver
    s = Service(executable_path="/var/jenkins_home/chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')  # # Bypass OS security model
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=s, options=options)
    #driver = uc.Chrome(options=options)
    driver.get(url="https://develop.icrm.liss.pro/#login")
    yield
    driver.quit()


def test_login(test_setup):
    # driver = webdriver.Chrome(service=s, options=options)

    # login_email
    driver.get(url="https://develop.icrm.liss.pro/#login")
    start_time = datetime.now()
    driver.find_element(By.XPATH, "//*[@id=\"login_email\"]").clear()
    driver.find_element(By.XPATH, "//*[@id=\"login_email\"]").send_keys("testing@selenium.com")
    driver.find_element(By.XPATH, "//*[@id=\"login_password\"]").clear()
    driver.find_element(By.XPATH, "//*[@id=\"login_password\"]").send_keys("aksjhd2912t7sai7w")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id=\"page-login\"]/div/main/div[2]/div/section[1]/div/form/div[2]/button")))
    #time.sleep(3)
    driver.find_element(By.XPATH,
                        "//*[@id=\"page-login\"]/div/main/div[2]/div/section[1]/div/form/div[2]/button").click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("app"))
    assert "app" in driver.current_url
    timeDelta = datetime.now() - start_time
    print("Время, потребовавшееся на выполнение данного процесса: " + str(timeDelta.seconds) + "s")


