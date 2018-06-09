from datetime import datetime

from flask import Flask
from flask_restful import Api, Resource

from database.news_database import NewsDatabase
from database.news_post import NewsPost

app = Flask(__name__)
api = Api(app)


class NewsPosts(Resource):

    def get(self):
        db = NewsDatabase('database/prod.db')
        lst = []
        this = db.retrieve_posts()
        if this:
            for post in this:
                lst.append(post.to_json())
            db.db_conn.close()
            return lst


api.add_resource(NewsPosts, '/')


if __name__ == '__main__':
    app.run()