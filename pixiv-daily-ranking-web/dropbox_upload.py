import dropbox
import time
import datetime
from pathlib import Path
import re

def dbx():
  dbx = dropbox.Dropbox(Path('token_dbx.txt').open().read().strip())

  mode = dropbox.files.WriteMode.overwrite

  _path = sorted( Path('images-pixiv').glob('*') )[-1]

  #  日時で分散
  for path in _path.glob('*'):
    data = path.open('rb').read()
    dpath = re.search(r'.*?/(.*?/.*?$)', str(path)).group(1)
    print(dpath)
    res = dbx.files_upload( data, '/' + dpath , mode, mute=True)
 
  # flatにネストせずに保存
  for path in _path.glob('*'):
    if '.txt' in str(path):
      continue
    data = path.open('rb').read()
    dpath = re.search(r'.*?/.*?/(.*?$)', str(path)).group(1)
    print(dpath)
    res = dbx.files_upload( data, '/flat/' + dpath , mode, mute=True)

if __name__ == '__main__':
    dbx()
