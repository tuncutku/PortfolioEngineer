from src.db.utils.connection import database_manager

CREATE_USERS = """CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT);"""
CREATE_USER_TOKEN = """CREATE TABLE IF NOT EXISTS user_token (
    access_token TEXT,
    api_server TEXT,
    expires_at TEXT,
    refresh_token TEXT,
    token_type TEXT,
    email TEXT,
    FOREIGN KEY (email) REFERENCES users (email) ON UPDATE CASCADE ON DELETE CASCADE,
    id SERIAL PRIMARY KEY);"""
CREATE_PORTFOLIO = """CREATE TABLE IF NOT EXISTS portfolio (
    name TEXT,
    source TEXT,
    status TEXT,
    type TEXT,
    email TEXT,
    questrade_id INT,
    FOREIGN KEY (email) REFERENCES users (email) ON UPDATE CASCADE ON DELETE CASCADE,
    id SERIAL PRIMARY KEY);"""
CREATE_POSITION = """CREATE TABLE IF NOT EXISTS position (
    symbol TEXT,
    source TEXT,
    quantity INT,
    state TEXT,
    portfolio_id INT,
    FOREIGN KEY (portfolio_id) REFERENCES portfolio (id) ON DELETE CASCADE,
    id SERIAL PRIMARY KEY);"""
CREATE_ORDERS = """CREATE TABLE IF NOT EXISTS orders (
    symbol TEXT,
    source TEXT,
    state TEXT,
    quantity DECIMAL,
    side TEXT,
    average_price DECIMAL,
    time TIMESTAMP,
    strategy TEXT,
    portfolio_id INT,
    fee DECIMAL,
    position_id INT,
    FOREIGN KEY (portfolio_id) REFERENCES portfolio (id) ON DELETE CASCADE,
    FOREIGN KEY (position_id) REFERENCES position (id) ON DELETE CASCADE,
    id SERIAL PRIMARY KEY);"""

def create_tables():
    with database_manager() as cursor:
        cursor.execute(CREATE_USERS)
        cursor.execute(CREATE_USER_TOKEN)
        cursor.execute(CREATE_PORTFOLIO)
        cursor.execute(CREATE_POSITION)
        cursor.execute(CREATE_ORDERS)