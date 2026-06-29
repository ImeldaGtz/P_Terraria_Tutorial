from globals import *
from world.items import *
from events import EventHandler

class Inventory:
    def __init__(self, app) -> None:
        self.app = app
        self.screen = app.screen

        # Create slots
        self.slots = []
        for index in range(5):
            self.slots.append(Item())

        self.slots[1] = BlockItem('grass', 5)
        self.slots[2] = BlockItem('dirt', 3)

        self.active_slot = 0

    def debug(self):
        for slot in self.slots:
            print(slot)
        print()

    def use(self, player, position):
        print( f"Active slot: {self.slots[self.active_slot]}" )
        if self.slots[self.active_slot].name != 'default':
            self.slots[self.active_slot].use(player, position)

    def add_item(self, item):
        first_available_slot = len(self.slots) # first empty slot
        target_slot = len(self.slots) # first slot of same name
        for index, slot in enumerate(self.slots):
            if slot.name == 'default' and index < first_available_slot:
                first_available_slot = index
            if slot.name == item.name:
                target_slot = index
        
        if target_slot < len(self.slots):
            self.slots[target_slot].quantity += items[item.name].quantity
        elif first_available_slot < len(self.slots):
            self.slots[first_available_slot] = items[item.name].item_type(item.name, items[item.name].quantity)

    def update(self):
        if EventHandler.keydown(pygame.K_RIGHT):
            if self.active_slot < len(self.slots) - 1:
                self.active_slot += 1
        if EventHandler.keydown(pygame.K_LEFT):
            if self.active_slot > 0:
                self.active_slot -= 1

        if EventHandler.clicked_any():
            self.debug()
    def draw(self):
        pass