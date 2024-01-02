class Order:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, date, customer_name, item_name):
        self.id = id
        self.date = date
        self.customer_name = customer_name
        self.item_name = item_name

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Order({self.id}, {self.date}, {self.customer_name}, {self.item_name})"
