# News Database

## Functions

### NewsDatabase()
Creates a new database object, which can be used to insert and query news posts.

#### Example
```python
from source.backend.database.news_database import NewsDatabase
news_db = NewsDatabase()
```

### store_news_post(news_post_obj)
Stores a news post object in the database, with the given NewsPost object.

#### Example
```python
from source.backend.database.news_post import NewsPost
from source.backend.database.news_database import NewsDatabase
from datetime import datetime

db = NewsDatabase()
test_post = NewsPost('test_title', 'test_content', datetime.now(), 'test_company', 'test_address')
db.store_news_post(test_post)
```

### store_many_news_posts(posts)
Stores a list of posts in the database, similar to the previous function. Simply provide a list of NewsPost objects.

### retrieve_posts()
Retrieves a set of posts from the database.

#### Example
```python
from source.backend.database.news_database import NewsDatabase
db = NewsDatabase()
posts = db.retrieve_posts()

print('Got ', len(posts), ' posts.')
for post in posts:
    print(post)
```