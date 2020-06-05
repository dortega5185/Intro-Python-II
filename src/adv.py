from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#
room["foyer"].items_list = [Item("Sword", "made of iron, intrument of death")]

# Make a new player object that is currently in the 'outside' room.
player = Player("jesus", room["outside"])
# done = False
# Isaac = Player("no mans land", room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print(
    "To move your Character type [w](north), [a](west), [s](south), [d](east), if you want to quit type [q], type [help] for instructions."
)

while True:
    print(player.print_currentroom())
    command = input(">Where would you like to go? ").lower()
    if command in ["n", "s", "e", "w"]:
        player.location = player.move(command, player.location)
        continue

    elif command == "find":
        player.search()
        print("Type [get] to grab an item in the room.")
        print("Type [drop] to drop an item in the room.")

    elif command == "get":
        player.grabItem()

    if command == "q" or command == "quit":
        break


# while True:
#     Isaac.move = input(">Where would you like to go?  ").lower()
#     if Isaac.move == "w":
#         Isaac.currentroom = Isaac.currentroom.n_to
#         print(
#             "You're now in the "
#             + Isaac.currentroom.name
#             + ", "
#             + Isaac.currentroom.description
#         )
#     elif Isaac.move == "d":
#         Isaac.currentroom = Isaac.currentroom.e_to
#         print(
#             "You're now in the "
#             + Isaac.currentroom.name
#             + ", "
#             + Isaac.currentroom.description
#         )
#     elif Isaac.move == "s":
#         Isaac.currentroom = Isaac.currentroom.s_to
#         print(
#             "You're now in the "
#             + Isaac.currentroom.name
#             + ", "
#             + Isaac.currentroom.description
#         )
#     elif Isaac.move == "a":
#         Isaac.currentroom = Isaac.currentroom.w_to
#         print(
#             "You're now in the "
#             + Isaac.currentroom.name
#             + ", "
#             + Isaac.currentroom.description
#         )
#     elif Isaac.move == "q":
#         print("You have now exited the game.")
#         break
#     elif Isaac.move == "help":
#         print(
#             """
# w - go north
# s - go south
# a - go west
# d - go east
# q - to quit the game
#         """
#         )
#     else:
#         print("There is no path in this direction, please pick another path.")


#     if Isaac.move == "q":
#         print("You have now exited the game.")
#         break
#     elif Isaac.move == "help":
#         print(
#             """
# w - go north
# s - go south
# a - go west
# d - go east
# q - to quit the game
#         """
#         )
#     else:
#         Isaac.shallnotpass
