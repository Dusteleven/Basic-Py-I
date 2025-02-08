import pygame
import random
import math

# Initialize Pygame

def main():
    pygame.init()

#GRID
    GRID_WIDTH = 12
    GRID_HEIGHT = 12
    CELL_SIZE = 30
    WINDOW_WIDTH = (GRID_WIDTH * CELL_SIZE) #750 width
    WINDOW_HEIGHT = (GRID_HEIGHT * CELL_SIZE) #900 height
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRID_LINE_COLOR = (100, 100, 100)
#BALL
    vel = 1
    ball_radius = 10
    #ball_1x = WINDOW_WIDTH//2 - WINDOW_WIDTH//4
    #ball_1y = WINDOW_HEIGHT//2 - WINDOW_HEIGHT//4 +0.5
    ball_1x=7*30
    ball_1y=11*30
    #ball_1x = 180 +2*ball_radius+12
    #ball_1y = WINDOW_HEIGHT//2 + WINDOW_HEIGHT//3
    ball_1dx = -1
    ball_1dy = 1
    #ball_1dx = -vel+0.2
    #ball_1dy = -vel+0.2
    #ball_1x = random.randint(ball_radius, WINDOW_SIZE - ball_radius)
    #ball_1y = random.randint(ball_radius, WINDOW_SIZE - ball_radius)
    ball_2x = WINDOW_WIDTH//2 - WINDOW_WIDTH//4
    ball_2y = WINDOW_HEIGHT//2 + WINDOW_HEIGHT//4
    #ball_2x = 30
    #ball_2y = 330
    ball_2dx = -vel
    ball_2dy = vel
    #ball_2x = random.randint(ball_radius, WINDOW_SIZE - ball_radius)
    #ball_2y = random.randint(ball_radius, WINDOW_SIZE - ball_radius)
    balls = [[ball_1x, ball_1y, ball_1dx, ball_1dy],[ball_2x, ball_2y, ball_2dx, ball_2dy]]
    #points_lists=[]

#initiate points lists
    #for ball in balls:
        #points_lists.append(create_points(ball[0], ball[1], ball_radius)) 
  
