from flask import Blueprint, request, session, url_for, render_template, redirect
import datetime

from src.environment.user_activities import Position, Portfolio, Order
from src.views.utils import requires_login, _modify_position_list, _check_position_validity, _extract_open_orders, _validate_order


order_blueprint = Blueprint("order", __name__)


@order_blueprint.route("/<string:portfolio_name>/view_orders/<string:symbol>/", methods=["GET"])
@requires_login
def list_orders(portfolio_name: str, symbol: str):
    port = Portfolio.find_by_name(portfolio_name, session["email"])
    position = Position.find_by_symbol(symbol, port.portfolio_id)
    all_orders = Order.find_all(position_id=position.position_id)
    open_orders = _extract_open_orders(all_orders)
    return render_template("order/order.html", portfolio_name=portfolio_name, symbol=position.symbol, order_list=open_orders, portfolio=port)


@order_blueprint.route("/<string:portfolio_name>/delete_order/<string:symbol>/<int:order_id>/", methods=["GET"])
@requires_login
def delete_order(portfolio_name: str, symbol: str, order_id: int):
    port = Portfolio.find_by_name(portfolio_name, session["email"])
    order = Order.find_by_id(order_id)
    order.delete_order()
    if port.source == "Questrade":
        return redirect(url_for("position.sync_position_list", portfolio_name=portfolio_name))
    else:
        return redirect(url_for("position.update_position", portfolio_name=portfolio_name, symbol=symbol))


@order_blueprint.route("/<string:portfolio_name>/edit_order/<string:symbol>/<int:order_id>/", methods=["GET", "POST"])
@requires_login
def edit_order(portfolio_name: str, symbol: str, order_id: int):
    
    port = Portfolio.find_by_name(portfolio_name, session["email"])
    order = Order.find_by_id(order_id)
    if request.method == "POST":
        try:
            date = datetime.datetime.strptime(request.form["date"], "%Y-%m-%d")
            time = datetime.datetime.strptime(request.form["time"], "%H:%M").time()
        except ValueError: # Add exception
            return render_template("order/edit_order.html",
                portfolio=port,
                order=order,
                required_amount=None,
                error_message="Invalid date or time provided, please try again."
                )
        
        exec_datetime = datetime.datetime.combine(date, time)
        position = Position.find_by_symbol(symbol, port.portfolio_id)

        if request.form["fee-currency"] == "USD":
            pass # TODO: convert to CAD by using exchange rate

        order.update_order(
            symbol,
            "Custom",
            "Executed",
            int(request.form["order_quantity"]),
            request.form["order_type"],
            33, # TODO: pull this from Market Data Manager
            exec_datetime,
            request.form["strategy"],
            port.portfolio_id,
            float(request.form["fee"]),
            position.position_id,
        )
        
        if port.source == "Questrade":
            return redirect(url_for("position.sync_position_list", portfolio_name=portfolio_name))
        else:
            return redirect(url_for("position.update_position", portfolio_name=portfolio_name, symbol=symbol))

    return render_template("order/edit_order.html",
        portfolio=port,
        order=order,
        required_amount=None,
        error_message=None)

# TODO: required_amount can be negative (which means the position is "sell", fix it!)
@order_blueprint.route("/<string:portfolio_name>/add_order/<string:symbol>/<float:required_amount>/", methods=["GET", "POST"])
@order_blueprint.route("/<string:portfolio_name>/add_order/", methods=["GET", "POST"])
@requires_login
def add_order(portfolio_name: str, symbol: str = None, required_amount: int = None):
    port = Portfolio.find_by_name(portfolio_name, session["email"])
    if request.method == "POST":
        try:
            # TODO: quantity should be positive integer
            # TODO: symbol should be accurate
            # TODO: if currency is USD convert it to CAD
            # TODO: check if the same order is in database
            date = datetime.datetime.strptime(request.form["date"], "%Y-%m-%d")
            time = datetime.datetime.strptime(request.form["time"], "%H:%M").time()
            exec_datetime = datetime.datetime.combine(date, time)
        except ValueError: # Add exception
            return render_template(
                "order/add_order.html",
                portfolio=port,
                symbol=symbol,
                required_amount=required_amount,
                error_message="Invalid date or time provided, please try again."
            )
    
        Order.add_order(
            request.form["symbol"],
            "Custom",
            "Executed",
            int(request.form["order_quantity"]),
            request.form["order_type"],
            33, # TODO: pull this from Market Data Manager
            exec_datetime,
            request.form["strategy"],
            port.portfolio_id,
            float(request.form["fee"]),
            Position.find_by_symbol(symbol, port.portfolio_id).position_id if symbol else None,
        )

        if port.source == "Custom":
            return redirect(url_for("position.update_position", portfolio_name=portfolio_name, symbol=request.form["symbol"]))

        return redirect(url_for("position.sync_position_list", portfolio_name=portfolio_name))


    return render_template(
        "order/add_order.html",
        portfolio=port,
        symbol=symbol,
        required_amount=required_amount,
        error_message=None
    )
