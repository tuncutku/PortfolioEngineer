"""Test fixtures"""
# pylint: disable=redefined-outer-name, unused-argument

import pytest
from flask import template_rendered

from src import create_app
from src.environment import (
    User,
    Portfolio,
    Position,
    Order,
    MarketAlert,
    WatchListInstrument,
)

from src.extensions import db
from src.market.ref_data import aapl
from tests.test_data import environment as env
from tests.test_data import market as mkt


@pytest.fixture
def app():
    """Create application for the tests."""
    return create_app("testing")


@pytest.fixture
def _db(client):
    """Create database for the tests."""

    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture
def load_environment_data(client) -> User:
    """Provides sample user, portfolio, position and order."""

    user = User(**env.user_1_raw)
    portfolio = Portfolio(**env.portfolio_1_raw)
    position_1 = Position(**env.position_1_raw)
    position_2 = Position(**env.position_2_raw)
    order_1 = Order(**env.order_1_raw)
    order_2 = Order(**env.order_2_raw)
    order_3 = Order(**env.order_3_raw)
    order_4 = Order(**env.order_4_raw)
    order_5 = Order(**env.order_5_raw)
    order_6 = Order(**env.order_6_raw)
    price_alert = MarketAlert(mkt.price_signal)
    instrument = WatchListInstrument(aapl)

    user.save_to_db()
    user.confirm_user()
    user.add_watchlist_instrument(instrument)
    user.add_market_alert(price_alert)
    user.add_portfolio(portfolio)
    portfolio.daily_report.activate()

    for position in [position_1, position_2]:
        portfolio.add_position(position)

    for order in [order_1, order_2, order_3]:
        position_1.add_order(order)

    for order in [order_4, order_5, order_6]:
        position_2.add_order(order)


@pytest.fixture
def login(client):
    """Log in test user for URL tests."""

    client.post(
        "/users/login",
        data=dict(email=env.user_1_raw["email"], password=env.user_1_raw["password"]),
    )


@pytest.fixture
def captured_templates(app):
    """Capture templates used as during system tests."""

    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


@pytest.fixture
def mock_current_md(mocker):
    """Mock current market data."""

    mocker.patch(
        "src.market.basic.FX.rate",
        new_callable=mocker.PropertyMock,
        return_value=1.2,
    )


@pytest.fixture
def runner(client):
    """Runner for cli tests."""

    return client.application.test_cli_runner()
