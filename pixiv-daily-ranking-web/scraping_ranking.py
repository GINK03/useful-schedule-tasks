
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By


import bs4

import concurrent.futures

import hashlib

from pathlib import Path
import json
import gzip
import sys
import pickle
import time
import os
import random
from datetime import datetime

url = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust'

def getRanking():
  options = Options()
  options.add_argument('--headless')
  options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")

  driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/local/bin/chromedriver')
  driver.set_window_size(1024,1024*10)
  
  return_chunk = dict()
  
  dt = datetime.now().strftime('%Y-%m-%d_%H_%M')
  
  ha = hashlib.sha256(bytes(url, 'utf8')).hexdigest()

  driver.get(url)

  action = webdriver.common.action_chains.ActionChains(driver)
  html   = driver.page_source
  soup   = bs4.BeautifulSoup(html, 'lxml')

  absolutes = []
  for div in soup.findAll('div', {'class':'ranking-image-item'}):
    relative = div.find('a').get('href')
    absolute = f'https://www.pixiv.net{relative}'
    absolutes.append( absolute )
  json.dump(absolutes, fp=open(f'images-abosolutes/{dt}.json', 'w'), indent=2 )

  driver.save_screenshot(f'ss/{ha}.png')
  driver.quit() 

if __name__ == '__main__':
  getRanking()

