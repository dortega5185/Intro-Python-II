# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.list = list()

    def __str__(self):
        return f"{self.name}"

    def print_currentroom(self):
        return f"{self.location}"

    def move(self, direction, currentroom):
        attribute = direction + "_to"

        if hasattr(currentroom, attribute):
            return getattr(currentroom, attribute)

        print("Error! There is no path this way. Pick a different direction.")
        return currentroom

    # def shallnotpass(self):
    #     if hasattr(self.currentroom, f"{self.move}_to"):
    #         self.currentroom = getattr(self.currentroom, f"{self.move}_to")
    #         print(self.currentroom)
    #         print(self.currentroom.description)
    #     else:
    #         print("Error! There is no path this way. Pick a different direction.")
