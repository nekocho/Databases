from lib.order_repository import *
from lib.order import *

def test_get_all_orders(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = OrderRepository(db_connection) # Create a new ArtistRepository

    orders = repository.all() # Get all artists

    # Assert on the results
    assert orders == [
        Order(1, '20-10-2023', 'John', 'Super Shark Vacuum Cleaner'),
        Order(2, '10-09-2023', 'Bob', 'Makerspresso Coffee Machine'),
        Order(3, '5-08-2023', 'Lizzie', 'Sunglasses')
    ]


def test_get_single_order(db_connection):
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = OrderRepository(db_connection)

    order = repository.find(1)
    assert order == Order(1, '20-10-2023', 'John', 'Super Shark Vacuum Cleaner')


def test_create_order(db_connection):
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = OrderRepository(db_connection)

    repository.create(Order(None, '1-1-1', 'Andy', 'Sunglasses'))

    result = repository.all()
    assert result == [
        Order(1, '20-10-2023', 'John', 'Super Shark Vacuum Cleaner'),
        Order(2, '10-09-2023', 'Bob', 'Makerspresso Coffee Machine'),
        Order(3, '5-08-2023', 'Lizzie', 'Sunglasses'),
        Order(4, '1-1-1', 'Andy', 'Sunglasses')
    ]


def test_delete_order(db_connection):
    db_connection.seed("seeds/shop_manager.sql") # Seed our database with some test data
    repository = OrderRepository(db_connection)
    repository.delete(3) 

    result = repository.all()
    assert result == [
        Order(1, '20-10-2023', 'John', 'Super Shark Vacuum Cleaner'),
        Order(2, '10-09-2023', 'Bob', 'Makerspresso Coffee Machine')
    ]
