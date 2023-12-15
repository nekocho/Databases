class Book:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    # makes sure duplicates match
    
    def __repr__(self): #formatting
        return f"Book({self.id}, {self.title}, {self.author_name})"