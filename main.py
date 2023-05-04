import pygame
import sys
import time
import random
import pygame.freetype

from model_implementation import *
from period_implementation import *
from animal_implementation import *

pygame.display.set_caption("PALEO FISHER")

#VARIABLES
#CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (0,51,102)

#INITIALIZATION
pygame.init()

#VARIABLES
#FONT / TEXT
ui_font = pygame.font.SysFont('goudyoldstyle', 20)
clock_font = pygame.font.SysFont('goudyoldstyle', 20)

periodinfo_font = pygame.font.SysFont('goudyoldstyle', 18)
animalinfo_font = pygame.font.SysFont('goudyoldstyle', 20)
unknown_font = pygame.font.SysFont('goudyoldstyle', 17)
new_font = pygame.font.SysFont('goudyoldstyle', 50)

global curr_period_text
global next_period_countdown

global clock_text_color
global clock_text

global player_health_text
global player_speed_text
global player_score_text
global player_total_text

#VARIABLES
#PAUSE
global pause_enabled
global game_pause
pause_enabled = False
game_pause = False

#VARIABLES
#GAME MANAGEMENT
clock = pygame.time.Clock()
global creatures
global curr_year
global curr_period
global time_0
global highscore
global new_game
global start_period
global hit_by_enemy

creatures = [0]*30
global creatures_found
global creatures_unknown

global prestige1a_text
global prestige1b_text
global prestige2a_text
global prestige2b_text
global prestige3_text

curr_year = 541
curr_period = 0
time_0 = time.time()
highscore = 0
new_game = True
start_period = False
hit_by_enemy = False

creatures_found = 0
creatures_unknown = 30

prestige1a_text = unknown_font.render('*   _____?_____', True, (255, 255, 255))
prestige1b_text = unknown_font.render('*   _____?_____', True, (255, 255, 255))
prestige2a_text = unknown_font.render('**   _____?_____', True, (255, 255, 255))
prestige2b_text = unknown_font.render('**   _____?_____', True, (255, 255, 255))
prestige3_text = unknown_font.render('***   _____?_____', True, (255, 255, 255))

enemy_direction_time = 0
fish_wait_time = int(random.randint(2, 3))
waiting_for_fish = False

curr_period_text = ui_font.render('CAMBRIAN PERIOD', True, (255, 255, 255))
next_period_countdown = 56
clock_text_color = (255, 255, 255)
clock_text = clock_font.render(str(curr_year) + ' MYA | '+str(next_period_countdown)+' MILLION YEARS LEFT |', True, clock_text_color)
new_creature_found_text = new_font.render('NEW!', True, (139, 0, 0))

player_health_text = ui_font.render('HEALTH: ' + str(player.healthbar()), True, (255, 255, 255))
player_speed_text = ui_font.render('SPEED: ' + str(player.speedbar()), True, (255, 255, 255))
player_score_text = ui_font.render('SCORE: ' + '{:0.1f}'.format(player.score), True, (255, 255, 255))
player_total_text = ui_font.render('ANIMALS CAUGHT: ' + str(player.net), True, (255, 255, 255))

#VARIABLES
#SOUNDS
water_splash_sound = pygame.mixer.Sound("water_splash.wav")
water_splash_sound.set_volume(0.5)
water_movement_sound = pygame.mixer.Sound("water_movement.wav")
water_movement_sound.set_volume(0.5)
underwater_splash_sound = pygame.mixer.Sound("underwater_splash.wav")
underwater_splash_sound.set_volume(0.5)
clock_chime_sound = pygame.mixer.Sound("chime.wav")
clock_chime_sound.set_volume(0.25)
metal_bang_sound = pygame.mixer.Sound("metal_bang.wav")
metal_bang_sound.set_volume(0.5)
sea_creature_sound = pygame.mixer.Sound('sea_creature.wav')
sea_creature_sound.set_volume(0.75)
crash_wood_sound = pygame.mixer.Sound('crash_wood.wav')
crash_wood_sound.set_volume(0.75)
repair_ship_sound = pygame.mixer.Sound('hammering.wav')
repair_ship_sound.set_volume(0.5)

global play_ocean_sound

play_ocean_sound = True
player_disabled = False
powerup_time = 0
play_metal_bang_sound = True

