from flask import Flask
from flask_restful import Api, Resource

from source.backend.database.news_database import NewsDatabase
from source.backend.endpoints.news_posts_resource import NewsPosts

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