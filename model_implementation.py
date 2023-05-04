from models import Fisherman, Enemy, FishArea, Powerup, BuoyObstacle
from images import *

player = Fisherman()
player.add_images(fisherman_idle_img, fisherman_fishing_img) #fisherman_idle_img

fishArea1 = FishArea()
fishArea1.set_location_random()
fishArea2 = FishArea()
fishArea2.set_location_random()
fishArea3 = FishArea()
fishArea3.set_location_random()
fishArea4 = FishArea()
fishArea4.set_location_random()
fishArea5 = FishArea()
fishArea5.set_location_random()

enemy = Enemy()
enemy.add_images(shadow_moving1, shadow_moving2, shadow_moving3)

barrelPowerup = Powerup()
barrelPowerup.health_bonus = 1
barrelPowerup.add_image(barrel_img_more_left, barrel_img_left, barrel_img, barrel_img_right, barrel_img_more_right)

oarPowerup = Powerup()
oarPowerup.speed_bonus = 1
oarPowerup.add_image(oar_img_more_left, oar_img_left, oar_img, oar_img_right, oar_img_more_right)

buoyObstacle = BuoyObstacle()
buoyObstacle.add_image(buoy_img1, buoy_img2, buoy_img3, buoy_img_left1, buoy_img_left2, buoy_img_left3, buoy_img_right1, buoy_img_right2, buoy_img_right3)
buoyObstacle2 = BuoyObstacle()
buoyObstacle2.add_image(buoy_img1, buoy_img2, buoy_img3, buoy_img_left1, buoy_img_left2, buoy_img_left3, buoy_img_right1, buoy_img_right2, buoy_img_right3)
