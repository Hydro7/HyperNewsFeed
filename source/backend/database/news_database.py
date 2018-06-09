import sqlite3
from database import news_post

"""
Database Connection.

Functions in this file are used for interacting with a database of news posts.
"""


class NewsDatabase:

    """
    Initializes the NewsDatabase object, and performs setup operations of the database,
    such as opening the db connection and creating tables if needed.
    """
    def __init__(self, db_filename='database/news_database.db'):
        self.db_conn = sqlite3.connect(db_filename, 3.0)
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
    def store_news_post(self, news_post_obj):
        try:
            self.cursor.execute(
                '''INSERT INTO news_posts(
                      title,
                      content,
                      created_date,
                      company_name,
                      address) VALUES (?, ?, ?, ?, ?);''',
                (
                    news_post_obj.title,
                    news_post_obj.content,
                    news_post_obj.created_date.strftime(news_post.DATE_FORMAT),
                    news_post_obj.company_name,
                    news_post_obj.address
                )
            )
            self.db_conn.commit()
        except Exception as err:
            print('Query failed while trying to insert news post: %s, \nError: %s' % news_post_obj, err)

    """
    Stores a list of news post objects.
    """
    def store_many_news_posts(self, posts):
        try:
            self.cursor.executemany(
                '''INSERT INTO news_posts(
                      title,
                      content,
                      created_date,
                      company_name,
                      address) VALUES (?, ?, ?, ?, ?);''',
                posts
            )
            self.db_conn.commit()
        except Exception as err:
            print('Query failed while trying to insert many posts: %s, \nError: %s' % posts, err)

    """
    Retrieves a list of the first 'count' posts that contain the given keywords, if they are provided.
    """
    def retrieve_posts(self):
        try:
            self.cursor.execute(
                '''SELECT *
                   FROM news_posts 
                   ORDER BY DATETIME(created_date) DESC;'''
            )
            posts = []
            rows = self.cursor.fetchall()
            if rows == None:
                return []
            for row in self.cursor.fetchall():
                print(row)
                posts.append(news_post.NewsPost.from_sqlite3_row(row))
            return posts
        except Exception as err:
            print('Query failed while trying to retrieve posts. Error: ', err)
