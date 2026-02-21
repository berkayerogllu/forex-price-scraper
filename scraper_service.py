import yfinance as yf
import pandas as pd
from ta import add_all_ta_features
import logging

class ScraperService:
  @staticmethod
  def fetch_and_enrich(ticker,period,interval):
    try:
      logging.info(f"{ticker} data is fetching...")
      df = yf.download(ticker,period = period, interval = interval)

      if df.empty:
        logging.warning(f"the data is returned empty for {ticker}")
        return None
      
      if isinstance(df.columns,pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

      logging.info(f"{ticker} tehcnical analysis data is calculating...")

      df = add_all_ta_features(
                df, 
                open="Open", 
                high="High", 
                low="Low", 
                close="Close", 
                volume="Volume", 
                fillna=True
            )
      return df

    except Exception as e:
      logging.error(f"Error on scraper service ({ticker}): {e}")
      return None