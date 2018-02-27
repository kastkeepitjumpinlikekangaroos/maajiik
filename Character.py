import pygame


class Character:
    def __init__(self, health, attack, armour, mType, charImg, imgW, imgH):
        self.health = health
        self.attack = attack
        self.armour = armour
        self.mType = mType
        self.x = 0
        self.y = 0
        self.xchange = 0
        self.ychange = 0
        self.charImg = charImg
        self.imgW = imgW
        self.imgH = imgH
        self.direction = ""
        self.weaponImgLeft = None
        self.weaponImgRight = None
        self.armourImg = None
        self.magic = ""
        self.showWeaponLeft = False
        self.showWeaponRight = False
    def addSpell(self, name):
        self.magic = name
        
    def newWeapon(self, item):
        self.weaponImgLeft = item.itemImg
        self.weaponImgRight = item.itemImgRight

    def newArmour(self, itemImg):
        self.armourImg = itemImg

    def useSpell(self):
        if self.magic == "heal":
            self.health += 10

    def reset(self):
        self.health = 100
        self.attack = 1
        self.armour = 1
        self.x = 0
        self.y = 0


class NPC:
    def __init__(self, x, y, dialogImg, dialogbImg, NPCImg, combo, magicName):
        self.x = x
        self.combo = combo
        self.y = y
        self.imgW = 100
        self.imgH = 100
        self.dialogImg = dialogImg
        self.NPCImg = NPCImg
        self.spellBuffer = ""
        self.dialogbImg = dialogbImg
        self.magicName = magicName
        
    def unlockSpell(self, combo, char):
        if combo == self.combo:
            self.dialogImg = self.dialogbImg
            char.addSpell(self.magicName)

    def addToSpellBuffer(self, key, char):
        self.spellBuffer += key
        if len(self.spellBuffer) == len(self.combo):
            self.unlockSpell(self.spellBuffer, char)
            self.spellBuffer = ""


class Tidabite:
    def __init__(self, x, y, NPCImg, NPCImgRight=pygame.image.load('art/tidabite0.png'), damage=25):
        self.x = x
        self.y = y
        self.imgW = 100
        self.imgH = 100
        self.tidaImg = NPCImg
        self.tidaImgLeft = NPCImg
        self.health = 50
        self.damage = damage
        self.tidaImgRight = NPCImgRight

    def chase(self, character):
        if self.x < character.x:
            self.x += 7
            self.tidaImg = self.tidaImgRight
        elif self.x > character.x:
            self.x += -7
            self.tidaImg = self.tidaImgLeft
        if self.y < character.y:
            self.y += 7
        elif self.y > character.y:
            self.y += -7