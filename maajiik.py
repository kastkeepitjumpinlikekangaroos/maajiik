import pygame
import Character
import Objs
pygame.init()
display_width = 1600
display_height = 900
currentChamber = 0
graph = Objs.Graph(19)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gameDisplay = pygame.display.set_mode((display_width, display_height))#has to be a touple
pygame.display.set_caption('Maajiik')
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def showText(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)


def characterInBounds(character):
    if character.x <= 0:
        character.x += 21
    elif character.x >= display_width - character.imgW:
        character.x += -21
    if character.y <= 0:
        character.y += 21
    if character.y >= display_height - character.imgH:
        character.y += -21
    return 0 <= character.x <= display_width - character.imgW and 0 <= character.y <= display_width - character.imgH


def constructGraph():
    #chamber 0
    chamberDoors = [Objs.Door(' ', 2, 3)]
    chamber = Objs.Chamber(0, chamberDoors)
    graph.addChamber(chamber)
    #chamber 1
    chamberDoors = [Objs.Door(' ', 2, 4)]
    chamber = Objs.Chamber(1, chamberDoors)
    chamberItems = [Objs.Item("weapon", 10, 700, display_height - 500, pygame.image.load('art/stiik.png')),
                    Objs.Item("armour", 15, 900, display_height - 300, pygame.image.load('art/cloak.png'))]
    chest = Objs.Chest(400, display_height - 400, chamberItems)
    chamber.addChest(chest)
    graph.addChamber(chamber)
    #chamber 2
    chamberDoors = [Objs.Door(' ', 1, 3), Objs.Door('111', 2, 8)]
    chamber = Objs.Chamber(2, chamberDoors)
    NPC = Character.NPC(100, 100, pygame.image.load('art/dialog2.png'),
                        pygame.image.load('art/dialog2b.png'), pygame.image.load('art/prisoner.png'), '221', "energy")
    chamber.addNpc(NPC)
    graph.addChamber(chamber)
    #chamber 3
    chamberDoors = [Objs.Door(' ', 1, 4), Objs.Door('132', 2, 9), Objs.Door('1', 3, 2), Objs.Door(' ', 4, 0)]
    chamber = Objs.Chamber(3, chamberDoors)
    chamberItems = [Objs.Item("weapon", 3, 700, display_height - 500, pygame.image.load('art/stiik.png')), Objs.Item("armour", 5, 900, display_height - 300, pygame.image.load('art/cloak.png')), Objs.Item('key', 1, 1000, display_height - 600, pygame.image.load('art/redkey.png')), Objs.Item('key', 2, 1200, display_height - 500, pygame.image.load('art/bluekey.png')), Objs.Item('key', 3, 900, display_height - 700, pygame.image.load('art/blackkey.png'))]
    #add chest
    chest = Objs.Chest(400, display_height - 400, chamberItems)
    chamber.addChest(chest)
    #add NPC
    NPC = Character.NPC(display_width - 200, display_height - 200, pygame.image.load('art/dialog3.png'), pygame.image.load('art/dialog3b.png'), pygame.image.load('art/oldman.png'), '123', "heal")
    chamber.addNpc(NPC)
    graph.addChamber(chamber)
    #chamber 4
    chamberDoors = [Objs.Door('1', 1, 5), Objs.Door('2', 2, 10), Objs.Door(' ', 3, 3), Objs.Door('3', 4, 1)]
    chamber = Objs.Chamber(4, chamberDoors)
    graph.addChamber(chamber)
    #chamber 5
    chamberDoors = [Objs.Door(' ', 1, 6), Objs.Door(' ', 3, 4)]
    chamber = Objs.Chamber(5, chamberDoors)
    graph.addChamber(chamber)
    #chamber 6
    chamberDoors = [Objs.Door('bigLock', 1, 7), Objs.Door(' ', 3, 5)]
    chamber = Objs.Chamber(6, chamberDoors)
    graph.addChamber(chamber)
    #chamber 7
    chamberDoors = [Objs.Door(' ', 3, 6)]
    chamber = Objs.Chamber(7, chamberDoors)
    graph.addChamber(chamber)
    #chamber 8
    chamberDoors = [Objs.Door('123', 1, 9), Objs.Door('111', 2, 13), Objs.Door(' ', 4, 2)]
    chamber = Objs.Chamber(8, chamberDoors)
    #add npc
    NPC = Character.NPC(100, 500, pygame.image.load('art/dialog8.png'),
                        pygame.image.load('art/dialog8.png'), pygame.image.load('art/prisonerDying.png'), '', "")
    chamber.addNpc(NPC)
    graph.addChamber(chamber)
    #chamber 9
    chamberDoors = [Objs.Door('212', 1, 10), Objs.Door('321', 2, 14), Objs.Door(' ', 3, 8), Objs.Door('121', 4, 3)]
    chamber = Objs.Chamber(9, chamberDoors)
    # add NPC
    NPC = Character.NPC(display_width / 2 + 400, display_height / 2 + 100, pygame.image.load('art/dialog9.png'),
                        pygame.image.load('art/dialog9.png'), pygame.image.load('art/prisoner.png'), '', "")
    chamber.addNpc(NPC)
    graph.addChamber(chamber)
    #chamber 10
    chamberDoors = [Objs.Door('121', 1, 11), Objs.Door('213', 2, 15), Objs.Door(' ', 3, 9), Objs.Door('111', 4, 4)]
    chamber = Objs.Chamber(10, chamberDoors)
    chamberItems = [Objs.Item("weapon", 15, 700, display_height - 500, pygame.image.load('art/sword.png')),
                    Objs.Item("armour", 15, 900, display_height - 300, pygame.image.load('art/armour.png'))]
    # add chest
    chest = Objs.Chest(400, display_height - 400, chamberItems)
    chamber.addChest(chest)
    # add NPC
    NPC = Character.NPC(50, 50, pygame.image.load('art/dialog10.png'),
                        pygame.image.load('art/dialog10.png'), pygame.image.load('art/prisoner.png'), '', "")
    chamber.addNpc(NPC)
    graph.addChamber(chamber)
    #chamber 11
    chamberDoors = [Objs.Door(' ', 1, 12), Objs.Door(' ', 3, 10)]
    chamber = Objs.Chamber(11, chamberDoors)
    graph.addChamber(chamber)
    #chamber 12
    chamberDoors = [Objs.Door(' ', 3, 11)]
    chamber = Objs.Chamber(12, chamberDoors)
    # add NPC
    NPC = Character.NPC(display_width - 100, display_height/2, pygame.image.load('art/dialog12.png'),
                        pygame.image.load('art/dialog12.png'), pygame.image.load('art/princess.png'), '', "")
    chamber.addNpc(NPC)
    graph.addChamber(chamber)
    #chamber 13
    chamberDoors = [Objs.Door('111', 2, 17), Objs.Door(' ', 4, 8)]
    chamber = Objs.Chamber(13, chamberDoors)
    # add NPC
    NPC = Character.NPC(display_width/2 + 400, display_height/2 + 100, pygame.image.load('art/dialog13.png'),
                        pygame.image.load('art/dialog13.png'), pygame.image.load('art/prisonerDead.png'), '', "")
    chamber.addNpc(NPC)
    graph.addChamber(chamber)
    #chamber 14
    chamberDoors = [Objs.Door('213', 1, 15), Objs.Door('233', 2, 18), Objs.Door(' ', 4, 9)]
    chamber = Objs.Chamber(14, chamberDoors)
    # add NPC
    NPC = Character.NPC(100, display_height - 100, pygame.image.load('art/dialog14.png'),
                        pygame.image.load('art/dialog14.png'), pygame.image.load('art/prisoner.png'), '', "")
    chamber.addNpc(NPC)
    graph.addChamber(chamber)
    #chamber 15
    chamberDoors = [Objs.Door(' ', 1, 16), Objs.Door(' ', 3, 14), Objs.Door(' ', 4, 10)]
    chamber = Objs.Chamber(15, chamberDoors)
    graph.addChamber(chamber)
    #chamber 16
    chamberDoors = [Objs.Door(' ', 3, 15)]
    chamber = Objs.Chamber(16, chamberDoors)
    graph.addChamber(chamber)
    #chamber 17
    chamberDoors = [Objs.Door(' ', 4, 13)]
    chamber = Objs.Chamber(17, chamberDoors)
    # add NPC
    NPC = Character.NPC(display_width / 2 + 400, display_height / 2 + 100, pygame.image.load('art/dialog13.png'),
                        pygame.image.load('art/dialog13.png'), pygame.image.load('art/prisonerDead.png'), '', "")
    chamber.addNpc(NPC)
    # add NPC
    NPC = Character.NPC(100, 100, pygame.image.load('art/dialog13.png'),
                        pygame.image.load('art/dialog13.png'), pygame.image.load('art/prisonerDead.png'), '', "")
    chamber.addNpc(NPC)
    # add NPC
    NPC = Character.NPC(100, 800, pygame.image.load('art/dialog13.png'),
                        pygame.image.load('art/dialog13.png'), pygame.image.load('art/prisonerDead.png'), '', "")
    chamber.addNpc(NPC)
    graph.addChamber(chamber)
    #chamber 18
    chamberDoors = [Objs.Door(' ', 4, 14), Objs.Door('132321233', 2, 0)]
    chamber = Objs.Chamber(18, chamberDoors)
    # add NPC
    NPC = Character.NPC(display_width - 100, display_height - 300, pygame.image.load('art/dialog18.png'),
                        pygame.image.load('art/dialog18.png'), pygame.image.load('art/prisoner.png'), '', "")
    chamber.addNpc(NPC)
    graph.addChamber(chamber)
    graph.addChamber(chamber)


