import pygame
from math import ceil
from helpers import constructGraph, graph, collided, characterInBounds, gameDisplay, show, showText, clock, \
    currentChamber
from Objs import display_width, display_height
import Character


def game_loop(currentChamber):
    constructGraph()
    quit = False
    char = Character.Character(100, 1, 1, "", pygame.image.load('art/hero.png'), 100, 100)
    keys = []
    haveRedKey = False
    haveBlueKey = False
    haveBlackKey = False
    gameover = False
    while not quit:
        if char.health <= 0:
            gameover = True
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if not gameover:
                    if event.key == pygame.K_a:
                        char.xchange = -10
                        char.direction = 'left'
                    if event.key == pygame.K_d:
                        char.xchange = 10
                        char.direction = 'right'
                    if event.key == pygame.K_w:
                        char.ychange = -10
                    if event.key == pygame.K_s:
                        char.ychange = 10
                    if event.key == pygame.K_p:
                        if char.direction == 'left':
                            char.showWeaponLeft = True
                        if char.direction == 'right':
                            char.showWeaponRight = True
                if event.key == pygame.K_RETURN and gameover:
                    constructGraph()
                    currentChamber = 0
                    char.reset()
                    keys = []
                    haveBlackKey = False
                    haveRedKey = False
                    haveBlueKey = False
                    gameover = False
                # red key handling
                if event.key == pygame.K_1:
                    for door in graph.chambers[currentChamber].doors:
                        if collided(char.x, char.y, char.imgW, char.imgH, door.x, door.y, door.width + 100,
                                    door.height + 100) and haveRedKey:
                            door.addToDoorBuffer(str(1))
                    for npc in graph.chambers[currentChamber].npcs:
                        if collided(char.x, char.y, char.imgW, char.imgH, npc.x, npc.y, npc.imgW + 50,
                                    npc.imgH + 50) and haveRedKey:
                            npc.addToSpellBuffer(str(1), char)
                # blue key
                if event.key == pygame.K_2:
                    for door in graph.chambers[currentChamber].doors:
                        if collided(char.x, char.y, char.imgW, char.imgH, door.x, door.y, door.width + 100,
                                    door.height + 100) and haveBlueKey:
                            door.addToDoorBuffer(str(2))
                    for npc in graph.chambers[currentChamber].npcs:
                        if collided(char.x, char.y, char.imgW, char.imgH, npc.x, npc.y, npc.imgW + 50,
                                    npc.imgH + 50) and haveBlueKey:
                            npc.addToSpellBuffer(str(2), char)
                # black key
                if event.key == pygame.K_3:
                    for door in graph.chambers[currentChamber].doors:
                        if collided(char.x, char.y, char.imgW, char.imgH, door.x, door.y, door.width + 100,
                                    door.height + 100) and haveBlackKey:
                            door.addToDoorBuffer(str(3))
                    for npc in graph.chambers[currentChamber].npcs:
                        if collided(char.x, char.y, char.imgW, char.imgH, npc.x, npc.y, npc.imgW + 50,
                                    npc.imgH + 50) and haveBlackKey:
                            npc.addToSpellBuffer(str(3), char)
                if event.key == pygame.K_o:
                    char.useSpell()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    char.xchange = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    char.ychange = 0
                if event.key == pygame.K_p:
                    char.showWeaponLeft = False
                    char.showWeaponRight = False
        if characterInBounds(char):
            char.x += char.xchange
            char.y += char.ychange
        # screen changes
        gameDisplay.fill((13 * (currentChamber + 1), 12 * (currentChamber + 1), 11 * (currentChamber + 1)))
        for door in graph.chambers[currentChamber].doors:
            show(door.x, door.y, door.doorImg)
            if collided(char.x, char.y, char.imgW, char.imgH, door.x, door.y, door.width,
                        door.height) and door.canPass():
                currentChamber = door.destination
                if door.number == 1:
                    char.x = 200
                    char.y = display_height / 2
                elif door.number == 2:
                    char.x = display_width / 2
                    char.y = 200
                elif door.number == 3:
                    char.x = display_width - 200
                    char.y = display_height / 2
                elif door.number == 4:
                    char.x = display_width / 2
                    char.y = display_height - 200
            if door.failedAttempt and door.locked:
                door.doorFlash = True
                door.flashTimer = 0
                door.failedAttempt = False
            if door.doorFlash:
                door.flashTimer += 1
                if door.flashTimer == 10:
                    if door.number % 2 == 0:
                        door.doorImg = pygame.image.load('art/door0.jpg')
                    else:
                        door.doorImg = pygame.image.load('art/door.jpg')
        for tida in graph.chambers[currentChamber].tidas:
            if tida.health > 0:
                show(tida.x, tida.y, tida.tidaImg)
                tida.chase(char)
                if collided(char.x, char.y, char.imgW, char.imgH, tida.x, tida.y, tida.imgW, tida.imgH):
                    if char.x < tida.x:
                        char.x += -15
                    elif char.x >= tida.x:
                        char.x += 15
                    char.health += -ceil(tida.damage / char.armour)
                if collided(char.x - 50, char.y + 25, 50, 50, tida.x, tida.y, tida.imgW,
                            tida.imgH) and char.showWeaponLeft:
                    tida.x += -15
                    tida.health += -char.attack
                if collided(char.x + 100, char.y + 25, 50, 50, tida.x, tida.y, tida.imgW,
                            tida.imgH) and char.showWeaponRight:
                    tida.x += 15
                    tida.health += -char.attack
            else:
                graph.chambers[currentChamber].tidas.remove(tida)
        for chests in graph.chambers[currentChamber].chests:
            show(chests.x, chests.y, chests.chestImg)
            if collided(char.x, char.y, char.imgW, char.imgH, chests.x, chests.y, 100, 100):
                for x in chests.items:
                    graph.chambers[currentChamber].items.append(x)
                    chests.chestImg = pygame.image.load('art/emptyChest.png')
                    chests.items.remove(x)
        for item in graph.chambers[currentChamber].items:
            show(item.x, item.y, item.itemImg)
            if collided(char.x, char.y, char.imgW, char.imgH, item.x, item.y, item.imgW, item.imgH):
                if item.type == 'weapon':
                    char.attack += item.stat
                    char.newWeapon(item)
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
            if collided(char.x, char.y, char.imgW, char.imgH, npc.x, npc.y, npc.imgW + 50, npc.imgH + 50):
                show(display_width / 2 - 400, display_height / 2 - 100, npc.dialogImg)
        showText('attack: ' + str(char.attack) + ' armour: ' + str(char.armour) + ' health: ' + str(char.health), 300,
                 50)
        show(char.x, char.y, char.charImg)
        if char.showWeaponLeft and char.weaponImgLeft is not None:
            show(char.x - 50, char.y + 25, char.weaponImgLeft)
        elif char.showWeaponRight and char.weaponImgRight is not None:
            show(char.x + 100, char.y + 25, char.weaponImgRight)
        if gameover:
            showText('Game OVER', display_width / 2, display_height / 2)
            showText('Enter to play again', display_width / 2, display_height / 2 + 300)
        pygame.display.flip()
        clock.tick(60)


game_loop(currentChamber)
pygame.quit()
quit()
