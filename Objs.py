import pygame

display_width = 1920
display_height = 1080


class Item:
    def __init__(self, type, stat, x, y, item_img, item_img_right):
        self.type = type
        self.stat = stat
        self.x = x
        self.y = y
        self.item_img = item_img
        self.item_img_right = item_img_right
        self.img_w = 50
        self.img_h = 50


class Chest:
    def __init__(self, x, y, items):
        self.x = x
        self.y = y
        self.items = items
        self.chest_img = pygame.image.load('art/chest.png')


class Door:
    def __init__(self, combo, number, destination_num):
        self.combo = combo
        if self.combo == ' ':
            self.locked = False
        else:
            self.locked = True
        self.door_flash = False
        self.number = number
        self.flash_timer = 0
        self.destination = destination_num
        self.door_buffer = ""
        self.failed_attempt = False
        # handle where to put the door on the scren
        if self.number == 1:
            self.x = display_width - 50
            self.y = display_height / 2 - 150
        elif self.number == 2:
            self.x = display_width / 2 - 150
            self.y = display_height - 50
        elif self.number == 3:
            self.x = 0
            self.y = display_height / 2 - 150
        elif self.number == 4:
            self.x = display_width / 2 - 150
            self.y = 0
        if number % 2 == 0:
            self.width = 300
            self.height = 50
            if combo == ' ':
                self.door_img = pygame.image.load('art/door0.png')
            else:
                self.door_img = pygame.image.load('art/door0.jpg')
        else:
            self.width = 50
            self.height = 300
            if combo == ' ':
                self.door_img = pygame.image.load('art/door.png')
            else:
                self.door_img = pygame.image.load('art/door.jpg')

    def can_pass(self):
        if self.combo == ' ':
            self.locked = False
            return True
        return not self.locked

    def unlock(self, combo):
        if combo == self.combo:
            self.locked = False
            if self.number % 2 == 0:
                self.door_img = pygame.image.load('art/door0.png')
            else:
                self.door_img = pygame.image.load('art/door.png')
            return True
        else:
            return False

    def add_to_door_buffer(self, key):
        self.door_buffer += key
        if len(self.door_buffer) == len(self.combo) and self.locked:
            if not self.unlock(self.door_buffer):
                if self.number % 2 == 0:
                    self.door_img = pygame.image.load('art/locked0.png')
                    self.failed_attempt = True
                else:
                    self.door_img = pygame.image.load('art/locked.png')
                    self.failed_attempt = True
            self.door_buffer = ""


class Chamber:
    def __init__(self, name, doors):
        self.chests = []
        self.npcs = []
        self.tidas = []
        self.items = []
        self.name = name
        self.doors = doors

    def add_chest(self, chest):
        self.chests.append(chest)

    def add_npc(self, npc):
        self.npcs.append(npc)

    def add_tida(self, tida):
        self.tidas.append(tida)


class Graph:
    def __init__(self, size: int):
        self.chambers = [0] * size

    def add_chamber(self, chamber):
        self.chambers[chamber.name] = chamber
