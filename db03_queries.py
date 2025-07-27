import sqlite3

conn = sqlite3.connect("books_authors.db")
cursor = conn.cursor()

def run_query(filename, label):
    with open(filename, 'r') as file:
        sql = file.read()
        cursor.execute(sql)
        print(f"\n--- {label} ---")
        for row in cursor.fetchall():
            print(row)

run_query("sql_queries/query_aggregation.sql", "Aggregation")
run_query("sql_queries/query_filter.sql", "Filter")
run_query("sql_queries/query_sorting.sql", "Sorting")
run_query("sql_queries/query_group_by.sql", "Group By")
run_query("sql_queries/query_join.sql", "Join")

conn.close()
