"""Portfolio endpoints"""

from flask import Blueprint, url_for, render_template, redirect, flash
from flask_login import login_required, current_user
from flask_wtf import FlaskForm

from src.environment import Portfolio
from src.market import Symbol, Currency, get_instrument
from src.forms.portfolio import AddPortfolioForm, generate_edit_portfolio_form


portfolio_blueprint = Blueprint("portfolio", __name__, url_prefix="/portfolio")


@portfolio_blueprint.route("/list", methods=["GET"])
@login_required
def list_portfolios():
    """List portfolios of the user including current market values."""

    portfolios = current_user.portfolios
    portfolios.sort(key=lambda x: x.primary, reverse=True)

    if not portfolios:
        flash("Add a custom portfolio!")

    return render_template("portfolio/list_portfolios.html", portfolios=portfolios)


@portfolio_blueprint.route("/add_portfolio", methods=["GET", "POST"])
@login_required
def add_portfolio():
    """Add a new portfolio."""

    form = AddPortfolioForm()
    if form.validate_on_submit():

        symbol = Symbol(form.benchmark.data)
        security = get_instrument(symbol)
        currency = Currency(form.reporting_currency.data)

        portfolio = Portfolio(
            form.port_name.data,
            form.port_type.data,
            currency,
            security,
        )
        current_user.add_portfolio(portfolio)

        if current_user.get_primary_portfolio() is None:
            portfolio.set_as_primary()
        return redirect(url_for("portfolio.list_portfolios"))
    return render_template("portfolio/add_portfolio.html", form=form)


@portfolio_blueprint.route("/edit/<int:portfolio_id>", methods=["GET", "POST"])
@login_required
def edit_portfolio(portfolio_id):
    """Edit an existing portfolio."""

    port = Portfolio.find_by_id(portfolio_id)
    edit_form = generate_edit_portfolio_form(port)
    form: FlaskForm = edit_form()
    if form.validate_on_submit():
        symbol = Symbol(form.benchmark.data)
        security = get_instrument(symbol)
        currency = Currency(form.reporting_currency.data)
        port.edit(
            form.port_name.data,
            currency,
            form.port_type.data,
            security,
        )
        return redirect(url_for("portfolio.list_portfolios"))
    return render_template(
        "portfolio/edit_portfolio.html", form=form, portfolio_id=portfolio_id
    )


@portfolio_blueprint.route("/delete/<int:portfolio_id>", methods=["GET"])
@login_required
def delete_portfolio(portfolio_id):
    """Delete an existing portfolio along with its positions as well as orders."""

    port = Portfolio.find_by_id(portfolio_id)
    port.delete_from_db()
    return redirect(url_for("portfolio.list_portfolios"))


@portfolio_blueprint.route("/set_primary/<int:portfolio_id>", methods=["GET"])
@login_required
def set_portfolio_primary(portfolio_id):
    """Set a portfolio primary which will be viewed at the top when listing portfolios."""

    primary_portfolio: Portfolio = current_user.get_primary_portfolio()

    if primary_portfolio:
        primary_portfolio.primary = False

    current_portfolio = Portfolio.find_by_id(portfolio_id)
    current_portfolio.set_as_primary()

    return redirect(url_for("portfolio.list_portfolios"))


@portfolio_blueprint.route("/activate_daily_report/<int:portfolio_id>", methods=["GET"])
@login_required
def activate_daily_report(portfolio_id):
    """Activate daily report for a given portfolio."""

    port = Portfolio.find_by_id(portfolio_id)
    port.daily_report.activate()

    return redirect(url_for("portfolio.list_portfolios"))


@portfolio_blueprint.route(
    "/deactivate_daily_report/<int:portfolio_id>", methods=["GET"]
)
@login_required
def deactivate_daily_report(portfolio_id):
    """Activate daily report for a given portfolio."""

    port = Portfolio.find_by_id(portfolio_id)
    port.daily_report.deactivate()

    return redirect(url_for("portfolio.list_portfolios"))
