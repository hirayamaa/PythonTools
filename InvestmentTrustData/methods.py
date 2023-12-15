import requests
import os
import time
from const import CSV_DIR_PATH, INVESTMENT_TRUST_NAMES

DOWNLOADS = ['https://www.am.mufg.jp/fund_file/setteirai/253425.csv',
             'https://www.am.mufg.jp/fund_file/setteirai/253266.csv',
             'https://www.am.mufg.jp/fund_file/setteirai/254062.csv']


# 投資信託CSVを取得し特定フォルダに保存
def download_csv_data():
    for i in range(0, len(DOWNLOADS)):
        res = requests.get(DOWNLOADS[i])
        res.raise_for_status()
        if not os.path.exists(CSV_DIR_PATH):
            os.makedirs(CSV_DIR_PATH)
        f = open(f'{CSV_DIR_PATH / INVESTMENT_TRUST_NAMES[i]}.csv', 'wb')
        for chunk in res.iter_content(100000):
            f.write(chunk)
        f.close()
        time.sleep(1)
