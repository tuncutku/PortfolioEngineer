"""Portfolio forms"""

from flask_wtf import FlaskForm as Form
from wtforms import StringField, SelectField
from wtforms.validators import (
    DataRequired,
    Length,
)

from src.environment import Portfolio
from src.market import Currency
from src.market.types import PortfolioType
from src.forms.validators import PortfolioName, Ticker

port_type_choices = [
    (PortfolioType.custom, PortfolioType.custom),
    (PortfolioType.margin, PortfolioType.margin),
    (PortfolioType.tfsa, PortfolioType.tfsa),
    (PortfolioType.cash, PortfolioType.cash),
    (PortfolioType.rrsp, PortfolioType.rrsp),
]

currency_choices = [("CAD", Currency("CAD")), ("USD", Currency("USD"))]


class AddPortfolioForm(Form):
    """Add portfolio form."""

    port_name = StringField(
        u"Portfolio Name", [DataRequired(), Length(max=20), PortfolioName()]
    )
    port_type = SelectField(u"Portfolio Type", default=1, choices=port_type_choices)
    reporting_currency = SelectField(
        u"Reporting Currency", default=1, choices=currency_choices
    )
    benchmark = StringField(u"Benchmark", [DataRequired(), Ticker()], default="^GSPC")


def generate_edit_portfolio_form(portfolio: Portfolio) -> Form:
    """Function that generates an instance of EditPortfolioForm and sets default arguments."""

    class EditPortfolioForm(Form):
        """Edit portfolio form."""

        port_name = StringField(
            u"Portfolio Name",
            [DataRequired(), Length(max=20), PortfolioName(exclude=portfolio.name)],
            default=portfolio.name,
        )
        port_type = SelectField(
            u"Portfolio Type",
            choices=port_type_choices,
            default=portfolio.portfolio_type,
        )
        reporting_currency = SelectField(
            u"Reporting Currency",
            choices=currency_choices,
            default=portfolio.reporting_currency,
        )
        benchmark = StringField(
            u"Benchmark",
            [DataRequired(), Ticker()],
            default=portfolio.benchmark.symbol.symbol,
        )

    return EditPortfolioForm
