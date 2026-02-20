import logging
from config import DB_CONFIG, SYMBOLS, FETCH_SETTINGS
from db_manager import DatabaseManager
from scraper_service import ScraperService

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PriceScraperApp:
    def __init__(self):
        self.db = DatabaseManager(DB_CONFIG)
        self.scraper = ScraperService()

    def run(self):
        logging.info("Forex Price scraper has started to working.")
        
        for name, ticker in SYMBOLS.items():
            df = self.scraper.fetch_and_enrich(
                ticker, 
                FETCH_SETTINGS["period"], 
                FETCH_SETTINGS["interval"]
            )
            
            if df is not None:
                table_name = f"price_{name.lower()}"
                if self.db.save_to_table(df, table_name):
                    logging.info(f"✅ Success: {name} -> {table_name}")
            else:
                logging.warning(f"⚠️ {name} for data could not fetch")

if __name__ == "__main__":
    app = PriceScraperApp()
    app.run()