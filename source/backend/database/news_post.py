from datetime import datetime as dt
import json
import hashlib

"""
NewsPost Object:

Represents a single news source, with some fields that can be initialized to
default values.
"""

DATE_FORMAT = '%Y-%m-%d %H-%M-%S'


class NewsPost:

    """
    Initialize the news post with all fields needed to complete the object.
    """
    def __init__(self, title, content, created_date, company_name, address):
        self.title = title
        self.created_date = created_date
        self.company_name = company_name
        self.address = address
        self.content = content

    """
    Returns a json object representing a news post.
    """
    def to_json(self):
        json_obj = {
            'title':        self.title,
            'content':      self.content,
            'created_date': self.created_date.strftime(DATE_FORMAT),
            'company_name': self.company_name,
            'address':      self.address
        }
        return json_obj

    """
    Returns a new NewsPost object loaded from a json object.
    """
    @staticmethod
    def from_json(json_str):
        json_obj = json.loads(json_str)
        return NewsPost(
            json_obj['title'],
            json_obj['content'],
            dt.strptime(json_obj['created_date'], DATE_FORMAT),
            json_obj['company_name'],
            json_obj['address']
        )

    """
    Returns a new NewsPost object as loaded from an sqlite3 result row.
    """
    @staticmethod
    def from_sqlite3_row(row):
        return NewsPost(
            row[1],
            row[2],
            dt.strptime(row[3], DATE_FORMAT),
            row[4],
            row[5]
        )

    """
    Prints the content of the news post.
    """
    def __str__(self):
        return 'News Post: {\n\tTitle: ' + self.title + '\n\tCreated Date: ' + str(self.created_date) + '\n\tAddress: ' + self.address + '\n\tCompany Name: ' + self.company_name + '\n\tContent: ' + self.content + '\n}\n'

    def create_hash(self, input_string):
        return hashlib.md5(input_string.encode('utf-8')).hexdigest()

