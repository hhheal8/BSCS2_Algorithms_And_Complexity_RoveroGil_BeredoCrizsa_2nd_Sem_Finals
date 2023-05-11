import mysql.connector

from mysql.connector import Error
from typing import List

FOODCOURT_SEAT_RESERVATION_DATABASE = "foodcourt_seat_reservation"

FOODCOURT_SEAT_RESERVATION_TABLE1 = "waltermart_candelaria_foodcourt"
FOODCOURT_SEAT_RESERVATION_TABLE2 = "waltermart_candelaria_storename"
FOODCOURT_SEAT_RESERVATION_TABLE3 = "waltermart_candelaria_timereservation"

class DatabaseManager:
  def __init__(self, host: str, user: str, password: str, database: str) -> None:
    self.connection = mysql.connector.connect(
      host = host,
      user = user,
      password = password,
      database = database
    )
    self.cursor = self.connection.cursor()
    
  def is_database_exists(self, database_name: str) -> bool:
    try:
      self.cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
      result = self.cursor.fetchone()
      return result is not None

    except mysql.connector.Error as error:
      print(f"\nERROR CHECKING DATABASE EXISTENCE: {error}\n")
      return False

  def create_tables(self) -> None:
    CREATE_TABLE_QUERIES: List[str] = [
      f"""
      CREATE TABLE IF NOT EXISTS {FOODCOURT_SEAT_RESERVATION_TABLE2} (
        store_name VARCHAR(100) PRIMARY KEY,
        number_customer INT,
        seat_fee FLOAT
      )
      """,

      f"""
      CREATE TABLE IF NOT EXISTS {FOODCOURT_SEAT_RESERVATION_TABLE1} (
        store_name_id VARCHAR(100) PRIMARY KEY,
        time_reservation DATETIME,
        number_customer INT,
        seat_fee FLOAT,
        store_name VARCHAR(100),
        FOREIGN KEY (store_name) REFERENCES {FOODCOURT_SEAT_RESERVATION_TABLE2}(store_name)
      )
      """,

      f"""
      CREATE TABLE IF NOT EXISTS {FOODCOURT_SEAT_RESERVATION_TABLE3} (
        store_name VARCHAR(100),
        time_reservation DATETIME,
        number_customer INT
      )
      """
    ]

    for QUERIES in CREATE_TABLE_QUERIES:
      self.cursor.execute(QUERIES)
    
    self.connection.commit()

    print("TABLES CREATED SUCCESSFULLY.\n")

  def read_data(self, table_name: str) -> None:
    try:
      self.cursor.execute(f"SELECT * FROM {table_name}")  
      rows = self.cursor.fetchall()  
      for row in rows:
        print(row)

    except mysql.connector.Error as error:
      print(f"\nERROR READING DATA FROM: {error}\n")

def main() -> None:
  sql = DatabaseManager("localhost", "root", "", FOODCOURT_SEAT_RESERVATION_DATABASE)

  if sql.is_database_exists(FOODCOURT_SEAT_RESERVATION_DATABASE) != False:
    sql.create_tables()
    
  if sql.is_database_exists(FOODCOURT_SEAT_RESERVATION_DATABASE) != False:
    sql.read_data(FOODCOURT_SEAT_RESERVATION_TABLE1)
  
if __name__ == "__main__":
  main()