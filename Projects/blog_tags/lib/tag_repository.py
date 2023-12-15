from lib.post import *
from lib.tag import *

class TagRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM tags'
        )
        tags = []
        for row in rows:
            item = Tag(row['id'], row['name'])
            tags.append(item)
        
        return tags
    
    def find_with_post(self, id):
        rows = self._connection.execute(
            'SELECT posts.id as post_id, posts.title, tags.id as tag_id, tags.name ' \
            'FROM tags '\
            'JOIN posts_tags ON posts_tags.tag_id = tags.id ' \
            'JOIN posts ON posts_tags.post_id = posts.id ' \
            'WHERE posts.id = %s', [id]
        )

        tags = []
        for row in rows:
            item = Tag(row['tag_id'], row['name'])
            tags.append(item)

        return Post(rows[0]['post_id'], rows[0]['title'], tags)
