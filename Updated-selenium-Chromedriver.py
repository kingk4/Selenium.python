import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:/chromedriver.exe')
driver = webdriver.Chrome(service=s)

url = 'https://the-internet.herokuapp.com/login'

driver.get(url)

Username = driver.find_element(By.ID, 'username')
Username.send_keys('tomsmith')

Password = driver.find_element(By.ID, 'password')
Password.send_keys('SuperSecretPassword!')

login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login.click()