class Tag:
    def __init__(self, id, name, post = None):
        self.id = id
        self.name = name
        self.post = post or []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Tag({self.id}, {self.name})"