# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

    def room_items(self):
        if len(self.items) == 0:
            print("this room doesn't have any items")
        else:
            print("The items in this room are: ")
            for a in self.items:
                print(a.name)
