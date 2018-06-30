
from pathlib import Path
import requests
def push():

  url     = "https://notify-api.line.me/api/notify"
  token   = open('secret.txt').read().strip()
  headers = {"Authorization" : "Bearer "+ token}
  
  path = sorted(Path('./images-pixiv').glob('*'))[-1]

  for jpg in path.glob('*.jpg'):
    try:
      files   = { "imageFile": jpg.open('rb') }
      payload = { "message": f'test' }
      r = requests.post( url, headers=headers, params=payload, files=files)
    except Exception as ex:
      print(ex)

if __name__ == '__main__':
  push()
