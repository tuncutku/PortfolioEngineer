from src.environment.portfolio import Portfolio

from tests.test_system.common import templete_used
from tests.sample_data import *


def test_portfolio_list(client, db, user, captured_templates):

    response = client.get("/portfolio/list")
    assert response.status_code == 200

    template_list = ["portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)


def test_add_portfolio(client, db, user, captured_templates):

    response = client.get("portfolio/add_portfolio")
    assert response.status_code == 200
    assert "Add new custom portfolio" in response.get_data(as_text=True)

    response = client.post(
        "portfolio/add_portfolio",
        data=dict(
            port_name="New",
            port_type=PortfolioType.margin,
            port_reporting_currency=Currency.USD,
            benchmark="^GSPC",
        ),
        follow_redirects=True,
    )
    assert response.status_code == 200

    new_portfolio = Portfolio.find_by_id(2)

    assert new_portfolio.name == "New"
    assert new_portfolio.portfolio_type == PortfolioType.margin
    assert new_portfolio.reporting_currency == Currency.USD

    template_list = ["portfolio/add_portfolio.html", "portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)


def test_edit_portfolio(client, db, user, captured_templates):

    response = client.get("portfolio/edit/1")
    assert response.status_code == 200

    assert "Edit portfolio" in response.get_data(as_text=True)
    assert "portfolio_1" in response.get_data(as_text=True)
    assert "Margin" in response.get_data(as_text=True)
    assert "USD" in response.get_data(as_text=True)

    response = client.post(
        "portfolio/edit/1",
        data=dict(
            port_name="edited_portfolio",
            port_type=PortfolioType.custom,
            port_reporting_currency=Currency.CAD,
        ),
        follow_redirects=True,
    )
    assert response.status_code == 200

    portfolio_test = Portfolio.find_by_id(1)
    assert portfolio_test.name == "edited_portfolio"
    assert portfolio_test.portfolio_type == PortfolioType.custom
    assert portfolio_test.reporting_currency == Currency.CAD

    template_list = ["portfolio/edit_portfolio.html", "portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)


def test_delete_portfolio(client, db, user, captured_templates):

    response = client.get("portfolio/delete/1", follow_redirects=True)
    assert response.status_code == 200
    assert Portfolio.find_by_id(1) == None

    template_list = ["portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)


def test_set_portfolio_primary(client, db, user, captured_templates):

    portfolio = Portfolio.find_by_id(1)
    assert portfolio.primary == False
    response = client.get("portfolio/set_primary/1", follow_redirects=True)
    assert response.status_code == 200
    portfolio = Portfolio.find_by_id(1)
    assert portfolio.primary == True

    template_list = ["portfolio/list_portfolios.html"]
    templete_used(template_list, captured_templates)
