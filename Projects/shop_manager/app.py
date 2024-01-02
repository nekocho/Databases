from lib.database_connection import DatabaseConnection
from lib.order_repository import *
from lib.item_repository import *


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/shop_manager.sql")

# # Retrieve all artists
# order_repository = OrderRepository(connection)
# orders = order_repository.all()

# item_repository = ItemRepository(connection)
# items = item_repository.all()

# # List them out
# for item in items:
#     print(item)


class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/shop_manager.sql")

  def run(self):
    item_repository = ItemRepository(self._connection)
    items = item_repository.all()

    order_repository = OrderRepository(self._connection)
    orders = order_repository.all()

    print("Welcome to the shop management program!")

    print("What do you want to do?")
    print('1 - List all shop items')
    print('2 - Create a new item')
    print('3 - List all orders')
    print('4 - Create a new order')
    inp = int(input("Enter your choice:"))
    if inp == 1:
        print('Here is a list of all shop items:')
        for item in items:
            print(f"#{item.id} {item.item_name} - Unit Price: {item.price} - Quantity: {item.item_amount}")
    if inp == 2:
        print('Create a new item:')
        item_name = input("Enter item name: ")
        item_price = input("Enter item price: ")
        item_amount = input("Enter item amount: ")
        item_repository.create(Item(None, item_name, item_price, item_amount, None))
        items = item_repository.all()
        for item in items:
            print(f"#{item.id} {item.item_name} - Unit Price: {item.price} - Quantity: {item.item_amount}")
    if inp == 3:
        print('Here is a list of all orders:')
        for order in orders:
            print(f"#{order.id} Date: {order.date} - Customer name: {order.customer_name} - Item: {order.item_name}")
    if inp == 4:
        print('Create a new order:')
        order_date = input("Enter Today's date: ")
        customer_name = input("Enter your name: ")
        item_name = input("Enter item name: ")
        order_repository.create(Order(None, order_date, customer_name, item_name))
        orders = order_repository.all()
        for order in orders:
            print(f"#{order.id} Date: {order.date} - Customer name: {order.customer_name} - Item: {order.item_name}")





if __name__ == '__main__':
    app = Application()
    app.run()
