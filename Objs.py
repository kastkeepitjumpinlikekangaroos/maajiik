import pygame
import math
display_width = 1600
display_height = 900


class Item:
    def __init__(self, type, stat, x, y, itemImg):
        self.type = type
        self.stat = stat
        self.x = x
        self.y = y
        self.itemImg = itemImg

class Chest:
    def __init__(self, x, y, items):
        self.x = x
        self.y = y
        self.items = items
        self.chestImg = pygame.image.load('art/chest.png')



class Door:
    def __init__(self, combo, number, destinationNum):
        self.combo = combo
        self.locked = True
        self.number = number
        self.destination = destinationNum
        self.doorBuffer = ""
        if self.number == 1:
            self.x = display_width - 50
            self.y = display_height/2 - 150
        elif self.number == 2:
            self.x = display_width/2 - 150
            self.y = display_height - 50
        elif self.number == 3:
            self.x = 0
            self.y = display_height / 2 - 150
        elif self.number == 4:
            self.x = display_width/2 - 150
            self.y = 0
        if number % 2 == 0:
            self.width = 300
            self.height = 50
            if combo == ' ':
                self.doorImg = pygame.image.load('art/door0.png')
            else:
                self.doorImg = pygame.image.load('art/door0.jpg')
        else:
            self.width = 50
            self.height = 300
            if combo == ' ':
                self.doorImg = pygame.image.load('art/door.png')
            else:
                self.doorImg = pygame.image.load('art/door.jpg')

    def canPass(self):
        if self.combo == ' ':
            self.locked = False
            return True
        return not self.locked

    def unlock(self, combo):
        if combo == self.combo:
            self.locked = False
            if self.number % 2 == 0:
                self.doorImg = pygame.image.load('art/door0.png')
            else:
                self.doorImg = pygame.image.load('art/door.png')

    def addToDoorBuffer(self, key):
        self.doorBuffer += key
        if len(self.doorBuffer) == len(self.combo):
            self.unlock(self.doorBuffer)
            self.doorBuffer = ""

class Chamber:
    def __init__(self, name, doors):
        self.chests = []
        self.npcs = []
        self.tidas = []
        self.items = []
        self.name = name
        self.doors = doors

    def addChest(self, chest):
        self.chests.append(chest)

    def addNpc(self, npc):
        self.npcs.append(npc)

    def addTida(self, tida):
        self.tidas.append(tida)


class Graph:
    def __init__(self, size):
        self.chambers = [0] * size

    def addChamber(self, chamber):
        self.chambers[chamber.name] = chamber

