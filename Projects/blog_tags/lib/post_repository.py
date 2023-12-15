from lib.post import *
from lib.tag import *

class PostRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM posts'
        )
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'])
            posts.append(item)
        
        return posts
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * FROM posts WHERE id = %s', [id]
        )
        row = rows[0]
        return Post(row['id'], row['title'])
    
    def find_with_tag(self, id):
        rows = self._connection.execute(
            'SELECT posts.id as post_id, posts.title, tags.id as tag_id, tags.name ' \
            'FROM posts '\
            'JOIN posts_tags ON posts_tags.post_id = posts.id ' \
            'JOIN tags ON posts_tags.tag_id = tags.id ' \
            'WHERE tags.id = %s', [id]
        )

        posts = []
        for row in rows:
            item = Post(row['post_id'], row['title'])
            posts.append(item)

        return Tag(rows[0]['tag_id'], rows[0]['name'], posts)
