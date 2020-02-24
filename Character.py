import pygame


class Character:
    def __init__(self, health, attack, armour, m_type, char_img, img_w, img_h):
        self.health = health
        self.attack = attack
        self.armour = armour
        self.m_type = m_type
        self.x = 0
        self.y = 0
        self.x_change = 0
        self.y_change = 0
        self.char_img = char_img
        self.img_w = img_w
        self.img_h = img_h
        self.direction = ""
        self.weapon_img_left = None
        self.weapon_img_right = None
        self.armour_img = None
        self.magic = ""
        self.show_weapon_left = False
        self.show_weapon_right = False

    def add_spell(self, name):
        self.magic = name

    def new_weapon(self, item):
        self.weapon_img_left = item.item_img
        self.weapon_img_right = item.item_img_right

    def new_armour(self, item_img):
        self.armour_img = item_img

    def use_spell(self):
        if self.magic == "heal":
            self.health += 10

    def reset(self):
        self.health = 100
        self.attack = 1
        self.armour = 1
        self.x = 0
        self.y = 0
        self.weapon_img_left = None
        self.weapon_img_right = None


class NPC:
    def __init__(self, x, y, dialog_img, dialog_b_img, npc_img, combo, magic_name):
        self.x = x
        self.combo = combo
        self.y = y
        self.img_w = 100
        self.img_h = 100
        self.dialog_img = dialog_img
        self.npc_img = npc_img
        self.spell_buffer = ""
        self.dialog_b_img = dialog_b_img
        self.magic_name = magic_name

    def unlock_spell(self, combo, char):
        if combo == self.combo:
            self.dialog_img = self.dialog_b_img
            char.add_spell(self.magic_name)

    def add_to_spell_buffer(self, key, char):
        self.spell_buffer += key
        if len(self.spell_buffer) == len(self.combo):
            self.unlock_spell(self.spell_buffer, char)
            self.spell_buffer = ""


class Tidabite:
    def __init__(self, x, y, npc_img, npc_img_right=pygame.image.load('art/tidabite0.png'), damage=25):
        self.x = x
        self.y = y
        self.img_w = 100
        self.img_h = 100
        self.tida_img = npc_img
        self.tida_img_left = npc_img
        self.health = 50
        self.damage = damage
        self.tida_img_right = npc_img_right

    def chase(self, character):
        if self.x < character.x:
            self.x += 7
            self.tida_img = self.tida_img_right
        elif self.x > character.x:
            self.x += -7
            self.tida_img = self.tida_img_left
        if self.y < character.y:
            self.y += 7
        elif self.y > character.y:
            self.y += -7
