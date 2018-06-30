import scraping_ranking
import scraping_each_images
import line_push
import dropbox_upload

import schedule
import time
def job():
  try:
    scraping_ranking.getRanking()
    scraping_each_images.each_image()
    line_push.push()
    dropbox_upload.dbx()
  except Exception as ex:
    print(ex)

schedule.every().day.at("10:30").do(job)
schedule.every().day.at("15:00").do(job)

schedule.every(1).hours.do(job)

job()
while True:
  schedule.run_pending()
  time.sleep(1)
