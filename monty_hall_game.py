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

    def open_door(self):
        if self.chosen_door == "car":
            self.opened_door = random.choice([door for door in self.doors if door != self.chosen_door])
        else:
            self.opened_door = [door for door in self.doors if door != "car" and door != self.chosen_door][0]

