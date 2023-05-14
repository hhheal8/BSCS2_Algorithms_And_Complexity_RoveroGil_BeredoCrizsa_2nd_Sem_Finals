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
      host=host,
      user=user,
      password=password,
      database=database
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
    
  def create_database(self) -> None:
    try:
      self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {FOODCOURT_SEAT_RESERVATION_DATABASE}")
      self.connection.commit()
      
      print("DATABASE CREATED SUCCESSFULLY.\n")
      
    except mysql.connector.Error as error:
      print(f"\nERROR CREATING DATABASE: {error}\n")
          
  def create_tables(self) -> None:
    CREATE_TABLE_QUERIES: List[str] = [
      f"""
      CREATE TABLE IF NOT EXISTS {FOODCOURT_SEAT_RESERVATION_TABLE1} (
        store_name_id VARCHAR(100) PRIMARY KEY,
        seat_fee FLOAT
      )
      """,

      f"""
      CREATE TABLE IF NOT EXISTS {FOODCOURT_SEAT_RESERVATION_TABLE2} (
        store_name_id VARCHAR(100) PRIMARY KEY,
        store_name VARCHAR(100)
      )
      """,

      f"""
      CREATE TABLE IF NOT EXISTS {FOODCOURT_SEAT_RESERVATION_TABLE3} (
        store_name_id VARCHAR(100),
        time_reservation DATETIME,
        number_customer INT,
        FOREIGN KEY (store_name_id) REFERENCES {FOODCOURT_SEAT_RESERVATION_TABLE1}(store_name_id)
      )
      """
    ]
    
    for query in CREATE_TABLE_QUERIES:
      self.cursor.execute(query)
      
    self.connection.commit()
    
    print("TABLES CREATED SUCCESSFULLY.\n")

  def insert_data(self, table_name: str, data: List[dict]) -> None:
    """
    Inserts data into the specified table.
    """
    try:
      for item in data:
        columns = ", ".join(item.keys())
        values = ", ".join(f"'{value}'" for value in item.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(query)
        self.connection.commit()
      print("Data inserted successfully.")
      
    except mysql.connector.Error as error:
      print(f"\nERROR INSERTING DATA: {error}\n")

  def read_data(self, table_name: str) -> None:
    try:
      self.cursor.execute(f"SELECT * FROM {table_name}")  
      rows = self.cursor.fetchall()  
      for row in rows:
        print(row)
        
    except mysql.connector.Error as error:
      print(f"\nERROR READING DATA FROM: {error}\n")

  def update_data(self, table_name: str, column_values: dict, condition: str = "") -> None:
    """
    Updates data in the specified table with the given column-value pairs and condition.
    """
    try:
      columns = ", ".join(f"{column} = '{value}'" for column, value in column_values.items())
      query = f"UPDATE {table_name} SET {columns}"
      if condition:
        query += f" WHERE {condition}"
      self.cursor.execute(query)
      self.connection.commit()
      print("Data updated successfully.")
      
    except mysql.connector.Error as error:
      print(f"\nERROR UPDATING DATA: {error}\n")

  def delete_data(self, table_name: str, condition: str = "") -> None:
    """
    Deletes data from the specified table based on the given condition.
    """
    try:
      query = f"DELETE FROM {table_name}"
      if condition:
        query += f" WHERE {condition}"
      self.cursor.execute(query)
      self.connection.commit()
      print("Data deleted successfully.")
      
    except mysql.connector.Error as error:
      print(f"\nERROR DELETING DATA: {error}\n")
          
def main() -> None:
  sql = DatabaseManager("localhost", "root", "", FOODCOURT_SEAT_RESERVATION_DATABASE)

  sql.create_database()

  if sql.is_database_exists(FOODCOURT_SEAT_RESERVATION_DATABASE) != False:
    sql.create_tables()

  storename_data = [
    {
      "store_name_id": "S01_P_C",
      "store_name": "Potato Corner"
    },
    {
      "store_name_id": "S05_K_B_H",
      "store_name": "Kirmz B Hub"
    },
    {
      "store_name_id": "S06_S_O",
      "store_name": "Sisig-OK"
    }
  ]
  
  sql.insert_data(FOODCOURT_SEAT_RESERVATION_TABLE2, storename_data)

  data = [
    {
      "store_name_id": "S01_P_C",
      "seat_fee": 10.00
    },
    {
      "store_name_id": "S05_K_B_H",
      "seat_fee": 15.00
    },
    {
      "store_name_id": "S06_S_O",
      "seat_fee": 25.00
    }
  ]
  
  sql.insert_data(FOODCOURT_SEAT_RESERVATION_TABLE1, data)
  
  reservation_data = [
    {
      "store_name_id": "S01_P_C",
      "time_reservation": "2023-05-12 11:00:00",
      "number_customer": 4
    },
    {
      "store_name_id": "S01_P_C",
      "time_reservation": "2023-05-12 13:10:00",
      "number_customer": 3
    },
    {
      "store_name_id": "S01_P_C",
      "time_reservation": "2023-05-12 9:20:00",
      "number_customer": 8
    },
    {
      "store_name_id": "S05_K_B_H",
      "time_reservation": "2023-05-12 11:40:00",
      "number_customer": 2
    },
    {
      "store_name_id": "S05_K_B_H",
      "time_reservation": "2023-05-12 14:30:00",
      "number_customer": 6
    }
  ]

  sql.insert_data(FOODCOURT_SEAT_RESERVATION_TABLE3, reservation_data)

  sql.read_data(FOODCOURT_SEAT_RESERVATION_TABLE1)
  sql.read_data(FOODCOURT_SEAT_RESERVATION_TABLE2)
  sql.read_data(FOODCOURT_SEAT_RESERVATION_TABLE3)

  update_values = {
    "seat_fee": 20.00
  }
  condition = "store_name_id = 'S06_S_O'"
  sql.update_data(FOODCOURT_SEAT_RESERVATION_TABLE1, update_values, condition)

  condition = "store_name_id = 'S01_P_C'"
  sql.delete_data(FOODCOURT_SEAT_RESERVATION_TABLE3, condition)

  sql.read_data(FOODCOURT_SEAT_RESERVATION_TABLE3)

if __name__ == "__main__":
  main()