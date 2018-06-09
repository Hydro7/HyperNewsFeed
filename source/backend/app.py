from flask import Flask
from flask_restful import Api

from source.backend.database.news_database import NewsDatabase
from source.backend.endpoints.news_posts_resource import NewsPosts

app = Flask(__name__)
api = Api(app)

api.add_resource(NewsPosts, '/newsposts')
db = NewsDatabase('database/news_database.db')


@app.route('/')
def get_posts():
    lst = []
    for post in db.retrieve_posts():
        lst.append(post.to_json())
    return lst


if __name__ == '__main__':
    app.run()