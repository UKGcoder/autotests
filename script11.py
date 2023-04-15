import time

import pytest as pytest
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from datetime import datetime


def getClick(XPATH):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, XPATH)))
    driver.find_element(By.XPATH, XPATH).click()


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


def test_new_deal_creator(test_setup):
    global start_time
    start_time = datetime.now()
    driver.find_element(By.XPATH, "//*[@id=\"login_email\"]").clear()
    driver.find_element(By.XPATH, "//*[@id=\"login_email\"]").send_keys("testing@selenium.com")
    driver.find_element(By.XPATH, "//*[@id=\"login_password\"]").clear()
    driver.find_element(By.XPATH, "//*[@id=\"login_password\"]").send_keys("aksjhd2912t7sai7w")
    getClick("//*[@id=\"page-login\"]/div/main/div[2]/div/section[1]/div/form/div[2]/button")
    assert WebDriverWait(driver, 10).until(
        EC.url_contains("app"))
    getClick('//*[@id="page-Workspaces"]/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/div[1]/a[4]')
    assert WebDriverWait(driver, 10).until(EC.url_contains(
        "https://develop.icrm.liss.pro/app/%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81%D0%BE-%D1%81%D0%B4%D0%B5%D0%BB%D0%BA%D0%B0%D0%BC%D0%B8"))
    getClick('//*[@id="page-Workspaces"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div[3]/div[2]/div[1]/div[2]/a[1]/span[2]')
    assert WebDriverWait(driver, 10).until(EC.url_contains("icrm-deal"))
    getClick('//*[@id="page-List/iCRM Deal/List"]/div[1]/div/div/div[2]/div[2]/button[2]')
    assert WebDriverWait(driver, 10).until(EC.url_contains("new-icrm-deal"))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,
         '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/div[1]/form/div[1]/div/div[2]/div[1]')))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="page-iCRM Deal"]/div[1]/div/div/div[2]/div[3]/button[2]')))
    driver.find_element(By.XPATH,
                        '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/div[1]/form/div[1]/div/div[2]/div[1]/input').send_keys(
        "15-04-2023")
    driver.find_element(By.XPATH,
                        '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/div[1]/form/div[2]/div/div[2]/div[1]/div/div/input').send_keys(
        "Тестовый пользователь")
    driver.find_element(By.XPATH,
                        '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/div[2]/form/div[1]/div/div[2]/div[1]/div/div/input').send_keys(
        'ООО "ОСТ"\n')
    driver.find_element(By.XPATH, '//*[@id="page-iCRM Deal"]/div[1]/div/div/div[2]/div[3]/button[2]').click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'alert-message')))
    timeDelta = datetime.now() - start_time
    print("Время, потребовавшееся на выполнение данного процесса: " + str(timeDelta))
