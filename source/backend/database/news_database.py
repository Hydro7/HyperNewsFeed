import sqlite3

from source.backend.database import news_post
from datetime import datetime

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
        self.initialize_tables()

    """
    Ensures that all tables in the database exist, and if not, creates them.
    """
    def initialize_tables(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS news_posts (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT DEFAULT NULL,
                  content TEXT DEFAULT NULL,
                  created_date DATETIME DEFAULT (STRFTIME('%Y-%m-%d %H-%M-%S', 'NOW')),
                  company_name TEXT DEFAULT NULL,
                  address TEXT DEFAULT NULL);'''
        )
        print('Tables initialized.')

    """
    Stores a news post into the database.
    """
    def store_news_post(self, news_post):
        self.cursor.execute(
            '''INSERT INTO news_posts(
                  title,
                  content,
                  created_date,
                  company_name,
                  address) VALUES (?, ?, ?, ?, ?);''',
            (
                news_post.title,
                news_post.content,
                news_post.created_date,
                news_post.company_name,
                news_post.address
            )
        )


db = NewsDatabase()
test_post = news_post.NewsPost('test_title', 'test_content', datetime.now(), 'test_company', 'test_address')
print(test_post)
db.store_news_post(test_post)
