"""Test alert objects"""
# pylint: disable=unused-argument

import pytest

from src.environment import Portfolio, DailyReport, MarketAlert, WatchListInstrument
from src.market import SingleValue
from src.market.ref_data import gspc, cad_ccy, aapl
from tests.test_data import environment as env


def test_daily_alert_object(client, _db, load_environment_data):
    """Test saved order object."""

    portfolio = Portfolio.find_by_id(1)
    alert = portfolio.daily_report
    assert alert == DailyReport.find_by_id(1)
    assert alert.id == 1
    assert alert.active
    alert.deactivate()
    assert alert.active is False


def test_daily_report_alert(client, _db, load_environment_data):
    """Unit test for daily alert methods."""

    daily_alert = DailyReport.find_by_id(1)
    assert daily_alert.condition()
    assert daily_alert.email_template == "email/daily_report.html"
    assert daily_alert.recipients[0] == env.user_1_raw["email"]

    content = daily_alert.generate_email_content()

    assert content["Main"]["Portfolio name"] == "portfolio_1"
    assert content["Main"]["Portfolio type"] == "TFSA"
    assert content["Main"]["Benchmark"] == gspc
    assert content["Main"]["Reporting currency"] == cad_ccy
    assert isinstance(content["Main"]["Creation date"], str)
    assert isinstance(content["Main"]["Current market value"], SingleValue)
    assert content["Return_table"]


def test_market_alert(client, _db, load_environment_data, mock_current_md):
    """Unit test for daily alert methods."""

    market_alert = MarketAlert.find_by_id(1)

    assert market_alert.condition()
    assert market_alert.email_template == "email/market_alert.html"
    assert market_alert.recipients[0] == env.user_1_raw["email"]

    content = market_alert.generate_email_content()
    assert str(content["symbol"]) == "Equity AAPL"
    assert (
        str(content["signal"])
        == "Signal triggered when current price is upper than 100."
    )
    assert content["current_value"] == pytest.approx(120, 20)
    assert isinstance(content["triggered_time"], str)

    market_alert.deactivate()
    assert not market_alert.active


def test_watchlist_instrument(client, _db, load_environment_data):
    """Test watchlist instrument."""

    watchlist_instrument = WatchListInstrument.find_by_id(1)
    assert watchlist_instrument.instrument == aapl
    assert str(watchlist_instrument) == "<Watchlist instrument: Equity AAPL.>"
