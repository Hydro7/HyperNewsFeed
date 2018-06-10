from flask import Flask
from flask_restful import Api, Resource

from database.news_database import NewsDatabase

app = Flask(__name__)
api = Api(app)


class NewsPosts(Resource):

    def get(self):
        db = NewsDatabase('database/prod.db')
        lst = []
        for post in db.retrieve_posts():
            lst.append(post.to_json())
        db.close()
        return lst

    def delete(self):
        db = NewsDatabase('database/prod.db')
        db.delete_posts()
        db.close()


class SearchPosts(Resource):

    def get(self, keyword):
        db = NewsDatabase('database/prod.db')
        lst = []
        for post in db.search_posts(keyword):
            lst.append(post.to_json())
        db.close()
        return lst


api.add_resource(NewsPosts, '/')
api.add_resource(SearchPosts, '/search/<keyword>', endpoint='search')



if __name__ == '__main__':
    app.run()