

import pygame
pygame.init()
width,height = 640,480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")


positions = [[0,0],[width-robot.get_width(), height-robot.get_height()]]

controls = []

# key, which robot moves, horizontal movement, vertical movement
controls.append((pygame.K_LEFT, 0, -2, 0))
controls.append((pygame.K_RIGHT, 0, 2, 0))
controls.append((pygame.K_UP, 0, 0, -2))
controls.append((pygame.K_DOWN, 0, 0, 2))
controls.append((pygame.K_a, 1, -2, 0))
controls.append((pygame.K_d, 1, 2, 0))
controls.append((pygame.K_w, 1, 0, -2))
controls.append((pygame.K_s, 1, 0, 2))

clock = pygame.time.Clock()

key_pressed={}

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed[event.key]=True   #adds to key pressed dict

        if event.type == pygame.KEYUP:
            del key_pressed[event.key]
        
        if event.type == pygame.QUIT:
            exit()

    for key in controls:
        if key[0] in key_pressed: #if key pressed
            positions[key[1]][0] += key[2] #positions at 0 or 1 robot (0 index = x starting) += key[2] =x movement
            positions[key[1]][1] += key[3] #positions at 0 or 1 robot (1 index = y starting) += y movement

    screen.fill((0, 0, 0))
    for i in range(2):
        screen.blit(robot, (positions[i][0], positions[i][1]))
    pygame.display.flip()
 
    clock.tick(60)    