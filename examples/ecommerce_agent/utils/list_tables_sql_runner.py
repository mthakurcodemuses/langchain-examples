import sqlite3

conn = sqlite3.connect('db.sqlite')


def list_tables():
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_details_rows = cursor.fetchall()
    return "\n".join(table_detail_row[0] for table_detail_row in table_details_rows if table_detail_row[0] is not None)