def collided(x1, y1, width1, height1, x2, y2, width2, height2):
    return (x2 <= x1 <= x2 + width2 or x2 <= x1 + width1 <= x2 + width2 or (x1 <= x2 and x1 + width1 >= x2 + width2)) \
           and (y2 <= y1 <= y2 + height2 or y2 <= y1 + height1 <= y2 + height2 or (y1 <= y2 and y1 + height1 >= y2 + height2))


def show(x, y, img):
    gameDisplay.blit(img, (x, y))


def spill(chest):
    for x in chest.items:
        graph.chambers[currentChamber].items.append(x)


def game_loop(currentChamber):
    constructGraph()
    quit = False
    char = Character.Character(100, 1, 1, "", pygame.image.load('art/hero.png'), 100, 100)
    alive = char.health > 0
    keys = []
    haveRedKey = False
    haveBlueKey = False
    haveBlackKey = False
    while not quit and alive:
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    char.xchange = -20
                    char.direction = 'left'
                if event.key == pygame.K_d:
                    char.xchange = 20
                    char.direction = 'right'
                if event.key == pygame.K_w:
                    char.ychange = -20
                    char.direction = 'up'
                if event.key == pygame.K_s:
                    char.ychange = 20
                    char.direction = 'down'
                #red key handling
                if event.key == pygame.K_1:
                    for door in graph.chambers[currentChamber].doors:
                        if collided(char.x, char.y, char.imgW, char.imgH, door.x, door.y, door.width + 100, door.height + 100) and haveRedKey:
                            door.addToDoorBuffer(str(1))
                    for npc in graph.chambers[currentChamber].npcs:
                        if collided(char.x, char.y, char.imgW, char.imgH, npc.x, npc.y, npc.imgW + 50, npc.imgH + 50) and haveRedKey:
                            npc.addToSpellBuffer(str(1), char)
                #blue key
                if event.key == pygame.K_2:
                    for door in graph.chambers[currentChamber].doors:
                        if collided(char.x, char.y, char.imgW, char.imgH, door.x, door.y, door.width + 100, door.height + 100) and haveBlueKey:
                            door.addToDoorBuffer(str(2))
                    for npc in graph.chambers[currentChamber].npcs:
                        if collided(char.x, char.y, char.imgW, char.imgH, npc.x, npc.y, npc.imgW + 50, npc.imgH + 50) and haveBlueKey:
                            npc.addToSpellBuffer(str(2), char)
                #black key
                if event.key == pygame.K_3:
                    for door in graph.chambers[currentChamber].doors:
                        if collided(char.x, char.y, char.imgW, char.imgH, door.x, door.y, door.width + 100, door.height + 100) and haveBlackKey:
                            door.addToDoorBuffer(str(3))
                    for npc in graph.chambers[currentChamber].npcs:
                        if collided(char.x, char.y, char.imgW, char.imgH, npc.x, npc.y, npc.imgW + 50, npc.imgH + 50) and haveBlackKey:
                            npc.addToSpellBuffer(str(3), char)
                if event.key == pygame.K_m:
                    char.useSpell()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    char.xchange = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    char.ychange = 0
        if characterInBounds(char):
            char.x += char.xchange
            char.y += char.ychange
        # screen changes
        gameDisplay.fill((13 * (currentChamber + 1), 12 * (currentChamber + 1), 11 * (currentChamber + 1)))
        for door in graph.chambers[currentChamber].doors:
            show(door.x, door.y, door.doorImg)
            if collided(char.x, char.y, char.imgW, char.imgH, door.x, door.y, door.width, door.height) and door.canPass():
                currentChamber = door.destination
                char.x = display_width/2
                char.y = display_height/2
        for chests in graph.chambers[currentChamber].chests:
            show(chests.x, chests.y, chests.chestImg)
            if collided(char.x, char.y, char.imgW, char.imgH, chests.x, chests.y, 100, 100):
                for x in chests.items:
                    graph.chambers[currentChamber].items.append(x)
                    chests.chestImg = pygame.image.load('art/emptyChest.png')
                    chests.items.remove(x)
        for item in graph.chambers[currentChamber].items:
            show(item.x, item.y, item.itemImg)
            if collided(char.x, char.y, char.imgW, char.imgH, item.x, item.y, 50, 50):
                if item.type == 'weapon':
                    char.attack += item.stat
                    char.newWeapon(item.itemImg)
                elif item.type == 'armour':
                    char.armour += item.stat
                    char.newArmour(item.itemImg)
                elif item.type == 'key':
                    keys.append(item)
                graph.chambers[currentChamber].items.remove(item)

        for key in keys:
            if key.stat == 1:
                show(display_width - 400, 0, key.itemImg)
                haveRedKey = True
            if key.stat == 2:
                show(display_width - 300, 0, key.itemImg)
                haveBlueKey = True
            if key.stat == 3:
                show(display_width - 200, 0, key.itemImg)
                haveBlackKey = True
        for npc in graph.chambers[currentChamber].npcs:
            show(npc.x, npc.y, npc.NPCImg)
            if collided(char.x, char.y, char.imgW, char.imgH, npc.x, npc.y, npc.imgW + 50, npc.imgH+ 50):
                show(display_width/2 - 400, display_height/2 - 100, npc.dialogImg)
        showText('attack: ' + str(char.attack) + ' armour: ' + str(char.armour) + ' health: ' + str(char.health), 300, 50)
        show(char.x, char.y, char.charImg)
        pygame.display.update()
        clock.tick(60)
game_loop(currentChamber)
pygame.quit()
quit()
