import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME")
}

# To add parameter list in there
SYMBOLS = {
    "XAUUSD": "GC=F",
    "XAGUSD": "SI=F",
    "BRENT": "BZ=F",
    "BTCUSD": "BTC-USD"
}

# To arrange data intervals
FETCH_SETTINGS = {
    "period": "1y",
    "interval": "1d"
}