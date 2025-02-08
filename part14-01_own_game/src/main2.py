# Complete your game here
import pygame

class DarkVLight:

    def __init__(self):
        pygame.init()

        

        self.load_images()
        self.new_game()

        self.height=len(self.map)
        self.width=len(self.map[0])
        self.scale = self.images[0].get_width()

        window_height=self.scale*self.height
        window_width=self.scale*self.width
        self.window = pygame.display.set_mode((window_width, window_height))
        
        pygame.display.set_caption("Dark V Light")

        self.ballxv=1
        self.ballyv=-1
        self.ballx=20
        self.bally=self.window.get_height()-20


        self.main_loop()


def load_images(self):
    self.images=[]
    for name in ["white","black","ballOnWhite","ballOnBlack","blocker"]:
        self.images.append(pygame.image.load(name+".png"))


def new_game(self):
    top = [[1]*20 for _ in range(20)]
    bottom=[[0]*20 for _ in range(20)]
    self.map=top+bottom



def check_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            self.blocker_move(event.pos[0]) #########send x of mouse to move blocker


def blocker_move(self, xcord):
    blocker = self.images[4]
    self.window.blit(blocker,(xcord - blocker.get_width//2,self.window.get_height()-blocker.get_height()))
        

def draw_window(self):
    self.window.fill((0,0,0))

    for y in range(self.height):
        for x in range(self.width):
            square = self.map[y][x]
            self.window.blit(self.images[square],(x*self.scale,y*self.scale))


def find_ball(self):


def main_loop(self):
    while True:
        self.check_events()
        self.check_collision()
        self.draw_window()