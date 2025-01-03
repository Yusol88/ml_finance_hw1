import pandas as pd
import matplotlib.pyplot as plt
import os

# Функция для построения графиков
def plot_current_situation():
    # Загрузка данных
    stocks = ['AAPL', 'MSFT', 'GOOGL']
    cryptos = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'XRP-USD']

    # Графики для акций
    plt.figure(figsize=(14, 7))
    for ticker in stocks:
        data = pd.read_csv(f'data/stocks/{ticker}.csv', index_col='Date', parse_dates=True)
        plt.plot(data['Close'], label=ticker)
    plt.title('Цены закрытия акций')
    plt.xlabel('Дата')
    plt.ylabel('Цена (USD)')
    plt.legend()
    plt.savefig('data/stocks/stock_prices.png')  # Сохранение графика
    plt.show()

    # Графики для криптовалют
    plt.figure(figsize=(14, 7))
    for ticker in cryptos:
        data = pd.read_csv(f'data/cryptos/{ticker}.csv', index_col='Date', parse_dates=True)
        plt.plot(data['Close'], label=ticker)
    plt.title('Цены закрытия криптовалют')
    plt.xlabel('Дата')
    plt.ylabel('Цена (USD)')
    plt.legend()
    plt.savefig('data/cryptos/crypto_prices.png')  # Сохранение графика
    plt.show()

# Вызов функции
plot_current_situation()