from room import Room
from player import Player
from item import Item

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

item = {
    'sword': Item('sword', "I'm a sword, duh"),
    'knife': Item('knife', "I'm a knife, duh"),
    'food': Item('food', "need to eat it to survive.")
}
# sword = Item('sword', "I'm a sword, duh")


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# item rooms
room['outside'].items = [item['sword'], item['knife']]
room['foyer'].items = [item['food']]

# Make a new player object that is currently in the 'outside' room.
player = Player("Azra", room['outside'])
player.items.append(item['food'])


# Helper Functions
def room_swapper(room, direction):
    new_room = getattr(room, f"{direction}_to")
    if new_room is None:
        print('There are no rooms in that direction, please try again\n')
        return room
    else:
        print('room switch was successful!\n')
        return new_room


def take_item(item_list, item_name, player, room):
    if item_list[item_name] in room.items:
        player.items.append(item_list[item_name])
        room.items.remove(item_list[item_name])
    else:
        print(f'{item_name} does not exist in {room.name}\n')


def drop_item(item_list, item_name, player, room):
    if item_list[item_name] in player.items:
        player.items.remove(item_list[item_name])
        room.items.append(item_list[item_name])
    else:
        print(f'you are currently not carrying {item_name}')


# Takes an array and prints out
q = False
while q is False:
    print(
        f'''Greetings {player.name}, your current room is: {player.room.name}.
 ''')
    player.room.room_items()

    command = input(
        '''Please enter a command:
    (i) get inventory
    (n) to go north
    (s) to go south
    (e) to go east
    (w) to go west
    (take item_name) to take an item from the room. Eg. take sword
    (drop item_name) to drop an item in the room. Eg. drop sword
    (q) to quit the game
        ''')
    command = command.lower().strip()
    if command is None:
        print("No options were selected, please try again")
    elif command[0] in ["n", "s", "e", "w"]:
        player.room = room_swapper(player.room, command)
    elif command[0] == "i":
        player.player_items()
    elif command[0:4] == "take":
        try:
            item_name = command.split(" ")[1]
            take_item(item, item_name, player, player.room)
        except IndexError:
            print('Invalid input. Please try again')
    elif command[0:4] == "drop":
        try:
            item_name = command.split(" ")[1]
            drop_item(item, item_name, player, player.room)
        except IndexError:
            print('Invalid input. Please try again')
    elif command == "q":
        print("thank you for playing, good bye")
        q = True
    else:
        print("\nInvalid input. Please try again:\n")

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
