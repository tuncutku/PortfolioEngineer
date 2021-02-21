class Exchange:
    TSX = "Toronto Stock Exchange"
    TSXV = "Toronto Venture Exchange"
    CNSX = "Canadian National Stock Exchange"
    MX = "Montreal Exchange"
    NASDAQ = "NASDAQ"
    NYSE = "New York Stock Exchange"
    NYSEAM = "NYSE AMERICAN"
    ARCA = "NYSE Arca"
    OPRA = "Option Reporting Authority"
    PinkSheets = "Pink Sheets"
    OTCBB = "OTC Bulletin Board"


class OrderSideType:
    Buy = "Buy"
    Sell = "Sell"
    Short = "Sell Short"
    Cov = "Cover the short"
    BTO = "Buy-to-Open"
    STC = "Sell-to-Close"
    STO = "Sell-to-Open"
    BTC = "Buy-to-Close"


class OptionType:
    Call = "Call"
    Put = "Put"


class OptionDurationType:
    Weekly = "Weekly expiry cycle"
    Monthly = "Monthly expiry cycle"
    Quarterly = "Quarterly expiry cycle"
    LEAP = "Long-term Equity Appreciation contracts"


class OptionExerciseType:
    American = "American option"
    European = "European option"


class OptionStrategyType:
    CoveredCall = "Covered Call"
    MarriedPuts = "Married Put"
    VerticalCallSpread = "Vertical Call"
    VerticalPutSpread = "Vertical Put"
    CalendarCallSpread = "Calendar Call"
    CalendarPutSpread = "Calendar Put"
    DiagonalCallSpread = "Diagonal Call"
    DiagonalPutSpread = "Diagonal Put"
    Collar = "Collar"
    Straddle = "Straddle"
    Strangle = "Strangle"
    ButterflyCall = "Butterfly Call"
    ButterflyPut = "Butterfly Put"
    IronButterfly = "Iron Butterfly"
    CondorCall = "Condor"
    Custom = "Custom"


class SecurityType:
    Cash = "Cash"
    Stock = "Common and preferred equities, ETFs, ETNs, units, ADRs, etc."
    ETF = "Exchange traded fund"
    Option = "Equity and index options."
    Bond = "Debentures, notes, bonds, both corporate and government."
    Right = "Equity or bond rights and warrants."
    Gold = "Physical gold (coins, wafers, bars)."
    MutualFund = "Canadian or US mutual funds."
    Index = "Stock indices (e.g., Dow Jones)."
    CryptoCurrency = "Crypto currency"


class Currency:
    CAD = "CAD"
    USD = "USD"


class PortfolioType:
    tfsa = "TFSA"
    rrsp = "RRSP"
    margin = "Margin"
    cash = "Cash"
    custom = "Custom"


class PortfolioStatus:
    active = "Active"
    inactive = "Inactive"


class PortfolioSource:
    questrade = "Questrade"
    custom = "Custom"