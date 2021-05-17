import os
import tempfile
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
db_file = tempfile.NamedTemporaryFile()

load_dotenv()


class ConfigBase(object):
    """Base class for configuration."""

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SECURITY_PASSWORD_SALT = os.environ.get("SECRET_KEY")
    # POSTS_PER_PAGE = 10

    # Celery config
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    RESULT_BACKEND = "redis://localhost:6379/0"

    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail config
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get("MAIL_SERVER_EMAIL")
    MAIL_PASSWORD = os.environ.get("MAIL_SERVER_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_SERVER_EMAIL")

    # Cash config
    CACHE_TYPE = "redis"
    CACHE_REDIS_HOST = ""
    CACHE_REDIS_PORT = "6379"
    CACHE_REDIS_PASSWORD = ""
    CACHE_REDIS_DB = "0"


class ProdConfig(ConfigBase):
    """Configuration for production."""

    CELERY_BROKER_URL = "redis://redis:6379/0"
    RESULT_BACKEND = "redis://redis:6379/0"

    WTF_CSRF_TIME_LIMIT = None


class DevConfig(ConfigBase):
    """Configuration for development."""

    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = "simple"

    WTF_CSRF_TIME_LIMIT = None


class TestConfig(ConfigBase):
    """Configuration for testing."""

    TESTING = True

    DEBUG = True
    DEBUG_TB_ENABLED = False
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, db_file.name)


config = {
    "production": ProdConfig,
    "development": DevConfig,
    "testing": TestConfig,
}
