import pygame
import random
import math

# Initialize Pygame

def main():
    pygame.init()

#GRID
    GRID_WIDTH = 20
    GRID_HEIGHT = 26
    CELL_SIZE = 30
    WINDOW_WIDTH = (GRID_WIDTH * CELL_SIZE) #750 width
    WINDOW_HEIGHT = (GRID_HEIGHT * CELL_SIZE) #900 height
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRID_LINE_COLOR = (100, 100, 100)
#BALL
    vel = 1
    ball_radius = 10
    ball_1x = WINDOW_WIDTH//2 + WINDOW_WIDTH//8
    #ball_1y = WINDOW_HEIGHT//2 - WINDOW_HEIGHT//4 +0.5
    #ball_1x=190
    ball_1y=330
    #ball_1x = 180 +2*ball_radius+12
    #ball_1y = WINDOW_HEIGHT//2 + WINDOW_HEIGHT//3
    #ball_1dx = -1
    #ball_1dy = -1
    ball_1dx = -vel+0.2
    ball_1dy = -vel+0.2
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for ball in balls:
            #if ball == balls[0]:
                #print("ball 1")
                #print (f"ball x,y,dx,dy: {ball[0]},{ball[1]},{ball[2]},{ball[3]},")
            #else: #print ("ball 2")
            #print(f" current x,y location: {ball[0]}, {ball[1]}")
            #print(f"current grid x, y { ball[0] // CELL_SIZE}, { ball[1] // CELL_SIZE}")

            ball = update_ball_location(ball) #poisition update
            points_list=[]

            #   [T,TR,R,BR,B,BL,L,TL]
            points_list=(create_points(ball[0], ball[1], ball_radius))  #all points
            dir = give_direction(ball)
            #print(f"{dir}")
            check_list = give_check_list(points_list, dir) # 3 points based on direction
            #print(f"check list{check_list}")

            bounces = check_for_bounce(check_list, ball, WINDOW_HEIGHT, WINDOW_WIDTH, grid, CELL_SIZE) #x, xy, or y bounce
            #print (f"{bounces}")
            #if ball[1] == 150:
                 #print ("stop")

            if 1 in bounces:
                #change color
                #change velocity
                #[xb, xyb, yb]

                vel_delta = velocity_calc(bounces) #converts bounce [3] into 2 length velocity vector
                color_change_locs = color_changes(check_list, bounces) 
                #sends 3 points to check if bounce was based on wb or color change
                #can return >1 color change cells
                ball[2]*=vel_delta[0]
                ball[3]*=vel_delta[1]

                for loc in color_change_locs:
                    a = int(loc[0]//CELL_SIZE)
                    b = int(loc[1]//CELL_SIZE)
                    #print (f"b:{b}")
                    if a >=0 and a<WINDOW_WIDTH//CELL_SIZE:
                         if b >=0 and b < WINDOW_HEIGHT/CELL_SIZE:
                            grid[b][a] = BLACK if grid[b][a] == WHITE else WHITE    


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

def color_changes(CL, bounces):
    rlist = []
    for i in range(len(bounces)):
          if bounces[i]==1:
               rlist.append(CL[i])
    return rlist
               

def velocity_calc(bounces):
    if bounces [1] == 1:
            return [-1,-1]
    elif bounces[0] ==1 and bounces[2] == 1:
            return [-1,-1]
    elif bounces[0] == 1:
            return [-1,1]
    elif bounces[2]==1:
            return [1,-1]

def check_for_bounce(CL, ball, WH, WW, grid, cell_size):
    # x, xy, y
    x = (CL[0])
    xy = (CL[1])
    y = (CL[2])
    xb=0
    xyb=0
    yb=0




    if x[0] < 0 or x[0] >= WW: # x cord oob
            xb = 1
    if x[1] < 0  or x[1] >= WH: #y coord oob
            yb=1


    if xy[0] < 0 or xy[0] >= WW: # x cord oob
            xb = 1
    if xy[1] < 0  or xy[1] >= WH: #y coord oob
            yb=1


    if y[0] < 0 or y[0] >= WW: # x cord oob
            xb = 1
    if y[1] < 0  or y[1] >= WH: #y coord oob
            yb=1   

    #only check colors if no wall bounce found
    ball_center_color = grid[int(ball[1]//cell_size)][int(ball[0]//cell_size)]
    if xb==0:
        x_color = grid[int(x[1]//cell_size)][int(x[0]//cell_size)]
        if x_color != ball_center_color:
            xb=1
    if xyb ==0:
        xy_color = grid[int(xy[1]//cell_size)][int(xy[0]//cell_size)]
        if xy_color != ball_center_color:
            xyb=1
    if yb == 0:
        y_color =grid[int(y[1]//cell_size)][int(y[0]//cell_size)]  
        if y_color != ball_center_color:
            yb=1

    #print(f" ball center {ball_center_color}, xcolor {x_color}, xycolor {xy_color}, ycolor {y_color}")
    
    return [xb,xyb,yb]

def give_check_list(pl, dir):
    if dir ==1:
        return [pl[0],pl[7],pl[6]]
    elif dir==2:
        return pl[0:3]
    elif dir ==3:
        return [pl[4],pl[3],pl[2]]
    elif dir==4:
        return pl[4:7]
                

            
def give_direction(ball):
    if ball[2]>0 and ball[3]<0:
         direction = 1
    elif ball[2]>0 and ball[3]>0:
         direction = 2
    elif ball[2]<0 and ball[3]>0:
         direction = 3
    elif ball[2]<0 and ball[3]<0:
         direction = 4
    return direction



def bounce_check(ball, edge_loc, bounce:str, cell_size, direction): 
    #doesn't work if correction in velocity occurs first
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
    #print("direction called")
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
    #print(f"create points called")
    angle_list = [0, math.pi*(1/4),  math.pi*(2/4),  math.pi*(3/4), math.pi*(4/4), math.pi*(5/4), math.pi*(6/4), math.pi*(7/4)]
    point_list = []

    for i in angle_list:
        c = br*math.cos(i)
        s = br*math.sin(i)
        point_list.append([x+c, y+s])
    #print(f"{point_list}")
    return point_list

def update_ball_location(ball): #x,y,dx,dy
        #print('update position called')
        ball[0]+=ball[2]
        ball[1]+=ball[3]
        return ball

def wall_check(point_list, ww, wh):
    #print("wall check called")
    for loc in point_list:
        if loc[0]<=0 or loc[0] >= ww:
            return ['x',loc]
        elif loc[1]<=0 or loc[1]>= wh:
            return ['y',loc]
    return None


main()

 