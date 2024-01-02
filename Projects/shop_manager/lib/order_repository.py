from lib.order import *

class OrderRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from orders')
        orders = []
        for row in rows:
            item = Order(row["id"], row["date"], row["customer_name"], row["item_name"])
            orders.append(item)
        return orders

    # Find a single artist by their id
    def find(self, order_id):
        rows = self._connection.execute(
            'SELECT * from orders WHERE id = %s', [order_id])
        row = rows[0]
        return Order(row["id"], row["date"], row["customer_name"], row["item_name"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, order):
        self._connection.execute('INSERT INTO orders (date, customer_name, item_name) VALUES (%s, %s, %s)', [
                                 order.date, order.customer_name, order.item_name])
        return None

    # Delete an artist by their id
    def delete(self, order_id):
        self._connection.execute(
            'DELETE FROM orders WHERE id = %s', [order_id])
        return None
