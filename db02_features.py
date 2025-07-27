import sqlite3

def execute_sql_file(cursor, filename):
    with open(filename, 'r') as file:
        sql = file.read()
        cursor.executescript(sql)

conn = sqlite3.connect("books_authors.db")
cursor = conn.cursor()

execute_sql_file(cursor, "sql_features/update_records.sql")
execute_sql_file(cursor, "sql_features/delete_records.sql")

conn.commit()
conn.close()
print("Record updates and deletions complete.")
