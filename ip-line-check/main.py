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
  
  try:
    ip = requests.get('https://api.ipify.org').text
    hostname = gethostname()
    payload = { "message": f'このコンピュータ({hostname})のGlobalIPは{ip}です' }
    r = requests.post( url, headers=headers, params=payload) #, files=files)
    print( json.dumps(payload,indent=2, ensure_ascii=False ) )
  except Exception as ex:
    print(ex)
  #files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです。

schedule.every().day.at("10:30").do(job)
schedule.every().day.at("15:00").do(job)
#schedule.every(1).minutes.do(job)
job()
while True:
  schedule.run_pending()
  time.sleep(1)
