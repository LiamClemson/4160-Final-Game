import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


''' FISHERMAN IMAGES '''
fisherman_idle_img = pygame.image.load('fisherman_idle.png').convert_alpha()
fisherman_img = pygame.image.load('fisherman.png').convert_alpha()
fisherman_fishing_img = pygame.image.load('fisherman_fishing.png').convert_alpha()

''' ENEMY IMAGES '''
raw_shadow_moving1 = pygame.image.load('shadow_in_water_1.png').convert_alpha()
raw_shadow_moving2 = pygame.image.load('shadow_in_water_2.png').convert_alpha()
raw_shadow_moving3 = pygame.image.load('shadow_in_water_3.png').convert_alpha()
shadow_moving1 = pygame.transform.scale(raw_shadow_moving1, (50 * 2, 25 * 2))
shadow_moving2 = pygame.transform.scale(raw_shadow_moving2, (50 * 2, 25 * 2))
shadow_moving3 = pygame.transform.scale(raw_shadow_moving3, (50 * 2, 25 * 2))

''' RIPPLES IMAGES '''
ripples_img = pygame.image.load('ripples.png').convert_alpha()
ripples1_img = pygame.image.load('ripples1.png').convert_alpha()
ripples2_img = pygame.image.load('ripples2.png').convert_alpha()
ripples3_img = pygame.image.load('ripples3.png').convert_alpha()
ripples4_img = pygame.image.load('ripples4.png').convert_alpha()
ripples5_img = pygame.image.load('ripples5.png').convert_alpha()
ripples6_img = pygame.image.load('ripples6.png').convert_alpha()
ripples7_img = pygame.image.load('ripples7.png').convert_alpha()


''' CREATURE MODEL IMAGES '''
creature_placeholder_img = pygame.image.load('blank_img.png').convert_alpha()

endoceras_enemy_img = pygame.image.load('endoceras.png').convert_alpha()
eurypterid_enemy_img = pygame.image.load('eurypterid.png').convert_alpha()
dunkleosteus_enemy_img = pygame.image.load('dunkleosteus.png').convert_alpha()
edestus_enemy_img = pygame.image.load('edestus.png').convert_alpha()
helicoprion_enemy_img = pygame.image.load('helicoprion.png').convert_alpha()

redlichia_img = pygame.image.load('redlichia.png').convert_alpha()
peytoia_img = pygame.image.load('peytoia.png').convert_alpha()
titanokorys_img = pygame.image.load('titanokorys.png').convert_alpha()
paradoxide_img = pygame.image.load('paradoxide.png').convert_alpha()
anomalocaris_img = pygame.image.load('anomalocaris.png').convert_alpha()

arandaspis_img = pygame.image.load('arandaspis.png').convert_alpha()
aphetoceras_img = pygame.image.load('aphetoceras.png').convert_alpha()
isoletus_img = pygame.image.load('isoletus.png').convert_alpha()
megalograptus_img = pygame.image.load('megalograptus.png').convert_alpha()
aegirocassis_img = pygame.image.load('aegirocassis.png').convert_alpha()

birkenia_img = pygame.image.load('birkenia.png').convert_alpha()
poraspis_img = pygame.image.load('poraspis.png').convert_alpha()
sphoocheras_img = pygame.image.load('sphoocheras.png').convert_alpha()
entelognathus_img = pygame.image.load('entelognathus.png').convert_alpha()
megamastax_img = pygame.image.load('megamastax.png').convert_alpha()

bothriolepis_img = pygame.image.load('bothriolepis.png').convert_alpha()
cladoselache_img = pygame.image.load('cladoselache.png').convert_alpha()
gemuendina_img = pygame.image.load('gemuendina.png').convert_alpha()
xenacanthus_img = pygame.image.load('xenacanthus.png').convert_alpha()
onychodus_img = pygame.image.load('onychodus.png').convert_alpha()

tristychius_img = pygame.image.load('tristychius.png').convert_alpha()
dracopristis_img = pygame.image.load('dracopristis.png').convert_alpha()
rhizodus_img = pygame.image.load('rhizodus.png').convert_alpha()
orthacanthus_img = pygame.image.load('orthacanthus.png').convert_alpha()
diplocaulus_img = pygame.image.load('diplocaulus.png').convert_alpha()

branchiosaurus_img = pygame.image.load('branchiosaurus.png').convert_alpha()
eryops_img = pygame.image.load('eryops.png').convert_alpha()
prionosuchus_img = pygame.image.load('prionosuchus.png').convert_alpha()
stereosternum_img = pygame.image.load('stereosternum.png').convert_alpha()
lebachacanthus_img = pygame.image.load('lebachacanthus.png').convert_alpha()


''' PLANK BACKGROUND IMAGES '''
planks_img = pygame.image.load('planks.jpg').convert()
planks_img.set_alpha(64)

''' BUOY IMAGES '''
buoy_img1 = pygame.image.load('buoy.png').convert_alpha()
buoy_img2 = pygame.image.load('buoy2.png').convert_alpha()
buoy_img3 = pygame.image.load('buoy3.png').convert_alpha()
buoy_img_left1 = pygame.transform.rotate(buoy_img1, -5)
buoy_img_left2 = pygame.transform.rotate(buoy_img2, -5)
buoy_img_left3 = pygame.transform.rotate(buoy_img3, -5)
buoy_img_right1 = pygame.transform.rotate(buoy_img1, 5)
buoy_img_right2 = pygame.transform.rotate(buoy_img2, 5)
buoy_img_right3 = pygame.transform.rotate(buoy_img3, 5)

''' BARREL IMAGES '''
barrel_img = pygame.image.load('barrel.png').convert_alpha()
barrel_img_left = pygame.transform.rotate(barrel_img, -2.5)
barrel_img_more_left = pygame.transform.rotate(barrel_img, -5)
barrel_img_right = pygame.transform.rotate(barrel_img, 2.5)
barrel_img_more_right = pygame.transform.rotate(barrel_img, 5)

''' OAR IMAGES '''
oar_img = pygame.image.load('oar.png').convert_alpha()
oar_img_left = pygame.transform.rotate(oar_img, -2.5)
oar_img_more_left = pygame.transform.rotate(oar_img, -5)
oar_img_right = pygame.transform.rotate(oar_img, 2.5)
oar_img_more_right = pygame.transform.rotate(oar_img, 5)