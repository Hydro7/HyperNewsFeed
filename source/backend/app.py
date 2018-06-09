from flask import Flask
from flask_restful import Resource, Api
from source.backend.database.news_database import NewsDatabase

app = Flask(__name__)
api = Api(app)

db = NewsDatabase('database/news_database.db')


class NewsPosts(Resource):
    def get(self):
        posts = db.retrieve_posts()
        post_json = []
        for post in posts:
            post_json.append(post.to_json())
        return post_json


api.add_resource(NewsPosts, '/newsposts')


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()