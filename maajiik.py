import pygame
from math import ceil
from helpers import construct_graph, graph, collided, character_in_bounds, game_display, show, show_text, clock
from Objs import display_width, display_height
import Character


def game_loop():
    construct_graph()
    quit = False
    char = Character.Character(100, 1, 1, "", pygame.image.load('art/hero.png'), 100, 100)
    keys = []
    have_red_key = False
    have_blue_key = False
    have_black_key = False
    game_over = False
    current_chamber = 0
    while not quit:
        if char.health <= 0:
            game_over = True
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            # handle key down
            if event.type == pygame.KEYDOWN:
                if not game_over:
                    # moving
                    if event.key == pygame.K_a:
                        char.x_change = -10
                        char.direction = 'left'
                    if event.key == pygame.K_d:
                        char.x_change = 10
                        char.direction = 'right'
                    if event.key == pygame.K_w:
                        char.y_change = -10
                    if event.key == pygame.K_s:
                        char.y_change = 10
                    # using weapon
                    if event.key == pygame.K_p:
                        if char.direction == 'left':
                            char.show_weapon_left = True
                        if char.direction == 'right':
                            char.show_weapon_right = True
                    # quit game
                    if event.key == pygame.K_ESCAPE:
                        quit = True
                if event.key == pygame.K_RETURN and game_over:
                    # reset them game
                    construct_graph()
                    current_chamber = 0
                    char.reset()
                    keys = []
                    have_black_key = False
                    have_red_key = False
                    have_blue_key = False
                    game_over = False

                # if a key is used on a door add the key to the door buffer
                # use red key
                if event.key == pygame.K_1:
                    for door in graph.chambers[current_chamber].doors:
                        if collided(char.x, char.y, char.img_w, char.img_h, door.x, door.y, door.width + 100,
                                    door.height + 100) and have_red_key:
                            door.add_to_door_buffer(str(1))
                    for npc in graph.chambers[current_chamber].npcs:
                        if collided(char.x, char.y, char.img_w, char.img_h, npc.x, npc.y, npc.img_w + 50,
                                    npc.img_h + 50) and have_red_key:
                            npc.add_to_spell_buffer(str(1), char)
                # use blue key
                if event.key == pygame.K_2:
                    for door in graph.chambers[current_chamber].doors:
                        if collided(char.x, char.y, char.img_w, char.img_h, door.x, door.y, door.width + 100,
                                    door.height + 100) and have_blue_key:
                            door.add_to_door_buffer(str(2))
                    for npc in graph.chambers[current_chamber].npcs:
                        if collided(char.x, char.y, char.img_w, char.img_h, npc.x, npc.y, npc.img_w + 50,
                                    npc.img_h + 50) and have_blue_key:
                            npc.add_to_spell_buffer(str(2), char)
                # use black key
                if event.key == pygame.K_3:
                    for door in graph.chambers[current_chamber].doors:
                        if collided(char.x, char.y, char.img_w, char.img_h, door.x, door.y, door.width + 100,
                                    door.height + 100) and have_black_key:
                            door.add_to_door_buffer(str(3))
                    for npc in graph.chambers[current_chamber].npcs:
                        if collided(char.x, char.y, char.img_w, char.img_h, npc.x, npc.y, npc.img_w + 50,
                                    npc.img_h + 50) and have_black_key:
                            npc.add_to_spell_buffer(str(3), char)
                if event.key == pygame.K_o:
                    char.use_spell()
            # handle key release
            if event.type == pygame.KEYUP:
                # stop moving
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    char.x_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    char.y_change = 0
                # don't show weapon
                if event.key == pygame.K_p:
                    char.show_weapon_left = False
                    char.show_weapon_right = False
        # don't let user outside the screen
        if character_in_bounds(char):
            char.x += char.x_change
            char.y += char.y_change
        # change background colour depending on chamber we're in
        game_display.fill((13 * (current_chamber + 1), 12 * (current_chamber + 1), 11 * (current_chamber + 1)))

        # show all doors in current chamber
        for door in graph.chambers[current_chamber].doors:
            show(door.x, door.y, door.door_img)
            # if user collides with the door and can pass through put them where they should be in the next chamber
            if collided(char.x, char.y, char.img_w, char.img_h, door.x, door.y, door.width,
                        door.height) and door.can_pass():
                current_chamber = door.destination
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

            # if user failed to open door flash
            if door.failed_attempt and door.locked:
                door.door_flash = True
                door.flash_timer = 0
                door.failed_attempt = False
            if door.door_flash:
                door.flash_timer += 1
                if door.flash_timer == 10:
                    if door.number % 2 == 0:
                        door.door_img = pygame.image.load('art/door0.jpg')
                    else:
                        door.door_img = pygame.image.load('art/door.jpg')

        # show all tidabites in current chamber
        for tida in graph.chambers[current_chamber].tidas:
            if tida.health > 0:
                show(tida.x, tida.y, tida.tida_img)
                tida.chase(char)
                # if user collides with tidabite the user takes damage
                if collided(char.x, char.y, char.img_w, char.img_h, tida.x, tida.y, tida.img_w, tida.img_h):
                    if char.x < tida.x:
                        char.x += -15
                    elif char.x >= tida.x:
                        char.x += 15
                    char.health += -ceil(tida.damage / char.armour)
                # if tidabite get hit by user's weapon it takes damage
                if collided(char.x - 50, char.y + 25, 50, 50, tida.x, tida.y, tida.img_w,
                            tida.img_h) and char.show_weapon_left:
                    tida.x += -15
                    tida.health += -char.attack
                if collided(char.x + 100, char.y + 25, 50, 50, tida.x, tida.y, tida.img_w,
                            tida.img_h) and char.show_weapon_right:
                    tida.x += 15
                    tida.health += -char.attack
            else:
                # remove from chamber if it's dead
                graph.chambers[current_chamber].tidas.remove(tida)

        # show all chests in the current chamber
        for chests in graph.chambers[current_chamber].chests:
            show(chests.x, chests.y, chests.chest_img)
            # if a user collides with a chest spill its contents into the chamber
            if collided(char.x, char.y, char.img_w, char.img_h, chests.x, chests.y, 100, 100):
                for x in chests.items:
                    graph.chambers[current_chamber].items.append(x)
                    chests.chest_img = pygame.image.load('art/emptyChest.png')
                    chests.items.remove(x)

        # show all items in the current chamber
        for item in graph.chambers[current_chamber].items:
            show(item.x, item.y, item.item_img)
            # if user collides with an item handle various types of items
            if collided(char.x, char.y, char.img_w, char.img_h, item.x, item.y, item.img_w, item.img_h):
                if item.type == 'weapon':
                    char.attack += item.stat
                    char.new_weapon(item)
                elif item.type == 'armour':
                    char.armour += item.stat
                    char.new_armour(item.item_img)
                elif item.type == 'key':
                    keys.append(item)
                graph.chambers[current_chamber].items.remove(item)

        # show keys if player has them
        for key in keys:
            if key.stat == 1:
                show(display_width - 400, 0, key.item_img)
                have_red_key = True
            if key.stat == 2:
                show(display_width - 300, 0, key.item_img)
                have_blue_key = True
            if key.stat == 3:
                show(display_width - 200, 0, key.item_img)
                have_black_key = True

        # show NPCs
        for npc in graph.chambers[current_chamber].npcs:
            show(npc.x, npc.y, npc.npc_img)
            # if the player collides with NPC show dialog
            if collided(char.x, char.y, char.img_w, char.img_h, npc.x, npc.y, npc.img_w + 50, npc.img_h + 50):
                show(display_width / 2 - 400, display_height / 2 - 100, npc.dialog_img)

        # show current attack, armour, and health
        show_text(f'attack: {char.attack} armour: {char.armour} health: {char.health}', 300, 50)

        # show character
        show(char.x, char.y, char.char_img)

        # show weapon on either side of character if it should be displayed
        if char.show_weapon_left and char.weapon_img_left is not None:
            show(char.x - 50, char.y + 25, char.weapon_img_left)
        elif char.show_weapon_right and char.weapon_img_right is not None:
            show(char.x + 100, char.y + 25, char.weapon_img_right)

        if game_over:
            show_text('Game OVER', display_width / 2, display_height / 2)
            show_text('Enter to play again', display_width / 2, display_height / 2 + 300)
        pygame.display.flip()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
