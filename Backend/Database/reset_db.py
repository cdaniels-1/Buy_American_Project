import os
import sqlite3

# function for deleting tables
def delete_db(file_path):
    os.remove(file_path)

# recreate the tables
def init_db(file_path):
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(current_dir, "schema.sql")

    with open(schema_path, "r") as f:
        schema = f.read()
        cursor.executescript(schema)

    conn.commit()
    conn.close()


