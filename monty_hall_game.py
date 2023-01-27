import random

class MontyHall:
    def __init__(self):
        self.doors = ["goat", "goat", "car"]
        self.chosen_door = None
        self.opened_door = None
        self.remaining_door = None
        random.shuffle(self.doors)

    def choose_door(self, door):
        self.chosen_door = door
