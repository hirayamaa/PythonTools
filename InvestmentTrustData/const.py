from pathlib import Path

# 設定来データが入っているパス
BASE_DIR = Path.home() / 'Desktop/InvestmentTrust'
CSV_DIR_PATH = BASE_DIR / 'csv'
OUTPUT_DIR_PATH = BASE_DIR / 'Output'
BACKUP_DIR_PATH = BASE_DIR / 'BackUp'
INVESTMENT_TRUST_NAMES = ['eMAXIS Slim 全世界株式（オール・カントリー）',
                          'eMAXIS Slim 米国株式（Ｓ＆Ｐ500）',
                          'eMAXIS NASDAQ100インデックス']
