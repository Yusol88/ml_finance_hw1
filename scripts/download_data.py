import yfinance as yf
import pandas as pd
import os  # Для работы с путями и создания директорий

# Список активов
stocks = ['AAPL', 'MSFT', 'GOOGL']  # Пример акций из SnP500
cryptos = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'XRP-USD']

# Загрузка данных
def download_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker')
    return data

# Параметры загрузки
start_date = '2020-01-01'
end_date = '2023-10-01'

# Загрузка данных
stock_data = download_data(stocks, start_date, end_date)
crypto_data = download_data(cryptos, start_date, end_date)

# Создание директорий, если они не существуют
os.makedirs('data/stocks', exist_ok=True)  # Папка для акций
os.makedirs('data/cryptos', exist_ok=True)  # Папка для криптовалют

# Сохранение данных в CSV
stock_data.to_csv('data/stocks/stock_data.csv')
crypto_data.to_csv('data/cryptos/crypto_data.csv')

print("Данные успешно сохранены в папку 'data'.")