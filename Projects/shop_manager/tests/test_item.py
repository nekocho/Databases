from lib.item import *

"""
Artist constructs with an id, name and genre
"""
def test_item_constructs():
    item = Item(1, "Test Item", 99, 15, 1)
    assert item.id == 1
    assert item.item_name == "Test Item"
    assert item.price == 99
    assert item.item_amount == 15
    assert item.order_id == 1

"""
We can format artists to strings nicely
"""
def test_item_format_nicely():
    item = Item(1, "Test Item", 99, 99, 1)
    assert str(item) == "Item(1, Test Item, 99, 99, 1)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_item_are_equal():
    item1 = Item(1, "Test item", 99, 99, 1)
    item2 = Item(1, "Test item", 99, 99, 1)
    assert item1 == item2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
