"""Reference data"""

from src.market.basic import Currency, FX
from src.market.security import Equity, ETF, Index
from src.market.symbol import Symbol

# Currencies
cad_ccy = Currency("CAD")
usd_ccy = Currency("USD")
eur_ccy = Currency("EUR")
try_ccy = Currency("TRY")

# FX
usdcad = FX(usd_ccy, cad_ccy)
eurusd = FX(eur_ccy, usd_ccy)

# Securities
aapl = Equity(usd_ccy, Symbol("AAPL"))
tsla = Equity(usd_ccy, Symbol("TSLA"))
ry_to = Equity(cad_ccy, Symbol("RY.TO"))
pbw = ETF(usd_ccy, Symbol("PBW"))
gspc = Index(usd_ccy, Symbol("^GSPC"))