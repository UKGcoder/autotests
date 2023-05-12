import undetected_chromedriver as uc
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from datetime import datetime


def inputField(xpath, driver: uc.Chrome, text):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    field = driver.find_element(By.XPATH, xpath)
    field.clear()
    field.send_keys(text)

def checkChanges(xpath, driver: uc.Chrome, text):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    field = driver.find_element(By.XPATH, xpath).get_attribute("value")
    print(field)
    if text == field:
        return True
    return False


def input_deal(driver: uc.Chrome):
    driver.get("https://develop.icrm.liss.pro/app/icrm-deal/%D0%90%D0%9E%20%22%D0%93%D0%B0%D0%B7%D0%BF%D1%80%D0%BE%D0%BC%D0%BD%D0%B5%D1%84%D1%82%D1%8C-%D0%9D%D0%9D%D0%93%22%200140")
    inputField(xpath='//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[3]/div/div[1]/form/div[1]/div/div[2]/div[1]/input',
               driver=driver, text="test1")
    inputField('//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[1]/input', driver, text="12-05-2023\n")
    inputField(text='13-05-2023\n', xpath='//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[4]/div/div[2]/form/div/div/div[2]/div[1]/input', driver=driver)

def check_changes(driver: uc.Chrome):
    driver.get(
        "https://develop.icrm.liss.pro/app/icrm-deal/%D0%90%D0%9E%20%22%D0%93%D0%B0%D0%B7%D0%BF%D1%80%D0%BE%D0%BC%D0%BD%D0%B5%D1%84%D1%82%D1%8C-%D0%9D%D0%9D%D0%93%22%200140")
    passed = checkChanges(
        xpath='//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[3]/div/div[1]/form/div[1]/div/div[2]/div[1]/input',
        driver=driver, text="test1")
    if not passed:
        return False
    passed = checkChanges(
        '//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[1]/input',
        driver, text="12-05-2023")
    if not passed:
        return False
    passed = checkChanges(text='13-05-2023',
               xpath='//*[@id="page-iCRM Deal"]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[3]/div[4]/div/div[2]/form/div/div/div[2]/div[1]/input',
               driver=driver)
    if not passed:
        return False
    return True

