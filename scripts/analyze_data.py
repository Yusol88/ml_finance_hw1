# scripts/analyze_data.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Функция для анализа пропусков и ошибок
def analyze_missing_data(data, ticker):
    print(f"\nАнализ данных для {ticker}:")
    print(data.info())  # Общая информация о данных
    print(data.isnull().sum())  # Пропуски
    print(data.describe())  # Описательная статистика

# Функция для анализа выбросов
def analyze_outliers(data, ticker):
    plt.figure(figsize=(14, 7))
    sns.boxplot(data=data['Close'])
    plt.title(f'Распределение цен закрытия для {ticker}')
    plt.show()

# Функция для оценки выбросов с использованием Z-оценки
def detect_outliers_zscore(data, threshold=3):
    z_scores = zscore(data['Close'])
    outliers = data[(z_scores > threshold) | (z_scores < -threshold)]
    return outliers

# Основной скрипт
def main():
    stocks = ['AAPL', 'MSFT', 'GOOGL']
    cryptos = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'XRP-USD']

    # Анализ данных по акциям
    print("Проверка данных по акциям:")
    for ticker in stocks:
        data = pd.read_csv(f'data/stocks/{ticker}.csv', index_col='Date', parse_dates=True)
        analyze_missing_data(data, ticker)
        analyze_outliers(data, ticker)
        outliers = detect_outliers_zscore(data)
        print(f"\nВыбросы для {ticker}:")
        print(outliers)

    # Анализ данных по криптовалютам
    print("\nПроверка данных по криптовалютам:")
    for ticker in cryptos:
        data = pd.read_csv(f'data/cryptos/{ticker}.csv', index_col='Date', parse_dates=True)
        analyze_missing_data(data, ticker)
        analyze_outliers(data, ticker)
        outliers = detect_outliers_zscore(data)
        print(f"\nВыбросы для {ticker}:")
        print(outliers)

if __name__ == "__main__":
    main()