from lib.post import *
from lib.post_repository import *
from lib.comment import *

def test_get_all_post(db_connection):
    db_connection.seed('seeds/blog.sql')
    repository = PostRepository(db_connection)

    result = repository.all()
    assert result == [
        Post(1, 'Title 1', 'Content 1'),
        Post(2, 'Title 2', 'Content 2'),
        Post(3, 'Title 3', 'Content 3')
    ]

def test_find_post(db_connection):
    db_connection.seed('seeds/blog.sql')
    repository = PostRepository(db_connection)

    result = repository.find(1)
    assert result == Post(1, 'Title 1', 'Content 1')

def test_find_with_comments(db_connection):
    db_connection.seed('seeds/blog.sql')
    repository = PostRepository(db_connection)

    result = repository.find_with_comments(1)
    assert result == Post(1, 'Title 1', 'Content 1', [
        Comment(1, 'Comment 1', 'Jack', 1),
        Comment(6, 'Comment 6', 'Steven', 1)
    ])