# Set up screen
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Grid Ball Game")
    clock = pygame.time.Clock()

    # Create grid (top half black, bottom half white)
    grid = [[BLACK if x < GRID_WIDTH // 2 else WHITE for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]


    # Main loop
    running = True
    while running:

        wall_bounce = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        for ball in balls:
            if ball == balls[0]:
                print("ball 1")
                print (f"ball x,y,dx,dy: {ball[0]},{ball[1]},{ball[2]},{ball[3]},")
            else: print ("ball 2")
            print(f" current x,y location: {ball[0]}, {ball[1]}")
            print(f"current grid x, y { ball[0] // CELL_SIZE}, { ball[1] // CELL_SIZE}")


            ball = update_ball_velocity(ball) #poisition update
            points_list=[]
            points_list=(create_points(ball[0], ball[1], ball_radius))  #point list update
            wc = wall_check(points_list, WINDOW_WIDTH, WINDOW_HEIGHT)
            if wc != None and wc[0] == 'x':
                loc=wc[1]
                #print(f"wall bounce on x: {points_list}")
                
                correction =bounce_check(ball, loc,'x', CELL_SIZE)
                ball[0]+=correction[0]
                ball[1]+=correction[1]
                ball[2] = -ball[2]
                points_list=(create_points(ball[0], ball[1], ball_radius))


                wall_bounce = True
            elif wc!= None and wc[0] == 'y':
                loc = wc[1]
                #print(f"wall bounce on y: {points_list}")
                
                correction =bounce_check(ball, loc,'y', CELL_SIZE)
                ball[0]+=correction[0]
                ball[1]+=correction[1]
                ball[3] = -ball[3]
                points_list=(create_points(ball[0], ball[1], ball_radius))
                #if ball[1]<ball_radius:
                    #ball[1]=ball_radius+1
                #elif ball[1] > WINDOW_HEIGHT:
                    #ball[1] = WINDOW_HEIGHT-ball_radius-1
                wall_bounce = True
            #else:
                wall_bounce = False

            #if wall_bounce == False:


                #check for collisions with color change on points_list
                #move ball starting coords by 0.5 to avoid corner collisions - else look for 1/4,3/4, 5/4, 7/4 collisions
                #print (f"ball in cell: {int(ball[0]//CELL_SIZE)},{int(ball[1]//CELL_SIZE)}")
                for loc in points_list:
                    a=int(loc[0]//CELL_SIZE)
                    b=int(loc[1]//CELL_SIZE) if int(loc[1]//CELL_SIZE)<= WINDOW_HEIGHT//CELL_SIZE-1 else WINDOW_HEIGHT//CELL_SIZE-1
                    x = int(ball[0]//CELL_SIZE)
                    y = int(ball[1]//CELL_SIZE)

                    #print (f"location 0: {loc[0]}")
                    #print (f"location 1: {loc[1]}")
                    
                    #a,b = edge  ----- x,y = ball center 
                    if grid[b][a] != grid[y][x]:
                        #print (f" colors not equal. ball edge = {grid[b][a]}, ball center = {grid[y][x]}")
                        #top or bottom collision
                        if ball[0] == loc[0]: 
                            ball[3]=-ball[3]
                            grid[b][a] = BLACK if grid[b][a] == WHITE else WHITE


                            correction =bounce_check(ball, loc,'y', CELL_SIZE)
                            print(f"{correction}")
                            ball[0]+=correction[0]
                            ball[1]+=correction[1]






                        #side collision
                        elif ball[1] == loc[1]:
                            ball[2]=-ball[2]
                            grid[b][a] = BLACK if grid[b][a] == WHITE else WHITE
                            print (f"calling bounce check w/ edge loc of {loc}")
                            print (f"ball radius: {ball_radius}")
                            print (f" ball center: {ball[0]},{ball[1]}")
                            correction =bounce_check(ball, loc,'x', CELL_SIZE)
                            print(f"{correction}")
                            ball[0]+=correction[0]+0.2
                            ball[1]+=correction[1]+0.2

                        #corner collision - try changing only x for all corner collisions
                            #angle_list = [0, (1/4),  (2/4),  (3/4), (4/4), (5/4), (6/4), (7/4)]
                        else: #directions CW q1, q2, q3, q4
                            ball[2]=-ball[2]
                            ball[3] = -ball[3]
                            grid[b][a] = BLACK if grid[b][a] == WHITE else WHITE
                            correction =bounce_check(ball, loc, 'xy', CELL_SIZE)
                            print(f"{correction}")
                            ball[0]+=correction[0]
                            ball[1]+=correction[1]

#angle_list = [0, math.pi*(1/4),  math.pi*(2/4),  math.pi*(3/4), math.pi*(4/4), math.pi*(5/4), math.pi*(6/4), math.pi*(7/4)]


        screen.fill(WHITE)  # Clears the screen before drawing
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = grid[y][x]
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            for x in range(GRID_WIDTH + 1):  # Vertical lines
                pygame.draw.line(screen, GRID_LINE_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, WINDOW_HEIGHT))
            for y in range(GRID_HEIGHT + 1):  # Horizontal lines
                pygame.draw.line(screen, GRID_LINE_COLOR, (0, y * CELL_SIZE), (WINDOW_WIDTH, y * CELL_SIZE))

        # Draw the ball
        for ball in balls:
            pygame.draw.circle(screen, (255, 0, 0), (ball[0], ball[1]), ball_radius)
            #pygame.draw.circle(screen, (255, 0, 0), (ball_2x, ball_2y), ball_radius)
        
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(120)
    pygame.mouse.set_visible(True)
    pygame.quit()


def bounce_check(ball, edge_loc, bounce:str, cell_size): 
    #doesn't work if correction in velocity occurs first
    if ball[2]>0 and ball[3]<0:
         direction = 1
    elif ball[2]>0 and ball[3]>0:
         direction = 2
    elif ball[2]<0 and ball[3]>0:
         direction = 3
    elif ball[2]<0 and ball[3]<0:
         direction = 4
    
    if bounce == 'y':
        if edge_loc[1]<ball[1]:
            edge_remainder = min(cell_size-(edge_loc[1] % cell_size), (edge_loc[1] % cell_size))
            return [0,edge_remainder+0.2]
        elif edge_loc[1]>ball[1]:
            edge_remainder = -1*min(cell_size-(edge_loc[1] % cell_size), (edge_loc[1] % cell_size))
            return [0,edge_remainder-0.2]

    elif bounce == 'x':
        if edge_loc[0] < ball[0]:
            edge_remainder = min(cell_size-(edge_loc[1] % cell_size), (edge_loc[1] % cell_size))
            return [edge_remainder+0.2,0]

        elif edge_loc[1]>ball[1]:
            edge_remainder = -1*min(cell_size-(edge_loc[1] % cell_size), (edge_loc[1] % cell_size))
            return [edge_remainder-0.2, 0]

    elif bounce == 'xy':
            return [0,0]

    else: return [0,0]

def direction(ball):
    print("direction called")
    x=ball[2]
    y=ball[3]
    if x>0 and y<0:
        return 'q1'
    elif x>0 and y>0:
        return 'q2'
    elif x<0 and y>0:
        return 'q3'
    else:
        return 'q4'

#vel cant equal more than half the cell size



def create_points(x, y, br):
    print(f"create points called")
    angle_list = [0, math.pi*(1/4),  math.pi*(2/4),  math.pi*(3/4), math.pi*(4/4), math.pi*(5/4), math.pi*(6/4), math.pi*(7/4)]
    point_list = []

    for i in angle_list:
        c = br*math.cos(i)
        s = br*math.sin(i)
        point_list.append([x+c, y+s])
    #print(f"{point_list}")
    return point_list

def update_ball_velocity(ball): #x,y,dx,dy
        print('update position called')
        ball[0]+=ball[2]
        ball[1]+=ball[3]
        return ball

def wall_check(point_list, ww, wh):
    print("wall check called")
    for loc in point_list:
        if loc[0]<=0 or loc[0] >= ww:
            return ['x',loc]
        elif loc[1]<=0 or loc[1]>= wh:
            return ['y',loc]
    return None


main()

 