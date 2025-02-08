# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
rockimg = pygame.image.load("rock.png")
rocks=[]
points=0
target_x=0
target_y=0


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        #robot moves with mouse
        if event.type == pygame.MOUSEMOTION:
            target_x = event.pos[0]-robot.get_width()/2
            target_y = event.pos[1]-robot.get_height()/2

    rnum_bots = random.randint(0,1)

    if rnum_bots ==1:
        x = random.randint(0, 640-rockimg.get_width())
        y = 0 #- rockimg.get_height()################
        xv =0
        yv=1
        new_bot=[x,y,xv,yv]
        rocks.append(new_bot)
    
    for rock in rocks:
        window.blit(rockimg, (rock[0],rock[1]))
        rock[1]+=rock[3] #bot move down 1
        
        if rock[1]>=480-robot.get_height():
            rockrange=[rock[0], rock[0]+rockimg.get_width()]
            botrange=[target_x,target_x+robot.get_width()]

            if rockrange[0]<botrange[1] and rockrange[1]>botrange[0]:
                points+=1
                rocks.remove(rock)

    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {points}", True, (255,0,0))
    window.blit(text, (480,0))


    
    window.blit(robot, (target_x, 480-robot.get_height()))
    pygame.display.flip()

    window.fill((0, 0, 0))
    clock.tick(100)

    if event.type == pygame.QUIT:
            exit(0)
