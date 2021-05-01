"""Test basic objects."""
# pylint: disable=pointless-statement

from datetime import date
from pandas import DataFrame, Series, DatetimeIndex

import pytest
from pytest_mock import MockerFixture

from src.market import Currency, SingleValue, IndexValue, Symbol, FX
from tests.sample_data import index_1, index_2, index_3, value_1, value_2, value_3

start_date = date(2020, 1, 2)
end_date = date(2021, 1, 4)


class TestSingleValue:
    """Tests for ValueIndex."""

    value = value_1

    def test_value(self, mock_symbol):
        """Test basic value."""
        assert self.value.value == 55
        assert self.value.currency == Currency("USD")

        new_value = self.value.to(Currency("CAD"))
        assert new_value.currency == Currency("CAD")
        assert new_value.value == 2750

    def test_value_sum(self):
        """Test value summation."""

        with pytest.raises(ValueError):
            value_1 + value_3

        new_value = value_1 + value_2

        assert isinstance(new_value, SingleValue)
        assert new_value.value == 65
        assert new_value.currency == Currency("USD")
        assert value_1 + value_2 == value_2 + value_1
        assert str(new_value) == "65 USD"

    def test_value_multiplication(self):
        """Test index multiplication."""

        new_value_1 = self.value * 2
        new_value_2 = 2 * self.value
        assert new_value_1 == new_value_2

        assert isinstance(new_value_1, SingleValue)
        assert new_value_1.value == 110
        assert new_value_1.currency == Currency("USD")


class TestValueIndex:
    """Tests for IndexValue."""

    index = index_1

    def test_index(self, mock_symbol):
        """Test basic index."""

        result_usd = Series(
            [10, 14, 20, 26],
            index=[
                date(2020, 1, 1),
                date(2020, 3, 1),
                date(2020, 5, 1),
                date(2020, 7, 1),
            ],
        )
        result_cad = Series(
            [500, 728, 1080, 1456],
            index=[
                date(2020, 1, 1),
                date(2020, 3, 1),
                date(2020, 5, 1),
                date(2020, 7, 1),
            ],
        )

        assert Series.equals(self.index.index, result_usd)
        assert index_1.currency == Currency("USD")

        new_index = self.index.to(Currency("CAD"))
        assert new_index.currency == Currency("CAD")
        assert Series.equals(new_index.index, result_cad)

    def test_index_sum(self):
        """Test index summation."""
        with pytest.raises(ValueError):
            index_1 + index_3

        new_index_1 = index_1 + index_2
        new_index_2 = index_2 + index_1

        assert isinstance(new_index_1, IndexValue)
        assert str(index_1) == "Index USD between 2020-01-01 - 2020-07-01"
        assert new_index_1.currency == Currency("USD")

        assert Series.equals(
            new_index_1.index,
            Series(
                [30, 14, 110, 60, 26, 78],
                index=[
                    date(2020, 1, 1),
                    date(2020, 3, 1),
                    date(2020, 3, 30),
                    date(2020, 5, 1),
                    date(2020, 7, 1),
                    date(2020, 7, 30),
                ],
            ),
        )
        assert new_index_1 == new_index_2

    def test_index_multiplication(self):
        """Test index multiplication."""

        new_index_1 = index_1 * 2
        new_index_2 = 2 * index_1
        assert new_index_1.currency == Currency("USD")
        assert new_index_1 == new_index_2
        assert sum(new_index_1.index) == 140

    def test_index_multiply(self):
        """Test index multiply method."""

        self.index.multiply(
            Series(
                [2, 5, 0, 7],
                index=[
                    date(2019, 1, 1),
                    date(2020, 3, 1),
                    date(2020, 6, 7),
                    date(2025, 12, 29),
                ],
            )
        )

    def test_index_replace(self):
        """Test index replace method."""

        self.index.replace(
            Series(
                [2, 5, 0, 7],
                index=[
                    date(2019, 1, 1),
                    date(2020, 3, 1),
                    date(2020, 6, 7),
                    date(2025, 12, 29),
                ],
            )
        )

        assert Series.equals(
            self.index.index,
            Series(
                [10, 5, 20, 26],
                index=[
                    date(2020, 1, 1),
                    date(2020, 3, 1),
                    date(2020, 5, 1),
                    date(2020, 7, 1),
                ],
            ),
        )


def test_currency():
    """Test currency."""

    with pytest.raises(ValueError):
        Currency.validate("ZAR")

    usd = Currency("USD")
    date_index = usd.calender(start_date, end_date)

    assert str(usd) == "USD"
    assert isinstance(date_index, DatetimeIndex)
    assert date_index.max().date() == date(2021, 1, 4)
    assert date_index.min().date() == date(2020, 1, 2)


def test_fx(mock_symbol):
    """Test fx index."""

    usdcad = FX(Currency("CAD"), Currency("USD"))
    assert usdcad.symbol == Symbol("USDCAD=X")
    assert usdcad.asset_currency == Currency("CAD")
    assert usdcad.numeraire_currency == Currency("USD")

    fx_value = usdcad.rate == 50
    assert usdcad.rate == 50

    fx_index = usdcad.index(start_date, end_date)
    assert fx_index.equals(
        Series(
            [50, 51, 52, 53, 54, 55, 56],
            index=[
                date(2020, 1, 1),
                date(2020, 2, 1),
                date(2020, 3, 1),
                date(2020, 4, 1),
                date(2020, 5, 1),
                date(2020, 6, 1),
                date(2020, 7, 1),
            ],
        )
    )


def test_symbol():
    """Test symbol."""

    symbol = Symbol("AAPL")
    wrong_symbol = Symbol("1111111111111")

    with pytest.raises(ValueError):
        Symbol.validate(["AAPL"])

    assert str(symbol) == "AAPL"
    assert symbol == "AAPL"
    assert symbol.is_valid
    assert not wrong_symbol.is_valid
    assert isinstance(symbol.info, dict)
    assert isinstance(symbol.index(date(2020, 1, 1), date.today()), Series)
    assert symbol.is_trading_day(date(2020, 1, 3))
    assert not symbol.is_trading_day(date(2020, 1, 1))