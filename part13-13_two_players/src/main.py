# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()

x2 = 0
y2 = 480-robot.get_height()

to_right = False
to_left = False
to_up = False
to_down = False

to_right_two = False
to_left_two = False
to_up_two = False
to_down_two = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

            if event.key == pygame.K_w:
                to_up_two = True
            if event.key == pygame.K_a:
                to_left_two = True
            if event.key == pygame.K_s:
                to_down_two = True
            if event.key == pygame.K_d:
                to_right_two = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False

            if event.key == pygame.K_w:
                to_up_two = False
            if event.key == pygame.K_a:
                to_left_two = False
            if event.key == pygame.K_s:
                to_down_two = False
            if event.key == pygame.K_d:
                to_right_two = False

        if event.type == pygame.QUIT:
            exit()

    if to_right:
        x += 4
    if to_left:
        x -= 4
    if to_up:
        y-=4
    if to_down:
        y+=4

    if x<0: x=0
    elif x> 640-robot.get_width():
        x=640-robot.get_width()
    if y<0: y=0
    elif y>480-robot.get_height():
        y=480-robot.get_height()


    if to_right_two:
        x2 += 4
    if to_left_two:
        x2 -= 4
    if to_up_two:
        y2-=4
    if to_down_two:
        y2+=4

    if x2<0: x2=0
    elif x2> 640-robot.get_width():
        x2=640-robot.get_width()
    if y2<0: y2=0
    elif y2>480-robot.get_height():
        y2=480-robot.get_height()








    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2,y2))
    pygame.display.flip()

    clock.tick(60)