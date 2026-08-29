import os
import sqlite3

# function for deleting tables
def delete_db(file_path):
    os.remove(file_path)

# recreate the tables
def init_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_db("products.db")
    init_db()



