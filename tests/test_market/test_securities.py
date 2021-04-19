"""Test securities."""

from datetime import date
import pytest

from src.market import Equity, ETF, Currency, Symbol, Security, SingleValue, IndexValue

start_date = date(2020, 1, 4)

currency = Currency("USD")
etf = ETF(asset_currency=currency, symbol=Symbol("PBW"))
equity = Equity(asset_currency=currency, symbol=Symbol("AAPL"))


@pytest.mark.parametrize(
    "security, symbol",
    [(etf, Symbol("PBW")), (equity, Symbol("AAPL"))],
    ids=["ETF", "Equity"],
)
def test_common(security: Security, symbol: Symbol):
    """Test common methods """

    assert security.asset_currency == currency
    assert security.symbol == symbol

    assert isinstance(security.value, SingleValue)
    assert isinstance(security.index(start_date), IndexValue)


def test_etf():
    """Test ETF."""


def test_equity():
    """Test Equity."""