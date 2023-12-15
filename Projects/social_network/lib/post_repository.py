from lib.post import *

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM posts ORDER BY id ASC'
        )
        post = []
        for row in rows:
            item = Post(row['id'], row['title'], row['content'], row['number_of_views'], row['user_account_id'])
            post.append(item)
        return post
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * FROM posts WHERE id = %s', [id]
        )
        row = rows[0]
        return Post(row['id'], row['title'], row['content'], row['number_of_views'], row['user_account_id'])
    
    def create(self, post):
        self._connection.execute(
            'INSERT INTO posts (id, title, content, number_of_views, user_account_id) VALUES(%s, %s, %s, %s, %s)', 
            [post.id, post.title, post.content, post.number_of_views, post.user_account_id]
        )
        return None
    
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [id]
        )
        return None
    
    def update(self, posts):
        self._connection.execute(
            'UPDATE posts SET title = %s, content = %s, number_of_views = %s, user_account_id = %s WHERE id = %s', [posts.title, posts.content, posts.number_of_views, posts.user_account_id, posts.id]
            )
        return None