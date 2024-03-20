import pygame
from pygame.locals import *
import random

#window and playground
size = width, height = (800,600)
road_w = int(width/1.8)
roadmark_w = int(width/80)

#car sizes
carSize = (220, 220)
car2Size = (180,200)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1

pygame.init()
running = True

#window size
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Game")

#background color
screen.fill((34, 7, 38))


#my car
car = pygame.image.load("assets/car.png")
car = pygame.transform.scale(car, carSize)
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8


def randomNum():
    num = random.randint(1,6)
    carNum = "assets/car"+str(num)+".png"
    return carNum


#trafic
car2 = pygame.image.load(randomNum())
car2 = pygame.transform.scale(car2, car2Size)
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

counter = 0
while running:
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up",speed)
    #trafic
    
    car2_loc[1] += speed
    if car2_loc[1]>height:
        if random.randint(0,1) == 0:
            car2 = pygame.image.load(randomNum())
            
            car2 = pygame.transform.scale(car2, car2Size)
            car2_loc = car2.get_rect()
            
            car2_loc.center = left_lane, height*0.2
            car2_loc.center = right_lane, -200
        else:
            car2 = pygame.image.load(randomNum())
            car2 = pygame.transform.scale(car2, car2Size)
            car2_loc = car2.get_rect()

            car2_loc.center = left_lane, height*0.2
            car2_loc.center = left_lane, -200

    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 200:
        print("GAME OVER")
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2),0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2),0])


    #draw graphics
    pygame.draw.rect(
        screen,
        (50,50,50),
        (width/2 - road_w/2, 0, road_w, height)
    )

    pygame.draw.rect(
        screen,
        (227, 212, 102),
        (width / 2 - roadmark_w/2, 0, roadmark_w, height)
    )
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width / 2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)
    )
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width / 2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)
    )

    screen.blit(car, car_loc) 
    screen.blit(car2, car2_loc) 
    pygame.display.update()       

pygame.quit()