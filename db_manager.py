from sqlalchemy import create_engine
import logging

class DatabaseManager:
  def __init__(self,config):
    self.url = f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    try:
      self.engine = create_engine(self.url)
      logging.info("Database engine has started successfully")
    except Exception as e:
      logging.error(f"While engine starting thrown an error {e}")

  def save_to_table(self,df,table_name):
    try:
      df.to_sql(table_name,self.engine,if_exists='replace', index = True)
      return True
    except Exception as e:
      logging.error(f"While saving data to table {table_name} thrown an error {e}")
      return False
