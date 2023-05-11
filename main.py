import mysql.connector
from mysql.connector import Error
from typing import Any

DATABASE_NAME: str = "waltermart_candelaria_foodcourt"

def execute_sql_commands(db_cursor: Any, query: Any) -> Any:
  return db_cursor.execute(query)

def display_databases_tables(db_cursor: Any) -> None:
  for _ in db_cursor:
    print(_)

def main() -> None:
    
  store_name: str = input("Input Store Name: ")
  time_reservation: str = input(f"Input Time of Seat Reservation for {store_name}\'s Customer: ")
  number_customer: int = input(f"Input Number of Seats for {store_name}\'s Customer: ")
  seat_fee: float = input("Input Seat Fee: ")
  
  try:
    
    db_connect = mysql.connector.connect(
      host = "localhost", 
      database = "foodcourt_seat_reservation", 
      user = "root", 
      password = ""
    )
    
    # db_create_query = f"CREATE DATABASE {} ({} {}, {} {})"
    # db_show_db_query = "SHOW DATABASES"
    # db_show_tb_query = "SHOW TABLES"
    
    db_insert_query = f"INSERT INTO {DATABASE_NAME} \
                        (store_name, time_reservation, number_customer, seat_fee) \
                        VALUES (\"{store_name}\", \"{time_reservation}\", \"{number_customer}\", \"{seat_fee}\")"
                 
    db_cursor = db_connect.cursor()
    
    execute_sql_commands(db_cursor, db_insert_query)
    
    db_connect.commit()
    db_cursor.close()
    
    print("\nDATA SUCCESSFULLY INSERTED\n")
    
  except Error as error:
    
    print(f"\nINSERT DATA FAILED {error}\n")
    
  finally:
    
    if db_connect.is_connected():
      db_connect.close()
      print("\nSQL IS NOW CLOSED.\n")

if __name__ == "__main__":
  main()