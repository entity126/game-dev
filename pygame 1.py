import pygame
from pygame.locals import*
import sys

pygame.init()

FPS = 60
RESOLUTION = (1200, 700)


class Game:
    def __init__(self, res, fps):
        
        self.res = res
        self.fps = fps
        self.run = True
        self.screen = pygame.display.set_mode(self.res)
        self.clock = pygame.time.Clock()
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        
        # instances0
        self.player0 = Rect(100, 500, 50, 50)
        self.player1 = Rect(100, 500, 50, 50)
        
        
        self.player_speed = 300  # Speed in pixels per second

    def gameloop(self):
        while self.run:
            dt = self.clock.tick(self.fps) / 1000  # Delta time in seconds

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            # Player 1 movement
            keys = pygame.key.get_pressed()
       
            if keys[pygame.K_a]:
                self.player1.x -= self.player_speed * dt
            if keys[pygame.K_d]:
                self.player1.x += self.player_speed * dt
            if keys[pygame.K_s]:
                self.player1.y += self.player_speed * dt

            if keys[pygame.K_w]:
                self.player1.y -= self.player_speed * dt

             # Player 2 movement
            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_LEFT]:
                self.player0.x -= self.player_speed * dt
            
            if keys[pygame.K_RIGHT]:
                self.player0.x += self.player_speed * dt

            if keys[pygame.K_DOWN]:
                self.player0.y += self.player_speed * dt
            
            if keys[pygame.K_UP]:
                self.player0.y -= self.player_speed * dt


            # Drawing
            self.screen.fill(self.black)  
            pygame.draw.rect(self.screen, "blue", self.player1) 
            pygame.draw.rect(self.screen, "red", self.player0)
            pygame.display.flip()  # Update the display


# Create an instance of the Game class
game_instance = Game(RESOLUTION, FPS)
game_instance.gameloop()

pygame.quit()
sys.exit()