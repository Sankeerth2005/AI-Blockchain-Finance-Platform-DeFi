# tests/test_app.py
import pytest
from app import fetch_price, fetch_historical_data

def test_fetch_price():
    price, change = fetch_price("bitcoin")
    assert isinstance(price, (int, float))
    assert isinstance(change, (int, float))
    assert price > 0

def test_fetch_historical_data():
    data = fetch_historical_data("bitcoin", 14)
    assert isinstance(data, pd.DataFrame)
    assert 'price' in data.columns
    assert len(data) > 0
