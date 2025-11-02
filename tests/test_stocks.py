import pytest
from data_sources.stocks import get_current_price


def test_get_current_price():
    ticker = "ACWI"
    price = get_current_price(ticker)

    assert price is not None, "Price should not be None"
    assert price > 0, "Price should be positive"
