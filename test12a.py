import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from datetime import datetime

Server = False


def getDriver(isServer):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-infobars')
    if isServer:
        s = Service(executable_path="/var/jenkins_home/chromedriver")
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(service=s, options=options)
    else:
        driver = uc.Chrome(options=options)
    return driver


def login(username, password, driver):
    driver.find_element(By.XPATH, "//*[@id=\"login_email\"]").clear()
    driver.find_element(By.XPATH, "//*[@id=\"login_email\"]").send_keys(username)
    driver.find_element(By.XPATH, "//*[@id=\"login_password\"]").clear()
    driver.find_element(By.XPATH, "//*[@id=\"login_password\"]").send_keys(password)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id=\"page-login\"]/div/main/div[2]/div/section[1]/div/form/div[2]/button")))
    # time.sleep(3)
    driver.find_element(By.XPATH,
                        "//*[@id=\"page-login\"]/div/main/div[2]/div/section[1]/div/form/div[2]/button").click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("app"))


def lock_deal(driver: webdriver.Chrome):
    driver.get("https://develop.icrm.liss.pro/app/icrm-lock/new-icrm-lock-1")
    save = (By.XPATH, '//*[@id="page-iCRM Lock"]/div[1]/div/div/div[2]/div[3]/button[2]')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(save))
    driver.find_element(By.XPATH,
                        '//*[@id="page-iCRM Lock"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div/div/div/form/div[3]/div/div[2]/div[1]/div/div/input').send_keys(
        "iCRM Deal\n")
    driver.find_element(By.XPATH,
                        '//*[@id="page-iCRM Lock"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div/div/div/form/div[4]/div/div[2]/div[1]/input').send_keys(
        'АО "Газпромнефть-ННГ" 0140\n')
    driver.find_element(By.XPATH, '//*[@id="page-iCRM Lock"]/div[1]/div/div/div[2]/div[3]/button[2]').click()
    time.sleep(3)


def get_deal(driver):
    driver.get(
        url="https://develop.icrm.liss.pro/app/icrm-deal/%D0%90%D0%9E%20%22%D0%93%D0%B0%D0%B7%D0%BF%D1%80%D0%BE%D0%BC%D0%BD%D0%B5%D1%84%D1%82%D1%8C-%D0%9D%D0%9D%D0%93%22%200140")
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
    except:
        print('aaaaaaaaa')


def checkLock(driver):
    get_deal(driver)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/div[1]')))

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                   '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div[2]/button')))
    driver.find_element(By.XPATH,
                        '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div[2]/button').click()
    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="page-iCRM Invoice"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[1]')))

    get_deal(driver)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                               '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div[5]/div[2]/div/div/div[1]/div[2]/div[2]/button')))
    driver.find_element(By.XPATH,
                        '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div[5]/div[2]/div/div/div[1]/div[2]/div[2]/button').click()
    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="page-iCRM Task"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[1]')))

    get_deal(driver)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                               '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div[5]/div[2]/div/div/div[1]/div[3]/div[2]/button')))
    driver.find_element(By.XPATH,
                        '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div[5]/div[2]/div/div/div[1]/div[3]/div[2]/button').click()
    assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="page-iCRM Done Job Act"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[1]')))


@pytest.fixture()
def test_setup():
    global driver2
    global driver1
    driver2 = getDriver(Server)
    driver1 = getDriver(Server)
    driver2.get(url="https://develop.icrm.liss.pro/#login")
    driver1.get(url="https://develop.icrm.liss.pro/#login")
    yield
    driver1.quit()
    driver2.quit()


def test_login(test_setup):
    login(username="testing@selenium.com", password="aksjhd2912t7sai7w", driver=driver2)
    login(username="secondtest@test.com", password="Khhkauds7gka8g3qo21", driver=driver1)
    lock_deal(driver=driver2)
    try:
        checkLock(driver=driver1)
    except:
        pytest.fail(msg="Тест завершился с ошибкой. Блокировка не сработала",
                    pytrace=False)
    time.sleep(180)
    get_deal(driver1)
    passed = True
    try:
        WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                         '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/div[1]')))
        checkLock(driver=driver1)
        passed = False
    except:
        pass
    if not passed:
        pytest.fail(reason="Тест завершился с ошибкой. Разблокировка не сработала",
                    pytrace=False)
