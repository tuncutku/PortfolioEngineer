import datetime
import pandas as pd
import matplotlib.pyplot as plt

from src.environment.utils.base import BaseModel
from src.extensions import db
from src.market_data.yahoo import YFinance
from src.environment.utils.types import *


class Report(BaseModel):
    __tablename__ = "report"

    id = db.Column(db.Integer(), primary_key=True)
    portfolio_id = db.Column(db.Integer(), db.ForeignKey("portfolios.id"))
    creation_date = db.Column(db.DateTime(), default=datetime.datetime.now)

    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.set_default_dates()
        self.set_portfolio_df()
        self.set_benchmark_df()
        self.set_value_df()
        self.set_return_df()

    def set_default_dates(self):
        df_raw_data = self.portfolio.positions_df()
        self.__start = df_raw_data.index.date.min()
        self.__end = datetime.date.today()

    def set_benchmark_df(self):
        md_provider = YFinance([self.portfolio.benchmark])
        self.benchmark_df = md_provider.get_historical_quotes(self.__start, self.__end)

    def set_portfolio_df(self):
        df_raw_data = self.portfolio.positions_df()
        df_raw_data.index = df_raw_data.index.date
        self.__raw_df = self.extend_df_with_market_data(df_raw_data)

    def extend_df_with_market_data(self, df_port):
        md_provider = YFinance(self.portfolio.symbols)
        df_raw_quotes = md_provider.get_historical_quotes(self.__start, self.__end)

        # Set date range for reindex
        date_range = pd.bdate_range(
            start=self.__start, end=df_raw_quotes.index.date.max()
        )
        df_port = df_port.reindex(date_range)

        # Extend portfolio df with market data
        for symbol in self.portfolio.symbols:
            df_port[symbol]["Quantity"] = df_port[symbol]["Quantity"].fillna(
                method="ffill"
            )
            df_port[symbol]["Quote"] = df_raw_quotes[symbol]

        return df_port

    def set_value_df(self):

        position_values = pd.DataFrame()
        port_value = pd.DataFrame()

        for symbol in self.portfolio.symbols:
            position_values[symbol] = (
                self.__raw_df[symbol]["Quantity"] * self.__raw_df[symbol]["Quote"]
            )
        self.position_values = position_values
        self.port_value = position_values.sum(axis=1)

    def set_return_df(self, return_period=1):

        port_weights = self.position_values.div(self.port_value, axis=0)

        self.benchmark_return = self.benchmark_df.pct_change(return_period)
        self.position_return = self.position_values.pct_change(return_period)
        self.portfolio_return = pd.DataFrame(
            (port_weights * self.position_return).sum(axis=1),
            columns=[self.portfolio.name],
        )

        f = lambda df: (1 + df).cumprod()
        self.benchmark_cum_return = f(self.benchmark_return)
        self.portfolio_cum_return = f(self.portfolio_return)

    def get_returns(self):
        return {
            "Position Return": self.position_return,
            "Benchmark Return": self.benchmark_return,
            "Portfolio Return": self.portfolio_return,
            "Benchmark Cumulative Return": self.benchmark_cum_return,
            "Portfolio Cumulative Return": self.portfolio_cum_return,
        }
