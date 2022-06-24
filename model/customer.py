class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            "first name": self.first_name,
            "last name": self.last_name
        }

