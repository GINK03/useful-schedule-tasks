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
  #files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです。
  r = requests.post( url, headers=headers, params=payload) #, files=files)

schedule.every().day.at("10:30").do(job)
schedule.every().day.at("15:00").do(job)
schedule.every(1).minutes.do(job)
while True:
  schedule.run_pending()
  time.sleep(1)
