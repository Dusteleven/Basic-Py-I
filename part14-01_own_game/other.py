import pygame
import random

# Initialize Pygame

def main():
    pygame.init()


    # Constants
    GRID_SIZE = 30
    CELL_SIZE = 30
    WINDOW_SIZE = GRID_SIZE * CELL_SIZE
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    ball_radius = 5
    ball_x = 180
    ball_y = 890
    #ball_x = random.randint(ball_radius, WINDOW_SIZE - ball_radius)
    #ball_y = random.randint(ball_radius, WINDOW_SIZE - ball_radius)
    ball_dx = 1
    ball_dy = -1
    paddle = pygame.image.load("paddle.png")
    paddle_x = -10
    paddle_y = -10
    paddle_width = paddle.get_width()
    paddle_height = paddle.get_height()

    # Set up screen
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Grid Ball Game")
    clock = pygame.time.Clock()

    # Create grid (top half black, bottom half white)
    grid = [[BLACK if y < GRID_SIZE -2 else WHITE for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]



    # Main loop
    running = True
    while running:

        
        wall_bounce = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                paddle_x=event.pos[0]
                paddle_y=event.pos[1]
                paddle_x_range=range(paddle_x,(paddle_x+paddle_width))
                paddle_y_range=range(paddle_y,(paddle_y+paddle_height))

                if check_paddle_collision(ball_x, ball_y, paddle_x, paddle_y, paddle_x_range, paddle_y_range, ball_dx, ball_dy):
                    ball_dy = -ball_dy





        # Update ball position
        ball_x += ball_dx
        ball_y += ball_dy
        
        edges = ball_edges(ball_x, ball_y, ball_radius)  #(L,R,T,B)
        L_edge=edges[0]
        R_edge=edges[1]
        T_edge=edges[2]
        B_edge=edges[3]

                                                                #wall bounces
        if L_edge[0] <= 0 or R_edge[0] >= WINDOW_SIZE:
            ball_dx = -ball_dx
            wall_bounce = True
        elif T_edge[1] <= 0 or  B_edge[1]>= WINDOW_SIZE:
            ball_dy = -ball_dy
            wall_bounce = True


        if wall_bounce == False:

            grid_row = ball_y // CELL_SIZE   #INT
            grid_col = ball_x // CELL_SIZE
                                                                #color of all surrounding cells
            
            surrounding_cell_colors = surrounding_colors(grid_row, grid_col, grid, GRID_SIZE)
            L_cell_color= surrounding_cell_colors[0]
            R_cell_color= surrounding_cell_colors[1]
            B_cell_color= surrounding_cell_colors[2]
            T_cell_color= surrounding_cell_colors[3]

            #if ball_y > 0:
                #T_cell_loc = ([grid_row-1],[grid_col])
            #if ball_x < WINDOW_SIZE:
                #R_cell_loc = ([grid_row],[grid_col+1])
            #if ball_y < WINDOW_SIZE:
                #B_cell_loc = ([grid_row+1],[grid_col])
            #if ball_x > 0:
                #L_cell_loc = ([grid_row],[grid_col-1])

            curr_color = grid[grid_row][grid_col] 

            #T_cell = grid[row-1][col]

            #print(f"current ball grid loc: {grid_row} {grid_col}")    
            #print(f"top cell grid loc: {grid_row-1} {grid_col} ")       
            #print(f" current x location: {ball_x}")
            #print(f" current y location: {ball_y}")
            #print(f"COLORS: ---current:{curr_color}top:{T_cell_color}right:{R_cell_color}bottom:{B_cell_color}left:{L_cell_color}")
            #print("remainder from edge")
            #print(f"left {(ball_x-ball_radius) % CELL_SIZE}")
            #print(f"right {(ball_x+ball_radius) % CELL_SIZE}")
            #print(f"top {(ball_y - ball_radius) % CELL_SIZE}")
           # print(f"bottom {(ball_y + ball_radius) % CELL_SIZE}")
            #print(f" next top {T_cell_color} and current color {curr_color}")
            #edges = ball_edges(ball_x, ball_y, ball_radius)  #(L,R,T,B)

                                                                                #cell collisions
            if ball_dx <0 and (L_edge[0]) % CELL_SIZE == 0 and L_cell_color != curr_color: #LEFT         
                ball_dx = -ball_dx
                grid[grid_row][grid_col-1] = BLACK if L_cell_color == WHITE else WHITE  

            if  ball_dx>0 and (R_edge[0]) % CELL_SIZE == 0 and R_cell_color != curr_color: #RIGHT
                ball_dx = -ball_dx
                grid[grid_row][grid_col+1] = BLACK if R_cell_color == WHITE else WHITE

            if  ball_dy <0 and (T_edge[1]) % CELL_SIZE == 0 and T_cell_color != curr_color: #TOP
                ball_dy = -ball_dy
                grid[grid_row-1][grid_col] = BLACK if T_cell_color == WHITE else WHITE

            if ball_dy >0 and (B_edge[1]) % CELL_SIZE == 0 and B_cell_color != curr_color: #BOTTOM
                ball_dy = -ball_dy
                grid[grid_row+1][grid_col] = BLACK if B_cell_color == WHITE else WHITE
                #print("Collision detected! Ball will bounce and color will change.")


    # Draw everything
        screen.fill((0, 0, 0))
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                
                pygame.draw.rect(screen, grid[row][col], rect)

        # Draw the ball
        pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
        screen.blit(paddle, (paddle_x, paddle_y))
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(120)
    pygame.mouse.set_visible(True)
    pygame.quit()


#print(f" current x location: {ball_x}")
        #print(f" current y location: {ball_y}")
        #print(f"COLORS: ---current:{curr_color}top:{next_top}right:{next_right}bottom:{next_bottom}left:{next_left}")
        #print("remainder from edge")
        #print(f"left {(ball_x-ball_radius) % CELL_SIZE}")
        #print(f"right {(ball_x+ball_radius) % CELL_SIZE}")
        #print(f"top {(ball_y + ball_radius) % CELL_SIZE}")
        #print(f"bottom {(ball_y - ball_radius) % CELL_SIZE}")
        #print(f" next left {next_left} and current color {curr_color}")
        #edges = ball_edges(ball_x, ball_y, ball_radius)  #(L,R,T,B)

def check_paddle_collision(bx, by, px, py, pxr, pyr, dx, dy):

        #if ball above the paddle and +dy = TRUE
        if by <= py and dy >0:
            if bx in pxr:
                if by in pyr:
                    print(f"ball x,y: {bx}, {by}")
                    print(f"paddle x range: {pxr}")
                    print(f"paddle y range: {pyr}")
                    return True
        elif by>= py and dy<0:
            if bx in pxr:
                if by in pyr:
                    print(f"ball x,y: {bx}, {by}")
                    print(f"paddle x range: {pxr}")
                    print(f"paddle y range: {pyr}")
                    return True

        
        
        return False

def ball_edges(x, y, r):
    left_edge_x = (x - r, y) 
    right_edge_x = (x + r, y)
    top_edge_y = (x, y - r) 
    bottom_edge_y = (x, y + r) 
    return [left_edge_x, right_edge_x, top_edge_y, bottom_edge_y]
        
def surrounding_colors(row, col, grid, GRID_SIZE):
    if col >0:
        L_cell = grid[row][col-1]
    else: L_cell = grid[row][col]

    if col < GRID_SIZE-1:
        R_cell = grid[row][col+1]
    else: R_cell = grid[row][col]

    if row < GRID_SIZE -1:
        B_cell = grid[row+1][col]
    else: B_cell = grid[row][col]

    if row >0:
        T_cell = grid[row-1][col]
    else: T_cell = grid[row][col]

    return [L_cell, R_cell, B_cell, T_cell]

main()