import yfinance as yf
import pandas as pd
import os

# Список активов
stocks = ['AAPL', 'MSFT', 'GOOGL']  # Пример акций
cryptos = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'XRP-USD']  # Пример криптовалют

# Параметры загрузки
start_date = '2023-01-01'
end_date = '2023-10-01'

# Загрузка данных
stock_data = yf.download(stocks, start=start_date, end=end_date, group_by='ticker')
crypto_data = yf.download(cryptos, start=start_date, end=end_date, group_by='ticker')

# Создание директорий
os.makedirs('data/stocks', exist_ok=True)
os.makedirs('data/cryptos', exist_ok=True)

# Сохранение данных по каждой акции в отдельный CSV
for ticker in stocks:
    file_path = f'data/stocks/{ticker}.csv'
    stock_data[ticker].to_csv(file_path)
    print(f"Данные для {ticker} сохранены в {file_path}")

# Сохранение данных по каждой криптовалюте в отдельный CSV
for ticker in cryptos:
    file_path = f'data/cryptos/{ticker}.csv'
    crypto_data[ticker].to_csv(file_path)
    print(f"Данные для {ticker} сохранены в {file_path}")