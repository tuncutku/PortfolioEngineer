"""Order endpoints."""

from flask import Blueprint, url_for, render_template, redirect
from flask_login import login_required

from src.extensions import db
from src.environment import Portfolio, Position, Order
from src.forms.order import AddOrderForm, generate_edit_order_form
from src.market import Symbol
from src.views.utils.yfinance import security_map
from src.views.utils.common import get_security


order_blueprint = Blueprint("order", __name__, url_prefix="/order")


@order_blueprint.route("/delete_order/<int:order_id>", methods=["GET"])
@login_required
def delete_order(order_id: int):

    order = Order.find_by_id(order_id)
    order.delete_from_db()

    return redirect(url_for("portfolio.list_portfolios"))


@order_blueprint.route("/edit/<int:order_id>", methods=["GET", "POST"])
@login_required
def edit_order(order_id: int):
    order = Order.find_by_id(order_id)
    form = generate_edit_order_form(order)

    if form.validate_on_submit():
        order.edit(
            form.quantity.data,
            form.direction.data,
            form.cost.data,
            form.exec_datetime.data,
        )
        return redirect(url_for("portfolio.list_portfolios"))

    return render_template("order/edit_order.html", form=form, order_id=order_id)


@order_blueprint.route("/<int:portfolio_id>/add_order", methods=["GET", "POST"])
@login_required
def add_order(portfolio_id):

    form = AddOrderForm()
    if form.validate_on_submit():
        symbol = Symbol(form.symbol.data)

        port = Portfolio.find_by_id(portfolio_id)
        pos = port.get_position_by_symbol(symbol)

        if pos is None:
            security = get_security(symbol)
            pos = port.add_position(security)

        pos.add_order(
            form.quantity.data,
            form.direction.data,
            form.cost.data,
            form.exec_datetime.data,
        )

        return redirect(url_for("portfolio.list_portfolios"))

    return render_template("order/add_order.html", form=form, portfolio_id=portfolio_id)
