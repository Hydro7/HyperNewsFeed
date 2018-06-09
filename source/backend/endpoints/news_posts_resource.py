from flask_restful import Resource
from source.backend.database.news_database import NewsDatabase


class NewsPosts(Resource):

    def get(self):
        db = NewsDatabase('database/news_database.db')
        lst = []
        for post in db.retrieve_posts():
            lst.append(post.to_json())
        return lst
