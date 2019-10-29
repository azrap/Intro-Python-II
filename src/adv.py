from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# does this room have this attribute? If so, I'm going to get this attribute.
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Azra", room['outside'])


def room_swapper(room, direction):
    new_room = getattr(room, f"{direction}_to")
    if new_room is None:
        print('There are no rooms in that direction, please try again\n')
        new_room = room
    else:
        print('room switch was successful!\n')
    return new_room

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
# create a helper version to do the movement
# has attr and get attr, google it.


q = False
while q is False:
    print(
        f"Greetings {player1.name}, your current room is: {player1.room.name}\n")
    direction = input(
        "which direction will you choose? (n,s,e,w) or enter q to quit: \n")
    direction = direction.lower().strip()[0]
    if direction in ["n", "s", "e", "w"]:
        player1.room = room_swapper(player1.room, direction)
    elif direction == "q":
        print("thank you for playing, good bye")
        q = True
    else:
        print("Invalid input. Type n,s,e,w to pick direction or q to quit:\n")

    # if direction.upper()=="N":
    #     player1.current_room=[key for (key, value) in room.items() if value==room[f'{player1.current_room}'].n_to ]
    # # if direction.upper()=="S":
    #     player1.current_room=room[f'{player1.current_room}'].s_to #change it to dynamic later
