import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(url="https://develop.icrm.liss.pro/#login")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id=\"login_email\"]").clear()
driver.find_element(By.XPATH, "//*[@id=\"login_email\"]").send_keys("testing@selenium.com")
driver.find_element(By.XPATH, "//*[@id=\"login_password\"]").clear()
driver.find_element(By.XPATH, "//*[@id=\"login_password\"]").send_keys("aksjhd2912t7sai7w")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id=\"page-login\"]/div/main/div[2]/div/section[1]/div/form/div[2]/button").click()
time.sleep(3)
assert "app" in driver.current_url
