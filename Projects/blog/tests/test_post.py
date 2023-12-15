from lib.post import *

def test_construct_post():
    post = Post(1, 'Title of post', 'Content of post')
    assert post.id == 1
    assert post.title == 'Title of post'
    assert post.content == 'Content of post'

def test_equal_post():
    post1 = Post(1, 'Title of post', 'Content of post')
    post2 = Post(1, 'Title of post', 'Content of post')
    assert post1 == post2

def test_format_post():
    post = Post(1, 'Title of post', 'Content of post')
    assert str(post) == 'Post(1, Title of post, Content of post)'