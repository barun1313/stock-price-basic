# Stocks.csv contains stock prices of 6 major stocks. In this code, we write functions
# that clean the code, compute the mean, std deviation and correlation matrix

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def clean_data():
    data = pd.read_csv("Stocks.csv")
    data.dropna(inplace=True)
    print(data)
    plt.plot(data["Date"], data["BA"])
    plt.show()
    # print(data)
    nb_rows = len(data.index)
    # print(nb_rows)
    return (nb_rows, data)


_, data1 = clean_data()


def compute_mean_portfolio(data):
    updated_data = data.copy()
    updated_data["Portfolio"] = (
        16 * updated_data["BA"]
        + 17 * updated_data["AAPL"]
        + 35 * updated_data["AMZN"]
        + 3 * updated_data["MSFT"]
        + 8 * updated_data["MC.PA"]
        + 21 * updated_data["GOOGL"]
    ) / 100
    mean_portfolio = updated_data["Portfolio"].mean()
    return (mean_portfolio, updated_data)


mean_data2, data2 = compute_mean_portfolio(data1)


def compute_standard_deviation_portfolio(data):
    updated_data = data.copy()
    std_dev_portfolio = updated_data["Portfolio"].std()
    return std_dev_portfolio


std_data3 = compute_standard_deviation_portfolio(data2)


def compute_interval(mean_portfolio, std_dev_portfolio):
    a = []
    b = []
    a = mean_portfolio - 2 * std_dev_portfolio
    b = mean_portfolio + 2 * std_dev_portfolio
    return (a, b)


compute_interval(mean_data2, std_data3)


def compute_correlation_matrix(data):
    data = data.copy()
    cor = data.corr()
    max_cor = cor["GM"].sort_values()[-2]

    return (max_cor, cor)


data5 = compute_correlation_matrix(data1)
