from flask import Flask
from flask_restful import Api, Resource

from database.news_database import NewsDatabase
from endpoints.news_posts_resource import NewsPosts

app = Flask(__name__)
api = Api(app)

db = NewsDatabase('database/news_database.db')


class NewsPosts(Resource):

    def get(self):
        lst = []
        for post in db.retrieve_posts():
            lst.append(post.to_json())
        return lst


api.add_resource(NewsPosts, '/')


if __name__ == '__main__':
    app.run()