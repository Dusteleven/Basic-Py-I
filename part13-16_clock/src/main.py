# WRITE YOUR SOLUTION HERE:



import pygame, math, time

pygame.init()
display = pygame.display.set_mode((640, 480))

display.fill((0, 0, 0))

clock = pygame.time.Clock()
start_time = time.time()


minute_angle=90
second_angle=90
hour_angle=90

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    elapsed_time=int(time.time()-start_time)
    hours=elapsed_time//3600
    min=(elapsed_time%3600)//60
    seconds=elapsed_time%60

    time_text=(f"{hours:02}:{min:02}:{seconds:02}")
    pygame.display.set_caption(f"{time_text}")






    xs = math.cos(math.radians(minute_angle))*190
    ys = math.sin(math.radians(minute_angle))*190
        
    xm = (math.cos(math.radians(second_angle)))*190
    ym = (math.sin(math.radians(second_angle)))*190

    xh = (math.cos(math.radians(hour_angle)))*190
    yh = (math.sin(math.radians(hour_angle)))*190


    display.fill((0, 0, 0))
    pygame.draw.circle(display, (255, 0, 0), (320,240), 200,5)#outer
    pygame.draw.circle(display, (255, 0, 0), (320,240), 10)#inner
   
    

    pygame.draw.line(display, (0, 0, 255), (320,240), (320 -xs, 240 -ys), 1)#sec
    pygame.draw.line(display, (0, 0, 255), (320,240), (320-xm, 240-ym), 2)#min
    pygame.draw.line(display, (0, 0, 255), (320,240), (320-xh, 240-yh), 5)#hour

    minute_angle+=6
    second_angle+=(6/60)
    hour_angle+=(6/3600)
    if minute_angle>360:
        minute_angle =0
    if second_angle>360:
        second_angle=0
    if hour_angle>360:
        hour_angle=0



    




    pygame.display.flip()
    clock.tick(1)