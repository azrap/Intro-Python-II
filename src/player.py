# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def __str__(self):
        return f'''
        Name: {self.name},
        Current Room: {self.room.name},
        Items: {self.items}'''

    def player_items(self):
        print("The items you have are: ")
        if len(self.items) == 0:
            print("you don't have any items")
        for a in self.items:
            print(a.name)
