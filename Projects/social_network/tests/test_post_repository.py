from lib.post import *
from lib.post_repository import *

def test_get_all_posts(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)

    result = repository.all()

    assert result == [
        Post(1, 'Life', 'Its been a rollercoaster', 5, 3),
        Post(2, 'Happy birthday!', 'Turning 29 today', 200, 1),
        Post(3, 'Sloths', 'I really like sloths', 1, 2),
        Post(4, 'Promotion!', 'I got a promotion at work today!', 30, 3),
        Post(5, 'Zoo', 'I saw my favourite animal today', 60, 2),
        Post(6, 'Guitars', 'Bought a new guitar today', 150, 1)
    ]

def test_find_post(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)

    result = repository.find(2)

    assert result == Post(2, 'Happy birthday!', 'Turning 29 today', 200, 1)

def test_create_post(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)

    repository.create(Post(7, 'Woo!', 'Its been a great day!', 30, 1))

    result = repository.all()
    assert result == [
        Post(1, 'Life', 'Its been a rollercoaster', 5, 3),
        Post(2, 'Happy birthday!', 'Turning 29 today', 200, 1),
        Post(3, 'Sloths', 'I really like sloths', 1, 2),
        Post(4, 'Promotion!', 'I got a promotion at work today!', 30, 3),
        Post(5, 'Zoo', 'I saw my favourite animal today', 60, 2),
        Post(6, 'Guitars', 'Bought a new guitar today', 150, 1),
        Post(7, 'Woo!', 'Its been a great day!', 30, 1)     
    ]

def test_delete_post(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)

    repository.delete(4)

    result = repository.all()
    assert result == [
        Post(1, 'Life', 'Its been a rollercoaster', 5, 3),
        Post(2, 'Happy birthday!', 'Turning 29 today', 200, 1),
        Post(3, 'Sloths', 'I really like sloths', 1, 2),
        Post(5, 'Zoo', 'I saw my favourite animal today', 60, 2),
        Post(6, 'Guitars', 'Bought a new guitar today', 150, 1),
    ] 

def test_update_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(1)
    post.title = 'New Title'
    repository.update(post)

    result = repository.all()
    assert result == [
        Post(1, 'New Title', 'Its been a rollercoaster', 5, 3),
        Post(2, 'Happy birthday!', 'Turning 29 today', 200, 1),
        Post(3, 'Sloths', 'I really like sloths', 1, 2),
        Post(4, 'Promotion!', 'I got a promotion at work today!', 30, 3),
        Post(5, 'Zoo', 'I saw my favourite animal today', 60, 2),
        Post(6, 'Guitars', 'Bought a new guitar today', 150, 1)
    ]

