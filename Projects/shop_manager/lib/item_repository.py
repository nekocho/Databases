from lib.item import *

class ItemRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from items')
        items = []
        for row in rows:
            object = Item(row["id"], row["item_name"], row["price"], row["item_amount"], row["order_id"])
            items.append(object)
        return items

    # Find a single artist by their id
    def find(self, item_id):
        rows = self._connection.execute(
            'SELECT * from items WHERE id = %s', [item_id])
        row = rows[0]
        return Item(row["id"], row["item_name"], row["price"], row["item_amount"], row["order_id"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, item):
        self._connection.execute('INSERT INTO items (item_name, price, item_amount, order_id) VALUES (%s, %s, %s, %s)', [
                                 item.item_name, item.price, item.item_amount, item.order_id])
        return None

    # Delete an artist by their id
    def delete(self, item_id):
        self._connection.execute(
            'DELETE FROM items WHERE id = %s', [item_id])
        return None
