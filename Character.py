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
        self.direction = "right"
        self.weaponImg = None
        self.armourImg = None
        self.magic = ""

    def addSpell(self, name):
        self.magic = name
        
    def newWeapon(self, itemImg):
        self.weaponImg = itemImg

    def newArmour(self, itemImg):
        self.armourImg = itemImg

    def useSpell(self):
        if self.magic == "heal":
            self.health += 10


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
    def __init__(self, x, y, NPCImg):
        print()