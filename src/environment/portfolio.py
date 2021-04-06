from datetime import datetime, date
import pandas as pd

from src.reports.report import Report

from src.environment.utils.base import BaseModel
from src.environment.alerts.daily import DailyReport
from src.extensions import db
from src.market_data.provider import YFinance
from src.environment.utils.types import *


class Portfolio(BaseModel):
    __tablename__ = "portfolios"

    user_id: int = db.Column(db.Integer(), db.ForeignKey("users.id"))
    date: date = db.Column(db.Date(), default=datetime.now)
    name: str = db.Column(db.String(255), nullable=False)
    portfolio_type: str = db.Column(db.String(255), nullable=False)
    reporting_currency: str = db.Column(db.String(3), nullable=False)
    benchmark: str = db.Column(db.String(3), nullable=False)
    primary: bool = db.Column(db.Boolean(), default=False)

    daily_report = db.Column(db.Boolean(), default=False)
    positions = db.relationship(
        "Position",
        backref="portfolio",
        cascade="all, delete-orphan",
    )
    daily_report: DailyReport = db.relationship(
        "DailyReport",
        back_populates="portfolio",
        uselist=False,
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Portfolio {self.name}.>"

    @property
    def symbols(self):
        return [pos.symbol for pos in self.positions]

    @property
    def total_mkt_value(self) -> float:

        fx_symbol = "USDCAD=X"
        fx_md = YFinance([fx_symbol])
        quote = fx_md.get_current_quotes(decimal=2)

        value = 0
        for pos in self.positions:
            pos_mkt_cap = (
                pos.market_cap
                if pos.currency == self.reporting_currency
                else pos.market_cap * float(quote[fx_symbol])
            )
            value += pos_mkt_cap
        return value

    @classmethod
    def get_primary(cls, user):
        return cls.query.filter_by(user=user, primary=True).first()

    def set_as_primary(self) -> None:
        self.primary = True
        db.session.commit()

    def edit(self, name, currency, port_type, benchmark) -> None:
        self.name = name
        self.reporting_currency = currency
        self.portfolio_type = port_type
        self.benchmark = benchmark
        db.session.commit()

    def to_dict(self) -> dict:

        position_list = [position.to_dict() for position in self.positions]
        position_list.sort(key=lambda x: x.get("Market Cap"))

        return {
            "id": self.id,
            "Name": self.name,
            "Portfolio type": self.portfolio_type,
            "Reporting currency": self.reporting_currency,
            "Primary": self.primary,
            "Creation date": self.date,
            "Total market value": "{:,.2f}".format(self.total_mkt_value),
            "Benchmark": self.benchmark,
            "Positions": position_list,
        }

    def positions_df(self) -> pd.DataFrame:

        # Raise error if list is empty.
        position_df_list = [position.orders_df() for position in self.positions]
        position_symbol_list = [position.symbol for position in self.positions]

        return pd.concat(position_df_list, axis=1, keys=position_symbol_list)

    def generate_report(self) -> Report:
        return Report(self)
