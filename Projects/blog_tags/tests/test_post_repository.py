from lib.post import *
from lib.post_repository import *

def test_get_all_post(db_connection):
    db_connection.seed('seeds/blog_tags.sql')
    repository = PostRepository(db_connection)

    result = repository.all()
    assert result == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(4, 'My weekend in Edinburgh'),
        Post(5, 'The best chocolate cake EVER'),
        Post(6, 'A foodie week in Spain'),
        Post(7, 'SQL basics')
    ]

def test_find_post(db_connection):
    db_connection.seed('seeds/blog_tags.sql')
    repository = PostRepository(db_connection)

    result = repository.find(1)
    assert result == Post(1, 'How to use Git')

def test_find_with_tags(db_connection):
    db_connection.seed('seeds/blog_tags.sql')
    repository = PostRepository(db_connection)

    result = repository.find_with_tag(1)
    assert result == Tag(1, 'coding', [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(7, 'SQL basics')
    ])

