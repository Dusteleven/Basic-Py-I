import pygame
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0]-robot.get_width()/2
            y = event.pos[1]-robot.get_height()/2
 
            screen.fill((0, 0, 0))
            screen.blit(robot, (x, y))
            pygame.display.flip()
 
        if event.type == pygame.QUIT:
            exit()