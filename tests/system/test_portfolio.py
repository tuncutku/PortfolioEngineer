"""Test portfolio endpoints"""
# pylint: disable=unused-argument

from src.environment.portfolio import Portfolio
from src.market import Currency
from src.market.types import PortfolioType

from tests.system.common import templete_used


def test_portfolio_list(client, _db, load_environment_data, login, captured_templates):
    """Test endpoint that lists portfolios."""

    response = client.get("/portfolio/list")
    assert response.status_code == 200

    template_list = ["portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)


def test_add_portfolio(client, _db, load_environment_data, login, captured_templates):
    """Test endpoint that adds portfolio."""

    response = client.get("portfolio/add_portfolio")
    assert response.status_code == 200
    assert "Add new custom portfolio" in response.get_data(as_text=True)

    data = dict(
        port_name="New",
        port_type=PortfolioType.margin,
        reporting_currency="USD",
        benchmark="^GSPC",
    )
    response = client.post("portfolio/add_portfolio", data=data, follow_redirects=True)
    assert response.status_code == 200

    new_portfolio = Portfolio.find_by_id(3)

    assert new_portfolio.name == "New"
    assert new_portfolio.portfolio_type == PortfolioType.margin
    assert new_portfolio.reporting_currency == Currency("USD")
    assert new_portfolio.primary is True

    template_list = ["portfolio/add_portfolio.html", "portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)


def test_edit_portfolio(client, _db, load_environment_data, login, captured_templates):
    """Test endpoint that edits an existing portfolio."""

    response = client.get("portfolio/edit/1")
    assert response.status_code == 200

    assert "Edit portfolio" in response.get_data(as_text=True)
    assert "portfolio_1" in response.get_data(as_text=True)
    assert "Margin" in response.get_data(as_text=True)
    assert "USD" in response.get_data(as_text=True)

    data = dict(
        port_name="edited_portfolio",
        port_type=PortfolioType.custom,
        reporting_currency="CAD",
    )
    response = client.post("portfolio/edit/1", data=data, follow_redirects=True)
    assert response.status_code == 200

    portfolio_test = Portfolio.find_by_id(1)
    assert portfolio_test.name == "edited_portfolio"
    assert portfolio_test.portfolio_type == PortfolioType.custom
    assert portfolio_test.reporting_currency == Currency("CAD")

    template_list = ["portfolio/edit_portfolio.html", "portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)


def test_delete_portfolio(
    client, _db, load_environment_data, login, captured_templates
):
    """Test endpoint that deletes portfolio."""

    response = client.get("portfolio/delete/1", follow_redirects=True)
    assert response.status_code == 200
    assert Portfolio.find_by_id(1) is None

    template_list = ["portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)


def test_set_portfolio_primary(
    client, _db, load_environment_data, login, captured_templates
):
    """Test endpoint that sets portfolio primary."""

    portfolio_1 = Portfolio.find_by_id(1)
    assert portfolio_1.primary is False

    response = client.get("portfolio/set_primary/1", follow_redirects=True)
    assert response.status_code == 200
    portfolio_1 = Portfolio.find_by_id(1)
    portfolio_2 = Portfolio.find_by_id(2)
    assert portfolio_1.primary is True
    assert portfolio_2.primary is False

    response = client.get("portfolio/set_primary/2", follow_redirects=True)
    assert portfolio_1.primary is False
    assert portfolio_2.primary is True

    template_list = ["portfolio/list_portfolios.html", "portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)


def test_portfolio_daily_report(
    client, _db, load_environment_data, login, captured_templates
):
    """Test endpoints that activates and deactivates daily report."""

    portfolio = Portfolio.find_by_id(1)
    daily_report = portfolio.daily_report

    response = client.get("portfolio/deactivate_daily_report/1", follow_redirects=True)
    assert response.status_code == 200
    assert daily_report.active is False

    response = client.get("portfolio/activate_daily_report/1", follow_redirects=True)
    assert response.status_code == 200
    assert daily_report.active is True

    template_list = ["portfolio/list_portfolios.html", "portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)
