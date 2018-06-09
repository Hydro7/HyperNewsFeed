import sqlite3

"""
Database Connection.

Functions in this file are used for interacting with a database of news posts.
"""

class NewsDatabase:

    """
    Initializes the NewsDatabase object, and performs setup operations of the database,
    such as opening the db connection and creating tables if needed.
    """
    def __init__(self):
        self.db_conn = sqlite3.connect('news_database.db', 3.0)
        self.cursor = self.db_conn.cursor()
        self.initializeTables()


    """
    Ensures that all tables in the database exist, and if not, creates them.
    """
    def initializeTables(self):
        