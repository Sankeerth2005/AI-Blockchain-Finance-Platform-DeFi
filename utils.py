# scripts/utils.py
import pandas as pd
import numpy as np

def preprocess_data(data):
    """Preprocess data by filling missing values and scaling."""
    data = data.fillna(method='bfill')
    return data

def calculate_returns(prices):
    """Calculate daily returns from price data."""
    return np.diff(prices) / prices[:-1]
