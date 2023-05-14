| Line Number | Method | Explanation | Time Complexity |
| ----------- | ------ | ----------- | --------------- |
| 21 | `is_database_exists` | This function executes a query to check if a database exists. The time complexity of this operation is O(1) because it only checks for the existence of the database and fetches a single row. | O(1) |
| 29 | `create_database` | This function executes a query to create a database if it does not already exist. The time complexity of this operation is O(1) because it only executes a single query to create the database. | O(1) |
| 37 | `create_tables` | This function executes multiple queries to create tables. The time complexity depends on the number of tables and the complexity of the table creation queries. In this case, it executes three queries to create three tables. The time complexity of each table creation query is O(1), so the overall time complexity is also O(1). | O(1) |
| 55 | `insert_data` | This function inserts data into a table. It iterates over the data list and executes an insert query for each item. If n is the number of items in the data list, the time complexity of this operation is O(n) because it performs a constant amount of work for each item. | O(n), where n is the number of items |
| 73 | `read_data` | This function executes a select query to fetch all rows from a table. The time complexity of this operation depends on the number of rows in the table. If m is the number of rows, the time complexity is O(n) because it needs to fetch all rows from the table. | O(n), where n is the number of rows |
| 91 | `update_data` | This function executes an update query to modify rows in a table. The time complexity depends on the number of rows that satisfy the condition. If k is the number of rows to be updated, the time complexity is O(n) because it needs to update each matching row. | O(n), where n is the number of rows to be updated |
| 107 | `delete_data` | This function executes a delete query to remove rows from a table. The time complexity depends on the number of rows that satisfy the condition. If k is the number of rows to be deleted, the time complexity is O(n) because it needs to delete each matching row. | O(n), where n is the number of rows to be deleted |
| 123 | `join_tables` | This function executes a join query to combine rows from two tables. The time complexity of this operation depends on the number of rows in the resulting join. If p is the number of rows in the join, the time complexity is O(n) because it needs to fetch and combine all matching rows from both tables. | O(n), where n is the number of rows in the join |
| 141 | `group_by_having` | This function executes a group by query to aggregate rows based on a specific condition. The time complexity of this operation depends on the number of rows in the resulting group. If q is the number of rows in the group, the time complexity is O(n) because it needs to group and aggregate the rows. | O(n), where n is the number of rows in the group |
| 157 | `order_by` | This function executes an order by query to sort rows based on a specific column. The time complexity depends on the number of rows in the table. If r is the number of rows, the time complexity is O(n log n) because it needs to sort all rows. | O(n log n), where n is the number of rows |

<!-- | Line Number | Method | Explanation | Time Complexity |
| ----------- | ------ | ----------- | --------------- |
| 21 | `is_database_exists` | This function executes a query to check if a database exists. | O(1) |
| 29 | `create_database` | This function executes a query to create a database if it does not already exist. | O(1) |
| 37 | `create_tables` | This function executes multiple queries to create tables. | O(1) |
| 55 | `insert_data` | This function inserts data into a table by executing an insert query for each item. | O(n), where n is the number of items |
| 73 | `read_data` | This function executes a select query to fetch all rows from a table. | O(n), where n is the number of rows |
| 91 | `update_data` | This function executes an update query to modify rows in a table. | O(n), where n is the number of rows to be updated |
| 107 | `delete_data` | This function executes a delete query to remove rows from a table. | O(n), where n is the number of rows to be deleted |
| 123 | `join_tables` | This function executes a join query to combine rows from two tables. | O(n), where n is the number of rows in the join |
| 141 | `group_by_having` | This function executes a group by query to aggregate rows based on a condition. | O(n), where n is the number of rows in the group |
| 157 | `order_by` | This function executes an order by query to sort rows based on a column. | O(n log n), where n is the number of rows | -->