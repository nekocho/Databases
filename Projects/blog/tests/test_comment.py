from lib.comment import *

def test_construct_comment():
    comment = Comment(1, 'Comment content', 'Author', 1)
    assert comment.id == 1
    assert comment.comment_content == 'Comment content'
    assert comment.author_name == 'Author'
    assert comment.post_id == 1

def test_equal_comment():
    comment1 = Comment(1, 'Comment content', 'Author', 1)
    comment2 = Comment(1, 'Comment content', 'Author', 1)
    assert comment1 == comment2

def test_format_comment():
    comment = Comment(1, 'Comment content', 'Author', 1)
    assert str(comment) == 'Comment(1, Comment content, Author, 1)'