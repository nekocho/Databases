from lib.order import *

"""
Artist constructs with an id, name and genre
"""
def test_order_constructs():
    order = Order(1, '1-1-1', 'bob', 'test item')
    assert order.id == 1
    assert order.date== "1-1-1"
    assert order.customer_name == 'bob'
    assert order.item_name == 'test item'

"""
We can format artists to strings nicely
"""
def test_order_format_nicely():
    order = Order(1, '1-1-1', 'bob', 'test item')
    assert str(order) == "Order(1, 1-1-1, bob, test item)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_order_are_equal():
    order1 = Order(1, '1-1-1', 'bob', 'test item')
    order2 = Order(1, '1-1-1', 'bob', 'test item')
    assert order1 == order2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
