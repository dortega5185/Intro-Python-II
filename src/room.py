# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items_list = list()

    def __str__(self):
        return f"{self.name}, {self.description}"

    def print_all_items(self):
        for i in self.items_list:
            print(f"{i.name}, {i.description}")
