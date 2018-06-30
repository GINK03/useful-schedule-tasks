
from pathlib import Path
paths = [ path for path in sorted( Path('images-abosolutes').glob('*') ) ]
path  = paths[-1]

import json

urls = json.load(path.open())

import requests
from bs4 import BeautifulSoup as BS
import os
from hashlib import sha256
from datetime import datetime
import time

def each_image():
  dt = datetime.now().strftime('%Y-%m-%d_%H_%M') 
  try:
    os.mkdir(f'images-pixiv/{dt}')
  except: ...

  for url in urls:
    try: 
      print(url)
      r = requests.get(url,  headers={'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust'})
      print(r.status_code)
      html = r.text
      soup = BS(html)
      src = None
      for img in soup.findAll('img'):
          is_src = img.get('src')
          print(is_src)
          if '600x600' in is_src:
              src = is_src

      if src is None:
        continue
     
      # c/600x600/ 削除
      src = src.replace('c/600x600', '')

      hash = sha256(bytes(src, 'utf8')).hexdigest()

      r = requests.get(src,  headers={'referer': url})
      cnt = r.content 
      with open(f'images-pixiv/{dt}/{hash}.jpg', 'wb') as fp:
        fp.write( cnt )
      with open(f'images-pixiv/{dt}/{hash}.txt', 'w') as fp:
        fp.write( url )
    except Exception as ex:
      print(ex)

if __name__ == '__main__':
  each_image()
