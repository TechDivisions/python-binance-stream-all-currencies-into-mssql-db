import schedule
import urllib.request, json
import db
import time

def start():
    schedule.every(60).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

def job():
    retrieve_all_binance_currencies()

def retrieve_all_binance_currencies():
    with urllib.request.urlopen("https://api.binance.com/api/v3/ticker/price") as url:
        data = json.loads(url.read().decode())
        db.save_all_data(data)

start()