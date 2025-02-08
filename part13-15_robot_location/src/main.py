# WRITE YOUR SOLUTION HERE:
import pygame
import random
import os
print("Current working directory:", os.getcwd())

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

#clock = pygame.time.Clock()

range_x = range(0, robot.get_width())
range_y = range(0, robot.get_height())
r_x=0
r_y=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range_x and event.pos[1] in range_y:
                r_x = random.randint(0, 640-robot.get_width())
                r_y = random.randint(0, 480-robot.get_height())
                range_x = range(r_x, r_x+ robot.get_width())
                range_y = range(r_y, r_y+robot.get_height())

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (r_x, r_y))
    pygame.display.flip()

    #clock.tick(60)