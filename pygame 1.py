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
        
        # instances
        self.player0 = Rect(100, 500, 50, 50)
        self.player1 = Rect(100, 500, 50, 50)
        
        
        self.player_speed = 300  # Speed in pixels per second
        self.projectiles = []  # List to store projectiles
        self.player1_direction = (1, 0)  # Default direction for player 1
        self.player0_direction = (1, 0)  # Default direction for player 0

    def gameloop(self):
        while self.run:
            dt = self.clock.tick(self.fps) / 1000  # Delta time in seconds

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Player 1 shoots
                        self.projectiles.append(Projectile(
                            self.player1.x + self.player1.width // 2,
                            self.player1.y + self.player1.height // 2,
                            speed=500,
                            direction=self.player1_direction,  # Use last movement direction
                            color="yellow",
                            size=10
                        ))
                    elif event.key == pygame.K_LSHIFT:  # Player 0 shoots
                        self.projectiles.append(Projectile(
                            self.player0.x + self.player0.width // 2,
                            self.player0.y + self.player0.height // 2,
                            speed=500,
                            direction=self.player0_direction,  # Use last movement direction
                            color="yellow",
                            size=10
                        ))

            # Player 1 movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player1.x -= self.player_speed * dt
                self.player1_direction = (-1, 0)  # Moving left
            if keys[pygame.K_d]:
                self.player1.x += self.player_speed * dt
                self.player1_direction = (1, 0)  # Moving right
            if keys[pygame.K_w]:
                self.player1.y -= self.player_speed * dt
                self.player1_direction = (0, -1)  # Moving up
            if keys[pygame.K_s]:
                self.player1.y += self.player_speed * dt
                self.player1_direction = (0, 1)  # Moving down

            # Player 2 movement
            if keys[pygame.K_LEFT]:
                self.player0.x -= self.player_speed * dt
                self.player0_direction = (-1, 0)  # Moving left
            if keys[pygame.K_RIGHT]:
                self.player0.x += self.player_speed * dt
                self.player0_direction = (1, 0)  # Moving right
            if keys[pygame.K_UP]:
                self.player0.y -= self.player_speed * dt
                self.player0_direction = (0, -1)  # Moving up
            if keys[pygame.K_DOWN]:
                self.player0.y += self.player_speed * dt
                self.player0_direction = (0, 1)  # Moving down

            # Boundaries for players
            self.player1.x = max(0, min(self.res[0] - self.player1.width, self.player1.x))
            self.player1.y = max(0, min(self.res[1] - self.player1.height, self.player1.y))
            self.player0.x = max(0, min(self.res[0] - self.player0.width, self.player0.x))
            self.player0.y = max(0, min(self.res[1] - self.player0.height, self.player0.y))

            # Update projectiles
            for projectile in self.projectiles[:]:
                projectile.move(dt)
                # Remove projectile if it goes off-screen
                if projectile.rect.bottom < 0 or projectile.rect.top > self.res[1] or \
                   projectile.rect.right < 0 or projectile.rect.left > self.res[0]:
                    self.projectiles.remove(projectile)

            # Drawing
            self.screen.fill(self.black)  
            pygame.draw.rect(self.screen, "blue", self.player1) 
            pygame.draw.rect(self.screen, "red", self.player0)
            for projectile in self.projectiles:
                projectile.draw(self.screen)
            pygame.display.flip() 


class Projectile:
    def __init__(self, x, y, speed, direction, color, size):
        self.rect = pygame.Rect(x - size // 2, y - size // 2, size, size)
        self.speed = speed
        self.color = color
        self.direction = direction  # Use the direction passed during initialization

    def move(self, dt):
        # Move the projectile based on its direction
        self.rect.x += self.direction[0] * self.speed * dt
        self.rect.y += self.direction[1] * self.speed * dt

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


# Create an instance of the Game class
game_instance = Game(RESOLUTION, FPS)
game_instance.gameloop()

pygame.quit()
sys.exit()