from flask import Blueprint, request, session, url_for, render_template, redirect

from src.environment.user_activities import User, Portfolio
from src.environment.user_activities.utils import UserError, requires_login, requires_questrade_access, PortfolioNotFoundError
from src.views.utils import check_and_update_portfolio, add_portfolio, _valide_portfolio_name

from src.questrade import Questrade

account_blueprint = Blueprint("account", __name__)

@account_blueprint.route("/account", methods=["GET", "POST", "PUT", "DELETE"])
@requires_login
def list_portfolios():
    try:
        port_list = Portfolio.find_all(session["email"])
        return render_template("account/account.html", port_list = port_list, error_message = None)
    except PortfolioNotFoundError as e:
        port_list = None
        return render_template("account/account.html", port_list = port_list, error_message = e.message)

@account_blueprint.route("/update", methods=["GET"])
@requires_login
@requires_questrade_access
def update_portfolio_list():
    
    new_port_list = list()
    q = Questrade()

    # List the Questrade portfolios saved in database, and pulled Questrade portfolios
    port_list_questrade = [port for port in q.accounts["accounts"]]
    port_list_db = [port for port in Portfolio.find_all(session["email"]) if port.source == "Questrade"]
    port_id_list_db = [port.questrade_id for port in port_list_db]

    # Insert a new portfolio or update an existing portfolio
    for port_questrade in port_list_questrade:
        port_id = int(port_questrade["number"])
        if port_id in port_id_list_db:
            # Get Portfolio by Questrade id
            port_db = port_list_db[port_id_list_db.index(port_id)]
            check_and_update_portfolio(port_db, port_questrade)
        else:
            add_portfolio(port_questrade, session["email"])
    
    #TODO: add functionality to delete portfolios if it doesn't exist on Questrade

    return redirect(url_for("account.list_portfolios"))

@account_blueprint.route("/edit", methods=["GET", "PUT"])
@requires_login
def edit_portfolio():
    pass

@account_blueprint.route("/delete", methods=["GET", "POST", "PUT", "DELETE"])
@requires_login
def delete_portfolio():
    pass

@account_blueprint.route("/portfolio_name", methods=["GET", "POST"])
@requires_login
def set_portfolio_name():
    if request.method == "POST":
        name = request.form["name"]
        if not _valide_portfolio_name(name, session["email"]):
            return render_template("account/set_portfolio_name.html", error_message = None)
        else:
            # Portfolio type can be specified my the user. Add a drop down menu.
            Portfolio.add_portfolio(name, "Custom", "Active", "Invalid", session["email"])
            return render_template("order/new_order.html")
    return render_template("account/set_portfolio_name.html", error_message = None)
