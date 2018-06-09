import json

"""
NewsPost Object:

Represents a single news source, with some fields that can be initialized to
default values.
"""


class NewsPost:

    """
    Initialize the news post with all fields needed to complete the object.
    """
    def __init__(self, title, created_date, company_name, address, html_content):
        self.title = title
        self.created_date = created_date
        self.company_name = company_name
        self.address = address
        self.html_content = html_content

    """
    Returns a json object representing a news post.
    """
    def to_json(self):
        return json.dumps(self)

    """
    Returns a new NewsPost object loaded from a json object.
    """
    @staticmethod
    def from_json(json_obj):
        print(json_obj)
