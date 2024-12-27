# scripts/plot_data.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

def plot_current_situation(stocks, cryptos, start_date, end_date):
    """
    Функция для автоматического отображения графиков текущей ситуации.
    
    :param stocks: Список тикеров акций.
    :param cryptos: Список тикеров криптовалют.
    :param start_date: Начальная дата для загрузки данных.
    :param end_date: Конечная дата для загрузки данных.
    """
    # Загрузка данных
    stock_data = yf.download(stocks, start=start_date, end=end_date, group_by='ticker')
    crypto_data = yf.download(cryptos, start=start_date, end=end_date, group_by='ticker')

    # Обработка данных
    stock_data.fillna(0, inplace=True)
    crypto_data.fillna(0, inplace=True)

    for ticker in stocks:
        stock_data[ticker] = pd.to_numeric(stock_data[ticker]['Close'], errors='coerce')
    for ticker in cryptos:
        crypto_data[ticker] = pd.to_numeric(crypto_data[ticker]['Close'], errors='coerce')

    stock_data.dropna(inplace=True)
    crypto_data.dropna(inplace=True)

    # Создание директорий, если они не существуют
    os.makedirs('../data/stocks', exist_ok=True)
    os.makedirs('../data/cryptos', exist_ok=True)

    # Графики цен закрытия для акций
    plt.figure(figsize=(14, 7))
    for ticker in stocks:
        plt.plot(stock_data[ticker], label=ticker)
    plt.title('Цены закрытия акций')
    plt.xlabel('Дата')
    plt.ylabel('Цена (USD)')
    plt.legend()
    plt.savefig('../data/stocks/stock_prices.png')  # Сохранение графика
    plt.show()

    # Графики цен закрытия для криптовалют
    plt.figure(figsize=(14, 7))
    for ticker in cryptos:
        plt.plot(crypto_data[ticker], label=ticker)
    plt.title('Цены закрытия криптовалют')
    plt.xlabel('Дата')
    plt.ylabel('Цена (USD)')
    plt.legend()
    plt.savefig('../data/cryptos/crypto_prices.png')  # Сохранение графика
    plt.show()

# Параметры
stocks = ['AAPL', 'MSFT', 'GOOGL']  # Пример акций из SnP500
cryptos = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'XRP-USD']  # Пример криптовалют
start_date = '2023-01-01'  # Начальная дата
end_date = datetime.now().strftime('%Y-%m-%d')  # Текущая дата

# Вызов функции для отображения графиков
plot_current_situation(stocks, cryptos, start_date, end_date)