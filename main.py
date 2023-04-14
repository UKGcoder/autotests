import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service


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
    driver.get(url="https://develop.icrm.liss.pro/#login")
    yield
    driver.quit()


def test_login(test_setup):
    driver.find_element(By.XPATH, "//*[@id=\"login_email\"]").clear()
    driver.find_element(By.XPATH, "//*[@id=\"login_email\"]").send_keys("testing@selenium.com")
    driver.find_element(By.XPATH, "//*[@id=\"login_password\"]").clear()
    driver.find_element(By.XPATH, "//*[@id=\"login_password\"]").send_keys("aksjhd2912t7sai7w")
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "//*[@id=\"page-login\"]/div/main/div[2]/div/section[1]/div/form/div[2]/button").click()
    assert "app" in driver.current_url


