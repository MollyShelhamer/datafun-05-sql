import sqlite3

def execute_sql_file(cursor, filename):
    with open(filename, 'r') as file:
        sql = file.read()
        cursor.executescript(sql)

conn = sqlite3.connect("books_authors.db")
cursor = conn.cursor()

execute_sql_file(cursor, "sql_create/01_drop_tables.sql")
execute_sql_file(cursor, "sql_create/02_create_tables.sql")
execute_sql_file(cursor, "sql_create/03_insert_records.sql")

conn.commit()
conn.close()
print("Database setup complete.")
