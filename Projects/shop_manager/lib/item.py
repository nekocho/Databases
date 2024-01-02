class Item:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, item_name, price, item_amount, order_id):
        self.id = id
        self.item_name = item_name
        self.price = price
        self.item_amount = item_amount
        self.order_id = order_id

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Item({self.id}, {self.item_name}, {self.price}, {self.item_amount}, {self.order_id})"
