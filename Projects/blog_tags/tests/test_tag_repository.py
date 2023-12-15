from lib.tag import *
from lib.tag_repository import *

def test_get_all_tags(db_connection):
    db_connection.seed('seeds/blog_tags.sql')
    repository = TagRepository(db_connection)

    result = repository.all()
    assert result == [
        Tag(1, 'coding'),
        Tag(2, 'travel'),
        Tag(3, 'cooking'),
        Tag(4, 'education'),
    ]

def test_find_with_post(db_connection):
    db_connection.seed('seeds/blog_tags.sql')
    repository = TagRepository(db_connection)

    result = repository.find_with_post(2)
    assert result == Post(2, 'Fun classes', [
        Tag(1, 'coding'),
        Tag(4, 'education')
    ])

