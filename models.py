import pygame
import random
from images import *

#VARIABLES
#CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (0, 51, 102)
PURPLE = (230,230,250)

''' FISHERMAN MODEL '''
class Fisherman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.initials = ''
        #SPRITE CHARACTERISTICS
        self.width = 50
        self.height = 25
        self.xpos = -self.width
        self.ypos = -self.height

        self.speed = 2
        self.curr_speed = 2
        self.health = 5
        self.score = 0
        self.net = 0

        #OTHER VARIABLES
        self.fishing = False
        self.canfish = True

        #ANIMATION VARIABLES
        self.actions = []
        self.curr_action = 0
        self.flip = False

    def healthbar(self):
        if self.health == 5:
            return '[O] [O] [O] [O] [O]'
        elif self.health == 4:
            return '[O] [O] [O] [O] [X]'
        elif self.health == 3:
            return '[O] [O] [O] [X] [X]'
        elif self.health == 2:
            return '[O] [O] [X] [X] [X]'
        elif self.health == 1:
            return '[O] [X] [X] [X] [X]'
        else:
            return '[X] [X] [X] [X] [X]'
        
    def speedbar(self):
        if self.speed == 3:
            return '[>] [>] [>]'
        elif self.speed == 2:
            return '[>] [>] [_]'
        else:
            return '[_] [_] [_]'

    #FUNC: sets start position
    def start_pos(self):
        self.xpos = self.width*2
        self.ypos = ((SCREEN_HEIGHT-100)/2 + 100) - self.height/2

    #FUNC: sets images
    def add_images(self, idle, fishing): #(self, spritesheet)
        self.actions.append(idle)
        self.actions.append(fishing)

    # EDIT RECT STUFF
    #FUNC: handles player movement
    def handle_keys(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.xpos < (SCREEN_WIDTH - self.width):
            self.xpos += self.speed
            self.canfish = False
            self.fishing = False
            self.flip = False
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.xpos > 0:
            self.xpos -= self.speed
            self.canfish = False
            self.fishing = False
            self.flip = True
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and self.ypos > 105: #100 length of menu block rect
            self.ypos -= self.speed
            self.canfish = False
            self.fishing = False
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.ypos < (SCREEN_HEIGHT - self.height):
            self.ypos += self.speed
            self.canfish = False
            self.fishing = False
        else:
            self.canfish = True
    
    def update(self, screen):
        if self.flip == False:
            screen.blit(self.actions[self.curr_action], (self.xpos, self.ypos))
        if self.flip == True:
            screen.blit((pygame.transform.flip(self.actions[self.curr_action], True, False).convert_alpha()), (self.xpos, self.ypos))
    
''' ENEMY MODEL '''
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #SPRITE CHARACTERISTICS
        self.width = 100
        self.height = 50
        self.xpos = -self.width
        self.ypos = -self.height
        self.direction = -1
        self.moving_up = False
        self.moving_down = True

        self.damage = 2

        self.speed = 2

        #ANIMATION VARIABLES
        self.actions = []
        self.curr_action = 0
        self.flip = False

    def hit_player(self, player):
        player.health -= self.damage

    #FUNC: sets start position
    def start_pos(self):
        self.xpos = SCREEN_WIDTH + self.width
        self.ypos = ((SCREEN_HEIGHT-100)/2 + 100) - self.height/2

    #FUNC: sets images
    def add_images(self, moving1, moving2, moving3): #(self, spritesheet)
        self.actions.append(moving1)
        self.actions.append(moving2)
        self.actions.append(moving3)

    #FUNC: move enemy
    def move(self):
        self.xpos += (self.speed)*self.direction
        if self.moving_up:
            self.ypos -= 1
        elif self.moving_down:
            self.ypos += 1
        self.curr_action += 1
        if self.curr_action > 2:
            self.curr_action = 0

        #CHECK X BOUNDS
        if self.xpos < 0:
            #self.xpos = SCREEN_WIDTH
            self.direction = 1
        elif self.xpos + self.width > SCREEN_WIDTH:
            #self.xpos = 0
            self.direction = -1
        #CHECK Y BOUNDS
        if self.ypos < 100:
            #self.ypos = SCREEN_HEIGHT
            self.moving_up = False
            self.moving_down = True
        elif self.ypos + self.height > SCREEN_HEIGHT:
            #self.ypos = 100
            self.moving_up = True
            self.moving_down = False
        
    def change_direction(self, player_xpos, player_ypos, player_speed):
        follow_chance = int(random.randint(0, 4))
        if (follow_chance == 0) or (follow_chance == 1):
            self.speed = player_speed + 1
            print('following')
            if player_xpos < self.xpos and self.direction == 1:
                self.direction*=-1
            if player_ypos > self.ypos and player_ypos < (self.ypos + self.height):
                self.moving_up = False
                self.moving_down = False
            elif player_ypos > self.ypos and self.moving_down == False:
                self.moving_up = False
                self.moving_down = True
            elif player_ypos < self.ypos and self.moving_up == False:
                self.moving_up = True
                self.moving_down = False
        else:
            self.speed = 2
            print('wondering')
            left_right_chance = int(random.randint(0, 1))
            up_down_chance = int(random.randint(0, 2))
            if left_right_chance == 0:
                self.direction*=-1
            if up_down_chance == 0:
                self.moving_up = False
                self.moving_down = False
            elif up_down_chance == 1:
                self.moving_up = True
                self.moving_down = False
            elif up_down_chance == 2:
                self.moving_up = False
                self.moving_down = True

    def compile_information(self, curr_period):
        if curr_period == 1:
            text = 'An endoceras has struck the ship...\n'
            text += 'These large straight shelled cephalopods roamed the waters from the Middle to Upper Ordovician...\n\n'
            text += '...be wary, these waters aren\'t safe...\n\n'
            text += '[ PRESS \'SPACEBAR\' TO CONTINUE FISHING ]'
        elif curr_period == 2:
            text = 'An pterygotus has struck the ship...\n'
            text += 'These giant predatory eurypterids (sea scorpions) roamed the waters from the Middle Silurian to Late Devonian...\n\n'
            text += '...be wary, these waters aren\'t safe...\n\n'
            text += '[ PRESS \'SPACEBAR\' TO CONTINUE FISHING ]'
        elif curr_period == 3:
            text = 'An dunkleosteus has struck the ship...\n'
            text += 'These enormous armored fish were the largest animals to exist up to this point in time and roamed the waters during the Late Devonian...\n\n'
            text += '...be wary, these waters aren\'t safe...\n\n'
            text += '[ PRESS \'SPACEBAR\' TO CONTINUE FISHING ]'
        elif curr_period == 4:
            text = 'An edestus has struck the ship...\n'
            text += 'These giant cartilaginous fish had curved blade-like teeth and roamed the waters during the Late Carboniferous...\n\n'
            text += '...be wary, these waters aren\'t safe...\n\n'
            text += '[ PRESS \'SPACEBAR\' TO CONTINUE FISHING ]'
        elif curr_period == 5:
            text = 'An helicoprion has struck the ship...\n'
            text += 'These huge shark-like fish had curved blade-like teeth and roamed the waters during the Permian...\n\n'
            text += '...be wary, these waters aren\'t safe...\n\n'
            text += '[ PRESS \'SPACEBAR\' TO CONTINUE FISHING ]'
        return text

    def display_text(self, screen, text, pos, font, font_color):
        background_color = (0,0,0) #black
        pygame.draw.rect(screen, background_color, pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
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
    
    #FUNC: blits/animates enemy on screen
    def update(self, screen):
        if self.direction == -1:
            screen.blit(self.actions[self.curr_action], (self.xpos, self.ypos))
        if self.direction == 1:
            screen.blit((pygame.transform.flip(self.actions[self.curr_action], True, False).convert_alpha()), (self.xpos, self.ypos))


''' FISH AREA MODEL '''
class FishArea(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #SPRITE CHARACTERISTICS
        self.active = True
        self.period = 0 #0 = cambrian, 5 = permian
        self.width = 30
        self.height = 30
        self.xpos = 0
        self.ypos = 0
        #time between ripples (RANDOM)
        self.wait_time = 250
        #time the last ripple occured
        self.last_ripple = 0
        self.lifespan = 30000
        #time before the ripple location is changed (SET, 12 seconds)
        self.move_ripple_threshold = self.lifespan

        #ANIMATION VARIABLES
        self.actions = [[ripples_img,ripples1_img,ripples2_img,ripples3_img,ripples4_img,
                        ripples5_img,ripples6_img,ripples7_img]]
        self.curr_action = 0
        self.curr_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.cooldown = 100
        self.step = 0

    #FUNC: sets new coordinates
    def set_location(self, new_x, new_y):
        self.xpos = new_x
        self.ypos = new_y
    
    #FUNC: sets new randomized coordinates
    def set_location_random(self):
        self.xpos = int(random.randint(0, SCREEN_WIDTH - self.width))
        self.ypos = int(random.randint((100 + self.height), SCREEN_HEIGHT - self.height))

    def randomly_ripple(self, current_time):
        if (self.move_ripple_threshold - current_time <= 0):
            self.active = True
            self.set_location_random()
            self.move_ripple_threshold = current_time + self.lifespan
        if current_time - self.last_ripple >= self.wait_time:
            if current_time - self.last_update >= self.cooldown:
                self.curr_frame += 1
                self.last_update = current_time
                if self.curr_frame >= len(self.actions[self.curr_action]):
                    self.curr_frame = 0
                    self.last_ripple = current_time
    
    #FUNC: blits/animates ripples on screen
    def update(self, screen, current_time):
        if self.active == True:
            screen.blit(self.actions[self.curr_action][self.curr_frame], (self.xpos, self.ypos))
        self.randomly_ripple(current_time)

''' CREATURE MODEL '''
class Creature(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.id = 0
        self.img = ''
        self.imgxpos = SCREEN_WIDTH - 310
        self.imgypos = 10
        self.min_length = 0
        self.max_length_increment = 0
        self.min_weight = 0
        self.max_weight_increment = 0
        
        self.rarity = 0 #on a scale of 1 (common), 1.25 (uncommon), and 1.5 (rare)
        self.length_val = 0
        self.weight_val = 0
        self.rating_val = 0

        #self.species = '[species]'
        self.genus = '[genus]'
        self.family = '[family]'
        self.order = '[order]'
        self.class_ = '[class]'
        self.phylum = '[phylum]'
        self.prestige = '[prestige]'
        self.length = '[length]'
        self.weight = '[weight]'
        self.description = '[description]'
        self.rating = '[rating]'
        self.p_continue = '[ PRESS \'SPACEBAR\' TO CONTINUE FISHING ]'

    def generate_length(self):
        rand = float(random.randint(0, self.max_length_increment))
        self.length_val = self.min_length + float(rand/100)
        self.length = 'Length: ' + '{:0.2f}'.format(self.length_val) + ' feet'

    def generate_weight(self):
        rand = float(random.randint(0, self.max_weight_increment))
        self.weight_val = self.min_weight + float(rand/100)
        self.weight = 'Weight: ' + '{:0.2f}'.format(self.weight_val) + ' pounds'

    def generate_rating(self):
        scale = 0
        base = 0
        max = 0
        if self.rarity == 0: #5-15
            scale = 1
            max = 15.0
            base = 5.0
        elif self.rarity == 1: #10-20
            scale = 1
            max = 20.0
            base = 10.0
        else: #15-25
            scale = 1
            max = 25.0
            base = 15.0
        l_frac = ((self.length_val*100)-self.min_length*100) / (self.max_length_increment)
        w_frac = ((self.weight_val*100)-self.min_weight*100) / (self.max_weight_increment)
        frac_average = ((l_frac+w_frac)/2)*10
        self.rating_val = base + (scale * frac_average)
        self.rating = 'Rating: '+'{:0.1f}'.format(self.rating_val)+' / '+str(max)

    def generate_size(self):
        self.generate_length()
        self.generate_weight()
    
    def compile_information(self):
        text = ''
        text += self.genus+'\n'
        text += self.family+'\n'
        text += self.order+'\n'
        text += self.class_+'\n'
        text += self.phylum+'\n\n'
        text += self.length+'\n'
        text += self.weight+'\n\n'
        text += self.description+'\n\n'
        text += self.prestige+'\n'
        text += self.rating+'\n\n'
        text += self.p_continue
        return text
    
    def add_image(self, img):
        self.img = img

    def display_text(self, screen, text, pos, font, font_color): #make pos 55, 55
        background_color = (101, 67, 33) #brown
        pygame.draw.rect(screen, background_color, pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(planks_img, (0,0))
        screen.blit(planks_img, (250,0))
        screen.blit(planks_img, (500,0))
        screen.blit(planks_img, (750,0))
        screen.blit(planks_img, (0,250))
        screen.blit(planks_img, (250,250))
        screen.blit(planks_img, (500,250))
        screen.blit(planks_img, (750,250))
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
    
    def update(self, screen):
        screen.blit(self.img, (self.imgxpos, self.imgypos))

''' PERIOD MODEL '''
class Period(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.width = 0
        self.height = 0
        self.xpos = (SCREEN_WIDTH / 2) - self.width
        self.ypos = (SCREEN_HEIGHT / 2) - self.height
        self.period_val = -1

        self.period = 'PERIOD: '
        self.timeframe = 'TIMEFRAME: '
        self.description = '[description]'
        self.p_continue = '[ PRESS \'F\' TO START FISHING ]'

    def compile_information(self):
        text = ''
        text += self.period+'\n'
        text += self.timeframe+'\n\n'
        text += self.description+'\n\n'
        text += self.p_continue
        return text
    
    def display_text(self, screen, text, pos, font, color):
        pygame.draw.rect(screen, (1,50,32), pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        collection = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]
        x, y = pos
        for lines in collection:
            for words in lines:
                word_surface = font.render(words, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= SCREEN_WIDTH:
                    x = pos[0]
                    y += word_height
                screen.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

''' POWERUP MODEL '''
class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.width = 20
        self.height = 25
        self.xpos = SCREEN_WIDTH
        self.ypos = int(random.randint(100,SCREEN_HEIGHT-self.height))
        
        self.drift = 0
        self.interval = 500
        self.threshold = 0
        self.curr_img = 2
        self.img = []
        self.enabled = False
        self.speed_bonus = 0
        self.health_bonus = 0

    def add_image(self, img, tilt_img_more_left, tilt_img_left, tilt_img_right, tilt_img_more_right):
        self.img.append(tilt_img_more_left)
        self.img.append(tilt_img_left)
        self.img.append(img)
        self.img.append(tilt_img_right)
        self.img.append(tilt_img_more_right)
    
    def set_location(self):
        self.xpos = int(random.randint(0, SCREEN_WIDTH-self.width))
        self.ypos = int(random.randint(100, SCREEN_HEIGHT-self.height))

    def applyBonus(self, player):
        if self.enabled:
            if player.health < 5:
                if player.health + self.health_bonus > 5:
                    player.health = 5
                else:
                    player.health += self.health_bonus
            if player.speed == 3:
                pass
            else:
                player.speed += self.speed_bonus
                player.curr_speed = player.speed
            self.enabled = False
        else:
            pass
    
    def float(self, curr_time, bouy):
        if (self.threshold + self.interval) - curr_time <= 0:
            self.drift = int(random.randint(1,2))
            if bouy == 1 and self.curr_img < 4:
                self.curr_img += 1
            elif bouy == 1 and self.curr_img == 4: 
                self.curr_img -= 1
            if bouy == 2 and self.curr_img > 0:
                self.curr_img -= 1
            elif bouy == 2 and self.curr_img == 0: 
                self.curr_img += 1
            self.threshold = curr_time
            
    def update(self, curr_time, screen, bouy):
        self.float(curr_time, bouy)
        screen.blit(self.img[self.curr_img], (self.xpos, self.ypos))

''' BUOY OBSTACLE MODEL '''
class BuoyObstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.width = 30
        self.height = 50
        self.xpos = -self.width
        self.ypos = -self.height
        
        self.drift = 0
        self.interval = 250
        self.threshold = 0
        self.curr_img = 4
        self.img = []
        self.enabled = True
        self.damage = 1

    def add_image(self, buoy_img1, buoy_img2, buoy_img3, buoy_img_left1, buoy_img_left2, buoy_img_left3, buoy_img_right1, buoy_img_right2, buoy_img_right3):
        self.img.append(buoy_img_left3)
        self.img.append(buoy_img_left2)
        self.img.append(buoy_img_left1)
        self.img.append(buoy_img3)
        self.img.append(buoy_img2)
        self.img.append(buoy_img1)
        self.img.append(buoy_img_right1)
        self.img.append(buoy_img_right2)
        self.img.append(buoy_img_right3)

    def set_location(self):
        self.xpos = SCREEN_WIDTH + self.width
        self.ypos = int(random.randint(100,SCREEN_HEIGHT-self.height))

    def hit_player(self, player):
        if self.enabled:
            player.health -= self.damage
        self.enabled = False
    
    def move(self, curr_time, bouy):
        if self.enabled == True and (self.xpos + self.width < 0):
            self.set_location()
        self.xpos -= 1
        if self.drift == 1:
            if self.ypos <= 100:
                self.ypos += 0.50
            self.ypos -= 0.50
        if self.drift == 2:
            if self.ypos+self.height >= SCREEN_HEIGHT:
                self.ypos -= 0.50
            self.ypos += 0.50
        if (self.threshold + self.interval) - curr_time <= 0:
            self.drift = int(random.randint(1,2))
            if bouy == 1 and self.curr_img < 8:
                self.curr_img += 1
            elif bouy == 1 and self.curr_img == 8: 
                self.curr_img -= 1
            if bouy == 2 and self.curr_img > 0:
                self.curr_img -= 1
            elif bouy == 2 and self.curr_img == 0: 
                self.curr_img += 1
            self.threshold = curr_time

    def update(self, curr_time, screen, bouy):
        self.move(curr_time, bouy)
        screen.blit(self.img[self.curr_img], (self.xpos, self.ypos))