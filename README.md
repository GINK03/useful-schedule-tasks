# .(dot) file appendixies

## CRONでジョブ管理はめんどくさすぎる
- 代替としてPythonで動作するもの
- shell scriptはもう使わない
- tmux　or screenで恒常化する

=> [schedule](https://github.com/dbader/schedule)モジュールを使う

## scheduleモジュールの例
```python
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## Global IP監視の例
```python
import requests
import os
from socket import gethostname
import schedule
import time
import json
def job():
  url = "https://notify-api.line.me/api/notify"
  token = open('secret.txt').read().strip()
  headers = {"Authorization" : "Bearer "+ token}

  ip = requests.get('https://api.ipify.org').text
  hostname = gethostname()
  payload = { "message": f'このコンピュータ({hostname})のGlobalIPは{ip}です' }
  print( json.dumps(payload,indent=2, ensure_ascii=False ) )
  r = requests.post( url, headers=headers, params=payload) #, files=files)

schedule.every().day.at("10:30").do(job)
schedule.every().day.at("15:00").do(job)
schedule.every(1).minutes.do(job)
while True:
  schedule.run_pending()
  time.sleep(1)
```

## ディレクトリ構成

- **ip-line-check** => IP, hostname監視
