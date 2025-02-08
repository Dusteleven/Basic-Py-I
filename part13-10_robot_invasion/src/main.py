# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

robots=[]

#x, y, xvel, yvel



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    rnum_bots = random.randint(0,20)

    if rnum_bots ==1:
        x = random.randint(0, 640-robot.get_width())
        y = 0 - robot.get_height()
        xv =0
        yv=1

        new_bot=[x,y,xv,yv]

        robots.append(new_bot)
    
    for bot in robots:
        window.blit(robot, (bot[0],bot[1]))
        if bot[1]<480-robot.get_height(): # if bot not at bottom
            bot[1]+=bot[3] #bot move down 1
        elif bot[1] == 480-robot.get_height(): #if bot at bottom
            bot[3]=0 #stop y vel
            if bot[0]<=640/2: #move left or right depending on L or R of center
                bot[2]=-1
            else:
                bot[2]=1
            bot[0]+=bot[2]
        elif bot[0] == 0 - robot.get_width() or bot[0]==640+robot.get_width():
            robots.remove(bot)

    pygame.display.flip()


    clock.tick(60)