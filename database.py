import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    """add entry into db"""
    with connection:
        #use ? to protect us from sqlinjection attacks 
        connection.execute(f"INSERT INTO entries VALUES(?,?)", (entry_content, entry_date))

def get_entries():
    """show entries in the db"""
    return entries