from lib.post import *
from lib.comment import *

class PostRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM posts'
        )
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'], row['post_content'])
            posts.append(item)
        
        return posts
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * FROM posts WHERE id = %s', [id]
        )
        row = rows[0]
        return Post(row['id'], row['title'], row['post_content'])
    
    def find_with_comments(self, id):
        rows = self._connection.execute(
            'SELECT posts.id as post_id, posts.title, posts.post_content, comments.id as comment_id, comments.comment_content, comments.author_name '\
            'FROM posts JOIN comments on posts.id = comments.post_id '\
            'WHERE posts.id = %s', [id]
        )

        comments = []
        for row in rows:
            item = Comment(row['comment_id'], row['comment_content'], row['author_name'], row['post_id'])
            comments.append(item)
        
        return Post(rows[0]['post_id'], rows[0]['title'], rows[0]['post_content'], comments)