#FUNCTION
#PARAGRAPH GENERATOR
def compact_text(screen, text, pos, font, font_color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x, y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, font_color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= SCREEN_WIDTH:
                x = pos[0]
                y += word_height
            screen.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

#FUNCTION
#RESET DISCOVERED PERIOD ANIMALS DISPLAY
def reset_prestige_text():
    global prestige1a_text
    global prestige1b_text
    global prestige2a_text
    global prestige2b_text
    global prestige3_text
    prestige1a_text = unknown_font.render('*   _____?_____', True, (255, 255, 255))
    prestige1b_text = unknown_font.render('*   _____?_____', True, (255, 255, 255))
    prestige2a_text = unknown_font.render('**   _____?_____', True, (255, 255, 255))
    prestige2b_text = unknown_font.render('**   _____?_____', True, (255, 255, 255))
    prestige3_text = unknown_font.render('***   _____?_____', True, (255, 255, 255))

#FUNCTION
#UPDATE COLLECTION OF CAUGHT / DISCOVERED ANIMALS
def beastiary():
    global creatures
    found = 0
    global creatures_found
    global creatures_unknown
    for x in creatures:
        if x == True:
            found += 1
    creatures_found = found
    creatures_unknown = 30 - found

#FUNCTION
#UPDATE PERIOD OVER TIME
def updatePeriod(screen, year):
    global curr_period_text
    global clock_text_color
    global clock_font
    global curr_period
    global prestige1a_text
    global prestige1b_text
    global prestige2a_text
    global prestige2b_text
    global prestige3_text
    global start_period
    global next_period_countdown
    ordovician_year_start = 485
    silurian_year_start = 444
    devonian_year_start = 419
    carboniferous_year_start = 359
    permian_year_start = 299
    
    if (year - ordovician_year_start == 5) and (year - ordovician_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - ordovician_year_start == 4) and (year - ordovician_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - ordovician_year_start == 3) and (year - ordovician_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - ordovician_year_start == 2) and (year - ordovician_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - ordovician_year_start == 1) and (year - ordovician_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    
    if (year - silurian_year_start == 5) and (year - silurian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - silurian_year_start == 4) and (year - silurian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - silurian_year_start == 3) and (year - silurian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - silurian_year_start == 2) and (year - silurian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - silurian_year_start == 1) and (year - silurian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    
    if (year - devonian_year_start == 5) and (year - devonian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - devonian_year_start == 4) and (year - devonian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - devonian_year_start == 3) and (year - devonian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - devonian_year_start == 2) and (year - devonian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - devonian_year_start == 1) and (year - devonian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    
    if (year - carboniferous_year_start == 5) and (year - carboniferous_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - carboniferous_year_start == 4) and (year - carboniferous_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - carboniferous_year_start == 3) and (year - carboniferous_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - carboniferous_year_start == 2) and (year - carboniferous_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - carboniferous_year_start == 1) and (year - carboniferous_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    
    if (year - permian_year_start == 5) and (year - permian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - permian_year_start == 4) and (year - permian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - permian_year_start == 3) and (year - permian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - permian_year_start == 2) and (year - permian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - permian_year_start == 1) and (year - permian_year_start > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)

    if (year - 252 == 5) and (year - 252 > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - 252 == 4) and (year - 252 > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - 252 == 3) and (year - 252 > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)
    elif (year - 252 == 2) and (year - 252 > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 20)
    elif (year - 252 == 1) and (year - 252 > 0):
        clock_font = pygame.font.SysFont('goudyoldstyle', 22)

    if (year == silurian_year_start - 5) or (year == devonian_year_start - 5) or (year == carboniferous_year_start - 5) or (year == permian_year_start - 5):
        buoyObstacle2.set_location()
        buoyObstacle2.enabled = True

    if year == ordovician_year_start:
        ordPeriod.display_text(screen, ordPeriod.compile_information(), (10, 10), periodinfo_font, (255, 255, 255))
        reset_prestige_text()
        player.flip = False
        player.curr_action = 0
        player.start_pos()
        enemy.start_pos()
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        buoyObstacle.set_location()
        buoyObstacle2.ypos = SCREEN_HEIGHT*2
        curr_period = 1
        print(curr_period)
        pygame.mixer.Sound.play(clock_chime_sound)
        information_screen(False)
        next_period_countdown = 41
        curr_period_text = ui_font.render('ORDOVICIAN PERIOD', True, (255, 255, 255))
        count_down()
        start_period = True
    elif year == silurian_year_start:
        silPeriod.display_text(screen, silPeriod.compile_information(), (10, 10), periodinfo_font, (255, 255, 255))
        reset_prestige_text()
        player.flip = False
        player.curr_action = 0
        player.start_pos()
        enemy.start_pos()
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        buoyObstacle.set_location()
        buoyObstacle2.ypos = SCREEN_HEIGHT*2
        buoyObstacle2.enabled = False
        curr_period = 2
        pygame.mixer.Sound.play(clock_chime_sound)
        information_screen(False)
        next_period_countdown = 25
        curr_period_text = ui_font.render('SILURIAN PERIOD', True, (255, 255, 255))
        count_down()
        start_period = True
    elif year == devonian_year_start:
        devPeriod.display_text(screen, devPeriod.compile_information(), (10, 10), periodinfo_font, (255, 255, 255))
        reset_prestige_text()
        player.flip = False
        player.curr_action = 0
        player.start_pos()
        enemy.start_pos()
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        buoyObstacle.set_location()
        buoyObstacle2.ypos = SCREEN_HEIGHT*2
        buoyObstacle2.enabled = False
        curr_period = 3
        pygame.mixer.Sound.play(clock_chime_sound)
        information_screen(False)
        next_period_countdown = 60
        curr_period_text = ui_font.render('DEVONIAN PERIOD', True, (255, 255, 255))
        count_down()
        start_period = True
    elif year == carboniferous_year_start:
        carPeriod.display_text(screen, carPeriod.compile_information(), (10, 10), periodinfo_font, (255, 255, 255))
        reset_prestige_text()
        player.flip = False
        player.curr_action = 0
        player.start_pos()
        enemy.start_pos()
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        buoyObstacle.set_location()
        buoyObstacle2.ypos = SCREEN_HEIGHT*2
        buoyObstacle2.enabled = False
        curr_period = 4
        pygame.mixer.Sound.play(clock_chime_sound)
        information_screen(False)
        next_period_countdown = 60
        curr_period_text = ui_font.render('CARBONIFEROUS PERIOD', True, (255, 255, 255))
        count_down()
        start_period = True
    elif year == permian_year_start:
        perPeriod.display_text(screen, perPeriod.compile_information(), (10, 10), periodinfo_font, (255, 255, 255))
        reset_prestige_text()
        player.flip = False
        player.curr_action = 0
        player.start_pos()
        enemy.start_pos()
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        buoyObstacle.set_location()
        buoyObstacle2.ypos = SCREEN_HEIGHT*2
        buoyObstacle2.enabled = False
        curr_period = 5
        pygame.mixer.Sound.play(clock_chime_sound)
        information_screen(False)
        next_period_countdown = 47
        curr_period_text = ui_font.render('PERMIAN PERIOD', True, (255, 255, 255))
        count_down()
        start_period = True
    elif year == 252:
        end_game()
        return
'''                                                     '''
'''                                                     '''
'''                                                     '''
'''                 MAIN MENU SCREEN                    '''
'''                                                     '''
'''                                                     '''
'''                                                     '''
def main_menu():
    pygame.mixer.music.load('shoreline.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)
    waiting = True
    menu = True
    instructions = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and menu == True:
                    pygame.mixer.music.stop()
                    waiting = False
                if event.key == pygame.K_f:
                    instructions = True
                    if instructions:
                        screen.fill((255, 255, 255))
                        menu = False
                        text = 'HOW TO PLAY\n\n\n'
                        text += '   CONTROLS\n'
                        text += '        HOW TO MOVE: WASD or ARROW KEYS\n'
                        text += '        HOW TO TOGGLE FISHING: SPACEBAR\n'
                        text += '        WHERE TO FISH: ripples in the water\n'
                        text += '        (if you are properly fishing, \'waiting for fish...\' will appear above your player)\n'
                        text += '        HOW TO PAUSE: P\n\n\n'
                        text += '   GOAL\n'
                        text += '        HOW TO WIN: reach the end of the Paleozoic Era with the highest score possible\n'
                        text += '        HOW TO REACH THE END: do not let your health hit 0\n'
                        text += '        HOW TO NOT LOSE HEALTH: do not let ocean buoys or large animals hit the ship\n'
                        text += '        HOW TO INCREASE SCORE: catch as many fish as possible\n\n\n'
                        text += '   TIPS\n'
                        text += '        Keep your health and speed as high as possible.\n'
                        text += '        Floating BARRELS will appear, collect these to increase your HEALTH.\n'
                        text += '        Floating OARS will appear, collect these to increase your SPEED.\n'
                        text += '        (your HEALTH and SPEED can not exceed their maximums)\n'
                        text += '        (time will STOP when an animal is caught or a new period begins; you have time to read informational screens)\n\n\n'
                        text += '[ PRESS \'G\' TO RETURN TO MENU ]'
                        screen.blit(art_credit_text, (SCREEN_WIDTH - art_credit_text.get_width(), SCREEN_HEIGHT - art_credit_text.get_height()))
                        compact_text(screen, text, (5,5), menu_font, (0,0,0))
                if event.key == pygame.K_g:
                    menu = True
                    instructions = False

        if menu:
            screen.fill((255, 255, 255))
            title_font = pygame.font.SysFont('Camrbia', 75)
            menu_font = pygame.font.SysFont('Camrbia', 25)
            title_text = title_font.render('Paleo Fisher', True, (0,0,0))
            continue_text = menu_font.render('[ PRESS \'ENTER\' TO WARP THROUGH TIME AND SET SAIL! ]', True, (0,0,0))
            how_to_play_text = menu_font.render('[ PRESS \'F\' FOR INSTRUCTIONS ]', True, (0,0,0))
            art_credit_text = menu_font.render('Animal Art Director: Ryan Madden ', True, (0,0,0))
            screen.blit(title_text, (SCREEN_WIDTH/2 - (title_text.get_width()/2), SCREEN_HEIGHT/5))
            screen.blit(how_to_play_text, (SCREEN_WIDTH/2 - (how_to_play_text.get_width()/2), SCREEN_HEIGHT/5 + (title_text.get_height())))
            screen.blit(continue_text, (SCREEN_WIDTH/2 - (continue_text.get_width()/2), SCREEN_HEIGHT/5 + (title_text.get_height() + continue_text.get_height())))
            screen.blit(art_credit_text, (SCREEN_WIDTH - art_credit_text.get_width(), SCREEN_HEIGHT - art_credit_text.get_height()))
        pygame.display.update()
        clock.tick(40)
'''                                                     '''
'''                                                     '''
'''                                                     '''
'''                 PLAYER PAUSE SCREEN                 '''
'''                                                     '''
'''                                                     '''
'''                                                     '''
def paused(screen, current_time):
    global play_ocean_sound
    global curr_period
    global pause_enabled

    global prestige1a_text
    global prestige1b_text
    global prestige2a_text
    global prestige2b_text
    global prestige3_text

    pygame.mixer.music.pause()
    
    play_ocean_sound = True
    pause = True
    pause_enabled = True

    pause_font = pygame.font.SysFont('Camrbia', 150)
    continue_font = pygame.font.SysFont('Camrbia', 25)

    pause_text = pause_font.render('PAUSED', True, (255, 255, 255))
    continue_text = continue_font.render('[ PRESS \'P\' TO CONTINUE FISHING ]', True, (255, 255, 255))

    screen.blit(clock_text, (1, 20))
    screen.blit(curr_period_text, (1, 1))
    screen.blit(player_health_text, (1,45))
    screen.blit(player_speed_text, (1,65))
    screen.blit(player_total_text, (SCREEN_WIDTH - 210,1))
    screen.blit(player_score_text, (SCREEN_WIDTH - 210,21))
    if oarPowerup.enabled:
        screen.blit(oarPowerup.img[oarPowerup.curr_img], (oarPowerup.xpos, oarPowerup.ypos))
    if barrelPowerup.enabled:
        screen.blit(barrelPowerup.img[barrelPowerup.curr_img], (barrelPowerup.xpos, barrelPowerup.ypos))
    screen.blit(prestige1a_text, (SCREEN_WIDTH - 400,1))
    screen.blit(prestige1b_text, (SCREEN_WIDTH - 400,21))
    screen.blit(prestige2a_text, (SCREEN_WIDTH - 400,41))
    screen.blit(prestige2b_text, (SCREEN_WIDTH - 400,61))
    screen.blit(prestige3_text, (SCREEN_WIDTH - 400,81))

    player.update(screen)

    if curr_period >= 1:
        enemy.update(screen)

    buoyObstacle.update(current_time, screen, buoyobstacle1)
    buoyObstacle2.update(current_time, screen, buoyobstacle2)

    fishArea1.update(screen, current_time)
    fishArea2.update(screen, current_time)
    fishArea3.update(screen, current_time)
    fishArea4.update(screen, current_time)
    fishArea5.update(screen, current_time)

    screen.blit(pause_text, (SCREEN_WIDTH/2 - (pause_text.get_width()/2), SCREEN_HEIGHT/2))
    screen.blit(continue_text, (SCREEN_WIDTH/2 - (continue_text.get_width()/2), SCREEN_HEIGHT/2 + 100))
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    pause_enabled = False
        pygame.display.update()
        clock.tick(40)
'''                                                     '''
'''                                                     '''
'''                                                     '''
'''                 ANIMAL / PERIOD SCREEN              '''
'''                                                     '''
'''                                                     '''
'''                                                     '''
def information_screen(animal_screen):
    global play_ocean_sound
    pygame.mixer.music.pause()
    if animal_screen:
        pygame.mixer.music.load('pirateship.wav')
        pygame.mixer.music.play(-1)
    play_ocean_sound = True
    global game_pause
    game_pause = True
    while game_pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if animal_screen:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.Sound.stop(clock_chime_sound)
                        pygame.mixer.Sound.stop(sea_creature_sound)
                        pygame.mixer.Sound.stop(crash_wood_sound)
                        game_pause = False
                else:
                    if event.key == pygame.K_f:
                        pygame.mixer.Sound.stop(clock_chime_sound)
                        game_pause = False
        
        pygame.display.update()
        clock.tick(40)  
'''                                                     '''
'''                                                     '''
'''                                                     '''
'''                 END GAME SCREEN                     '''
'''                                                     '''
'''                                                     '''
'''                                                     '''
def end_game():
    with open('highscores.txt', 'r+') as read_file:
        highscores = read_file.readlines()

    check_score = True
    initials_complete = False

    highscore1 = highscores[0].strip()
    highscore2 = highscores[1].strip()
    highscore3 = highscores[2].strip()
    highscore4 = highscores[3].strip()
    highscore5 = highscores[4].strip()

    highscore1value = float(highscore1[14:])
    highscore2value = float(highscore1[14:])
    highscore3value = float(highscore1[14:])
    highscore4value = float(highscore1[14:])
    highscore5value = float(highscore1[14:])

    global curr_year
    global time_0
    global highscore
    global new_game
    global creatures
    global clock_text
    global player_health_text
    global player_speed_text
    global player_score_text
    global player_total_text
    global curr_period_text
    global creatures_found
    global hit_by_enemy
    game_end = True
    pygame.mixer.music.load('pirateship.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)
    total_achievements = 0
    achievements_text = '\nACHIEVEMENTS:\n\n'
    if player.health == 5:
        achievements_text += 'MASTER SHIPWRIGHT (FINISH WITH FULL HEALTH)\n'
        total_achievements += 1
    if player.net >= 50:
        achievements_text += 'MASTER ANGLER (CATCH 50+ ANIMALS)\n'
        total_achievements += 1
    if player.score >= 500:
        achievements_text += 'TROPHY ANGLER (SCORE 500+ POINTS)\n'
        total_achievements += 1
    if hit_by_enemy:
        achievements_text += 'CAPTAIN AHAB (ENCOUNTER A BEAST OF THE SEA)\n'
        total_achievements += 1
    if creatures_found >= 22:
        achievements_text += 'MARINE BIOLOGIST (DISCOVER OVER 75% OF TOTAL ANIMALS)\n'
        total_achievements += 1
    achievements_text += '\n[ '+str(total_achievements)+' OUT OF 5 ACHIEVEMENTS ACCOMPLISHED ]'
    
    font = pygame.font.SysFont('Camrbia', 30)
    playagain_text = font.render('[ PRESS \'F\' TO RETURN TO MENU ]', True, (0,0,0))
    enter_initials_text = font.render('PLEASE ENTER YOUR INITIALS: ', True, (0,0,0))

    while game_end:
        if len(player.initials) == 3:
            initials_complete = True
            if player.score > highscore1value and check_score:
                highscore5 = highscore4
                highscore4 = highscore3
                highscore3 = highscore2
                highscore2 = highscore1
                highscore1 = '1     '+(player.initials).upper()+'     '+str(player.score)
                check_score = False
            elif player.score > highscore2value and check_score:
                highscore5 = highscore4
                highscore4 = highscore3
                highscore3 = highscore2
                highscore2 = '1     '+(player.initials).upper()+'     '+str(player.score)
                check_score = False
            elif player.score > highscore3value and check_score:
                highscore5 = highscore4
                highscore4 = highscore3
                highscore3 = '1     '+(player.initials).upper()+'     '+str(player.score)
                check_score = False
            elif player.score > highscore3value and check_score:
                highscore5 = highscore4
                highscore4 = highscore3
                highscore3 = '1     '+(player.initials).upper()+'     '+str(player.score)
                check_score = False
            elif player.score > highscore4value and check_score:
                highscore5 = highscore4
                highscore4 = '1     '+(player.initials).upper()+'     '+str(player.score)
                check_score = False
            elif player.score > highscore5value and check_score:
                highscore5 = '1     '+(player.initials).upper()+'     '+str(player.score)
                check_score = False
            else:
                check_score = False
        with open('highscores.txt', 'w') as write_file:
            write_file.writelines(highscores)

        screen.fill((255, 255, 255))
        
        screen.blit(enter_initials_text, (10, SCREEN_HEIGHT-playagain_text.get_height()*2-enter_initials_text.get_height()*2))

        highscore_text = font.render('HIGHSCORES:', True, (0,0,0))
        highscore1_text = font.render(str(highscore1), True, (0,0,0))
        highscore2_text = font.render(str(highscore2), True, (0,0,0))
        highscore3_text = font.render(str(highscore3), True, (0,0,0))
        highscore4_text = font.render(str(highscore4), True, (0,0,0))
        highscore5_text = font.render(str(highscore5), True, (0,0,0))

        playerscore_text = font.render('SCORE: '+'{:0.1f}'.format(player.score), True, (0,0,0))
        creatures_caught_text = font.render('TOTAL FISH: '+str(player.net), True, (0,0,0))

        screen.blit(playerscore_text, (10, 10))
        screen.blit(creatures_caught_text, (10, 30))

        screen.blit(highscore_text, (SCREEN_WIDTH-300, 10))
        screen.blit(highscore1_text, (SCREEN_WIDTH-300, 30))
        screen.blit(highscore2_text, (SCREEN_WIDTH-300, 50))
        screen.blit(highscore3_text, (SCREEN_WIDTH-300, 70))
        screen.blit(highscore4_text, (SCREEN_WIDTH-300, 90))
        screen.blit(highscore5_text, (SCREEN_WIDTH-300, 110))

        if initials_complete:
            screen.blit(playagain_text, (10, SCREEN_HEIGHT-playagain_text.get_height()*2))

        compact_text(screen, achievements_text, (10,50), font, (0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                read_file.close()
                write_file.close()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and not (event.key == pygame.K_f) and len(player.initials) != 3:
                player.initials += event.unicode
                enter_initials_text = font.render('PLEASE ENTER YOUR INITIALS: '+(player.initials).upper(), True, (0,0,0))
                print(player.initials)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and len(player.initials) == 3:
                    read_file.close()
                    write_file.close()
                    game_end = False
                    new_game = True
                    creatures = [0]*30
                    curr_year = 541
                    time_0 = time.time()
                    player.initials = ''
                    player.speed = 2
                    player.curr_speed = 2
                    player.health = 5
                    player.fishing = False
                    player.score = 0
                    player.net = 0
                    pygame.mixer.music.stop()
                    clock_text = clock_font.render(str(curr_year) + ' MYA | '+str(next_period_countdown)+' MILLION YEARS LEFT |', True, clock_text_color)
                    player_health_text = ui_font.render('HEALTH: ' + str(player.healthbar()), True, (255, 255, 255))
                    player_speed_text = ui_font.render('SPEED: ' + str(player.speedbar()), True, (255, 255, 255))
                    player_score_text = ui_font.render('SCORE: ' + '{:0.1f}'.format(player.score), True, (255, 255, 255))
                    player_total_text = ui_font.render('ANIMALS CAUGHT: ' + str(player.net), True, (255, 255, 255))
                    curr_period_text = ui_font.render('CAMBRIAN PERIOD', True, (255, 255, 255))
                    reset_prestige_text()
        pygame.display.update()
        clock.tick(40)  
'''                                                     '''
'''                                                     '''
'''                                                     '''
'''                 COUNT DOWN SCREEN                   '''
'''                                                     '''
'''                                                     '''
'''                                                     '''
def count_down():
    global curr_period
    wait = True
    time_0 = time.time()
    count = 3
    count_font = pygame.font.SysFont('Camrbia', 150)
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        count_text = count_font.render(str(count), True, (255, 255, 255))
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, (1,50,32), pygame.Rect(0, 0, SCREEN_WIDTH, 100))
        screen.blit(clock_text, (1, 20))
        screen.blit(curr_period_text, (1, 1))
        screen.blit(player_health_text, (1,45))
        screen.blit(player_speed_text, (1,65))
        screen.blit(player_total_text, (SCREEN_WIDTH - 210,1))
        screen.blit(player_score_text, (SCREEN_WIDTH - 210,21))
        screen.blit(prestige1a_text, (SCREEN_WIDTH - 400,1))
        screen.blit(prestige1b_text, (SCREEN_WIDTH - 400,21))
        screen.blit(prestige2a_text, (SCREEN_WIDTH - 400,41))
        screen.blit(prestige2b_text, (SCREEN_WIDTH - 400,61))
        screen.blit(prestige3_text, (SCREEN_WIDTH - 400,81))
        screen.blit(count_text, (SCREEN_WIDTH/2 - (count_text.get_width()/2), SCREEN_HEIGHT/2))
        player.update(screen)
        if curr_period >= 1:
            enemy.update(screen)
        time_1 = time.time()
        if time_1 - time_0 >= 1: #increments every 'n' seconds
            count -= 1
            time_0 = time_1
        if count <= 0:
            wait = False
        pygame.display.update()
        clock.tick(40)  
'''                                             '''
'''                                             '''
'''                                             '''
'''                 GAME LOOP                   '''
'''                                             '''
'''                                             '''
'''                                             '''
while True:

    current_time = pygame.time.get_ticks()

    if new_game:
        main_menu()
        pygame.mixer.Sound.play(clock_chime_sound)
        camPeriod.display_text(screen, camPeriod.compile_information(), (10, 10), periodinfo_font, (255, 255, 255))
        player.start_pos()
        enemy.start_pos()
        buoyObstacle.set_location()
        print(curr_period)
        information_screen(False)
        count_down()
        new_game = False
    
    if play_ocean_sound:
        pygame.mixer.music.load('ocean_ship.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.25)
        play_ocean_sound = False

    #check if game is paused; else decrement 'curr_year' by 1 per second passed
    if pause_enabled == False:
        time_1 = time.time()
        if time_1 - time_0 >= 1.5: #increments every 'n' seconds
            curr_year -= 1
            time_0 = time_1
            next_period_countdown -= 1

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, (1,50,32), pygame.Rect(0, 0, SCREEN_WIDTH, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.curr_action = 0
                #player.flip = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.curr_action = 0
                #player.flip = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.curr_action = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.curr_action = 0
            if event.key == pygame.K_SPACE and player.canfish == True:
                if player.fishing == False:
                    player.curr_action = 1
                    player.fishing = True
                else:
                    player.curr_action = 0
                    player.fishing = False
            if event.key == pygame.K_p:
                paused(screen, current_time)

    # update and dispaly fishing area ripples
    fishArea1.update(screen, current_time)
    fishArea2.update(screen, current_time)
    fishArea3.update(screen, current_time)
    fishArea4.update(screen, current_time)
    fishArea5.update(screen, current_time)


    # every 3 seconds the enemy will either follow the player (hunting speed) or wonder aimlessly (wondering speed)
    if curr_period >= 1:
        if enemy_direction_time + 3000 < current_time:
            enemy.change_direction(player.xpos, player.ypos, player.speed)
            enemy_direction_time = current_time
        enemy.move()
        enemy.update(screen)

    # update and display player movements
    player.handle_keys()
    player.update(screen)
    # display time, player stats, and period
    clock_text = clock_font.render(str(curr_year) + ' MYA | '+str(next_period_countdown)+' MILLION YEARS LEFT |', True, clock_text_color)
    clock_text_color = (255, 255, 255)
    clock_font = pygame.font.SysFont('goudyoldstyle', 20)

    player_health_text = ui_font.render('HEALTH: ' + str(player.healthbar()), True, (255, 255, 255))
    player_speed_text = ui_font.render('SPEED: ' + str(player.speedbar()), True, (255, 255, 255))
    player_score_text = ui_font.render('SCORE: ' + '{:0.1f}'.format(player.score), True, (255, 255, 255))
    player_total_text = ui_font.render('ANIMALS CAUGHT: ' + str(player.net), True, (255, 255, 255))
    screen.blit(clock_text, (1, 20))
    updatePeriod(screen, curr_year)
    screen.blit(curr_period_text, (1, 1))

    screen.blit(player_health_text, (1,45))
    screen.blit(player_speed_text, (1,65))
    screen.blit(player_total_text, (SCREEN_WIDTH - 210,1))
    screen.blit(player_score_text, (SCREEN_WIDTH - 210,21))
    screen.blit(prestige1a_text, (SCREEN_WIDTH - 400,1))
    screen.blit(prestige1b_text, (SCREEN_WIDTH - 400,21))
    screen.blit(prestige2a_text, (SCREEN_WIDTH - 400,41))
    screen.blit(prestige2b_text, (SCREEN_WIDTH - 400,61))
    screen.blit(prestige3_text, (SCREEN_WIDTH - 400,81))
    # create player and fishing area hitboxes and check for collisions while fishing
    player_hitbox = player.actions[player.curr_action].get_rect()
    player_hitbox.topleft = (player.xpos, player.ypos)
    fishArea1Hitbox = fishArea1.actions[fishArea1.curr_action][fishArea1.curr_frame].get_rect()
    fishArea1Hitbox.topleft = (fishArea1.xpos, fishArea1.ypos)
    fishArea2Hitbox = fishArea2.actions[fishArea2.curr_action][fishArea2.curr_frame].get_rect()
    fishArea2Hitbox.topleft = (fishArea2.xpos, fishArea2.ypos)
    fishArea3Hitbox = fishArea3.actions[fishArea3.curr_action][fishArea3.curr_frame].get_rect()
    fishArea3Hitbox.topleft = (fishArea3.xpos, fishArea3.ypos)
    fishArea4Hitbox = fishArea4.actions[fishArea4.curr_action][fishArea4.curr_frame].get_rect()
    fishArea4Hitbox.topleft = (fishArea4.xpos, fishArea4.ypos)
    fishArea5Hitbox = fishArea5.actions[fishArea5.curr_action][fishArea5.curr_frame].get_rect()
    fishArea5Hitbox.topleft = (fishArea5.xpos, fishArea5.ypos)

    if player.fishing == False:
        fish_wait_time = int(random.randint(2, 3))
    if ((pygame.Rect.colliderect(player_hitbox, fishArea1Hitbox) and fishArea1.active == True) or (pygame.Rect.colliderect(player_hitbox, fishArea2Hitbox) and fishArea2.active == True) or (pygame.Rect.colliderect(player_hitbox, fishArea3Hitbox) and fishArea3.active == True) or (pygame.Rect.colliderect(player_hitbox, fishArea4Hitbox) and fishArea4.active == True) or (pygame.Rect.colliderect(player_hitbox, fishArea5Hitbox) and fishArea5.active == True)) and player.fishing:
        fish_1 = time.time()
        if waiting_for_fish == False:
            fish_0 = time.time()
            waiting_for_fish = True
        if fish_1 - fish_0 >= 1:
            print('waiting for fish')
            fish_wait_time -= 1
            fish_0 = fish_1
        fishing_text = ui_font.render('waiting for fish...', True, (255, 255, 255))
        screen.blit(fishing_text, (player.xpos, player.ypos - player.height))
        
        if fish_wait_time <= 0:
            print('fishing')
            creature_val = int(random.randint(0, 4))
            caught_creature = creatures_list[curr_period][creature_val]
            if pygame.Rect.colliderect(player_hitbox, fishArea1Hitbox):
                fishArea1.active = False
            if pygame.Rect.colliderect(player_hitbox, fishArea2Hitbox):
                fishArea2.active = False
            if pygame.Rect.colliderect(player_hitbox, fishArea3Hitbox):
                fishArea3.active = False
            if pygame.Rect.colliderect(player_hitbox, fishArea4Hitbox):
                fishArea4.active = False
            if pygame.Rect.colliderect(player_hitbox, fishArea5Hitbox):
                fishArea5.active = False
            caught_creature.generate_size()
            caught_creature.generate_rating()
            caught_creature.display_text(screen, caught_creature.compile_information(), (10, 10), animalinfo_font, (255, 255, 255))
            if creatures[caught_creature.id] == 0:
                screen.blit(new_creature_found_text, (SCREEN_WIDTH - 450, 10))
                if creature_val == 0:
                    prestige1a_text = unknown_font.render('*   '+(caught_creature.genus[7:len(caught_creature.genus)]).upper(), True, (255, 255, 255))
                elif creature_val == 1:
                    prestige1b_text = unknown_font.render('*   '+(caught_creature.genus[7:len(caught_creature.genus)]).upper(), True, (255, 255, 255))
                elif creature_val == 2:
                    prestige2a_text = unknown_font.render('**   '+(caught_creature.genus[7:len(caught_creature.genus)]).upper(), True, (255, 255, 255))
                elif creature_val == 3:
                    prestige2b_text = unknown_font.render('**   '+(caught_creature.genus[7:len(caught_creature.genus)]).upper(), True, (255, 255, 255))
                elif creature_val == 4:
                    prestige3_text = unknown_font.render('***   '+(caught_creature.genus[7:len(caught_creature.genus)]).upper(), True, (255, 255, 255))
            creatures[caught_creature.id] += 1
            beastiary()
            player.net += 1
            player.score += caught_creature.rating_val
            pygame.mixer.Sound.play(water_movement_sound)
            caught_creature.update(screen)
            information_screen(True)
            pygame.mixer.Sound.play(water_splash_sound)
            waiting_for_fish = False
            fish_wait_time = int(random.randint(2, 3))
            player.curr_action = 0
    
    barrel_hitbox = barrelPowerup.img[barrelPowerup.curr_img].get_rect()
    barrel_hitbox.topleft = (barrelPowerup.xpos, barrelPowerup.ypos)
    oar_hitbox = oarPowerup.img[oarPowerup.curr_img].get_rect()
    oar_hitbox.topleft = (oarPowerup.xpos, oarPowerup.ypos)

    buoy_hitbox = buoyObstacle.img[buoyObstacle.curr_img].get_rect()
    buoy_hitbox.topleft = (buoyObstacle.xpos, buoyObstacle.ypos)
    buoy_hitbox2 = buoyObstacle2.img[buoyObstacle2.curr_img].get_rect()
    buoy_hitbox2.topleft = (buoyObstacle2.xpos, buoyObstacle2.ypos)

    enemy_hitbox = enemy.actions[enemy.curr_action].get_rect()
    enemy_hitbox.w = (enemy.width*3)/4
    enemy_hitbox.h = (enemy.height*3)/4
    enemy_hitbox.topleft = (enemy.xpos+(enemy.width/8), enemy.ypos+(enemy.height/8))

    buoy1 = int(random.randint(1,2))
    buoy2 = int(random.randint(1,2))

    buoyobstacle1 = int(random.randint(1,2))
    buoyobstacle2 = int(random.randint(1,2))

    if player_disabled:
        if player_disabled_time + 1500 < current_time:
            player.speed = player.curr_speed
            buoyObstacle.enabled = True
            buoyObstacle2.enabled = True
            player_disabled = False

    if powerup_time + 30000 < current_time:
        oarPowerup.enabled = False
        barrelPowerup.enabled = False
        if player.health < 5 and player.speed < 3:
            chance = int(random.randint(1,2))
            if chance == 1:
                oarPowerup.enabled = True
                oarPowerup.set_location()
            else:
                barrelPowerup.enabled = True
                barrelPowerup.set_location()
        elif player.health < 5:
            barrelPowerup.enabled = True
            barrelPowerup.set_location()
        elif player.speed < 3:
            oarPowerup.enabled = True
            oarPowerup.set_location()
        else:
            pass
        powerup_time = current_time

    if pygame.Rect.colliderect(player_hitbox, buoy_hitbox):
        if play_metal_bang_sound and player_disabled == False:
            metal_bang_sound.play()
        play_metal_bang_sound = False
        player_disabled_time = current_time
        player_disabled = True
        buoyObstacle.hit_player(player)
        buoyObstacle.enabled = False
        player.speed = 0
        if player.curr_speed == 3:
            player.curr_speed = 2

    if pygame.Rect.colliderect(player_hitbox, buoy_hitbox2):
        if play_metal_bang_sound and player_disabled == False:
            metal_bang_sound.play()
        play_metal_bang_sound = False
        player_disabled_time = current_time
        player_disabled = True
        buoyObstacle2.hit_player(player)
        buoyObstacle2.enabled = False
        player.speed = 0
        if player.curr_speed == 3:
            player.curr_speed = 2

    if not (pygame.Rect.colliderect(player_hitbox, buoy_hitbox) or pygame.Rect.colliderect(player_hitbox, buoy_hitbox)):
        play_metal_bang_sound = True

    if pygame.Rect.colliderect(player_hitbox, barrel_hitbox) and barrelPowerup.enabled == True:
        if play_repair_sound and player.health < 5:
            repair_ship_sound.play()
        barrelPowerup.applyBonus(player)
        play_repair_sound = False
        barrelPowerup.enabled = False
    if barrelPowerup.enabled:
        barrelPowerup.update(current_time, screen, buoy1)

    if not (pygame.Rect.colliderect(player_hitbox, barrel_hitbox)):
        play_repair_sound = True

    if pygame.Rect.colliderect(player_hitbox, oar_hitbox) and oarPowerup.enabled == True:
        oarPowerup.applyBonus(player)
        oarPowerup.enabled = False
    if oarPowerup.enabled:
        oarPowerup.update(current_time, screen, buoy2)

    if not (pygame.Rect.colliderect(player_hitbox, enemy_hitbox)):
        play_enemy_sounds = True
            
    if pygame.Rect.colliderect(player_hitbox, enemy_hitbox):
        hit_by_enemy = True
        if play_enemy_sounds:
            pygame.mixer.Sound.play(crash_wood_sound)
            pygame.mixer.Sound.play(sea_creature_sound)
        play_enemy_sounds = False
        enemy.display_text(screen, enemy.compile_information(curr_period), (10, 10), animalinfo_font, (255, 255, 255))
        if curr_period == 1:
            screen.blit(endoceras_enemy_img, (SCREEN_WIDTH - endoceras_enemy_img.get_width()-10, SCREEN_HEIGHT - endoceras_enemy_img.get_height()-10))
        elif curr_period == 2:
            screen.blit(eurypterid_enemy_img, (SCREEN_WIDTH - eurypterid_enemy_img.get_width()-10, SCREEN_HEIGHT - eurypterid_enemy_img.get_height()-10))
        elif curr_period == 3:
            screen.blit(dunkleosteus_enemy_img, (SCREEN_WIDTH - dunkleosteus_enemy_img.get_width()-10, SCREEN_HEIGHT - dunkleosteus_enemy_img.get_height()-10))
        elif curr_period == 4:
            screen.blit(edestus_enemy_img, (SCREEN_WIDTH - edestus_enemy_img.get_width()-10, SCREEN_HEIGHT - edestus_enemy_img.get_height()-10))
        elif curr_period == 5:
            screen.blit(helicoprion_enemy_img, (SCREEN_WIDTH - helicoprion_enemy_img.get_width()-10, SCREEN_HEIGHT - helicoprion_enemy_img.get_height()-10))
        player.start_pos()
        enemy.start_pos()
        enemy.hit_player(player)
        if player.curr_speed == 3:
            player.curr_speed = 2
        information_screen(True)

    
    buoyObstacle.update(current_time, screen, buoyobstacle1)
    if curr_period >= 2:
        buoyObstacle2.update(current_time, screen, buoyobstacle2)

    if player.health <= 0:
        print('GAME OVER')
        pygame.quit()
        sys.exit

    # update game display
    pygame.display.update()
    clock.tick(40) #40 fps