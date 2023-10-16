import sqlite3

connection = sqlite3.connect("data.db")

#another way of getting data in dict format
connection.row_factory = sqlite3.Row

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    """add entry into db"""
    with connection:
        #use ? to protect us from sqlinjection attacks 
        connection.execute(f"INSERT INTO entries VALUES(?,?)", (entry_content, entry_date))

def get_entries():
    """show entries in the db"""
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor