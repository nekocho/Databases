from lib.post import *

def test_construct_of_post():
    post = Post(1, 'Title', 'Contents of post', 9, 1)
    assert post.id == 1
    assert post.title == 'Title'
    assert post.content == 'Contents of post'
    assert post.number_of_views == 9
    assert post.user_account_id == 1

def test_equals_to_post():
    post1 = Post(1, 'Title', 'Contents of post', 9, 1)
    post2 = Post(1, 'Title', 'Contents of post', 9, 1)
    assert post1 == post2

def test_formatting_post():
    post = Post(1, 'Title', 'Contents of post', 9, 1)
    assert str(post) == 'Post(1, Title, Contents of post, 9, 1)'