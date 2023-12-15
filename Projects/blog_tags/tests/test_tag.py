from lib.tag import *

def test_construct_tag():
    tag = Tag(1, 'Tag',)
    assert tag.id == 1
    assert tag.name == 'Tag'

def test_equal_tag():
    tag1 = Tag(1, 'Tag')
    tag2 = Tag(1, 'Tag')
    assert tag1 == tag2

def test_format_tag():
    tag = Tag(1, 'Tag')
    assert str(tag) == 'Tag(1, Tag)'