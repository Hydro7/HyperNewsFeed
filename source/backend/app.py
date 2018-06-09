from flask import Flask
from flask_restful import Api
from source.backend.endpoints.news_posts_resource import NewsPosts

app = Flask(__name__)
api = Api(app)

api.add_resource(NewsPosts, '/newsposts')


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()