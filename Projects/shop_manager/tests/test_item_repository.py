from lib.item_repository import *
from lib.item import *

def test_get_all_items(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = ItemRepository(db_connection) # Create a new ArtistRepository

    items = repository.all() # Get all artists

    # Assert on the results
    assert items == [
        Item(1, 'Super Shark Vacuum Cleaner', 99, 30, 1),
        Item(2, 'Makerspresso Coffee Machine', 69, 15, 2),
        Item(3, 'Sunglasses', 25, 20, 3)
    ]


def test_get_single_item(db_connection):
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = ItemRepository(db_connection)

    item = repository.find(1)
    assert item == Item(1, 'Super Shark Vacuum Cleaner', 99, 30, 1)


def test_create_item(db_connection):
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = ItemRepository(db_connection)

    repository.create(Item(None, 'Lipstick', 10, 10, 1))

    result = repository.all()
    assert result == [
        Item(1, 'Super Shark Vacuum Cleaner', 99, 30, 1),
        Item(2, 'Makerspresso Coffee Machine', 69, 15, 2),
        Item(3, 'Sunglasses', 25, 20, 3),
        Item(4, 'Lipstick', 10, 10, 1)
    ]


def test_delete_item(db_connection):
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = ItemRepository(db_connection)
    repository.delete(3) 

    result = repository.all()
    assert result == [
        Item(1, 'Super Shark Vacuum Cleaner', 99, 30, 1),
        Item(2, 'Makerspresso Coffee Machine', 69, 15, 2)
    ]
