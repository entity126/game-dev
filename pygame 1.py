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
        self.player0 = Rect(1100, 500, 50, 50)
        self.player1 = Rect(100, 200, 50, 50)
        
        
        self.player_speed = 300  # Speed in pixels per second
        self.projectiles = []  # List to store projectiles
        self.player1_direction = (1, 0)  # Default direction for player 1
        self.player0_direction = (1, 0)  # Default direction for player 0

        # HP attributes
        self.player1_hp = 10
        self.player0_hp = 10
        self.player1_score = 0
        self.player0_score = 0

    def reset_players(self):
        # Reset player positions and HP
        self.player0.x, self.player0.y = 1100, 500
        self.player1.x, self.player1.y = 100, 200
        self.player1_hp = 10
        self.player0_hp = 10
        self.projectiles.clear()
        self.player1_direction = (1, 0)
        self.player0_direction = (1, 0)

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
                    elif event.key == pygame.K_RSHIFT:  # Player 0 shoots
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
                # Check collision with player1 (blue), skip if projectile owner is player1
                if projectile.direction == self.player1_direction:
                    if self.player0.colliderect(projectile.rect):
                        self.player0_hp -= 1
                        self.projectiles.remove(projectile)
                        continue
                # Check collision with player0 (red), skip if projectile owner is player0
                elif projectile.direction == self.player0_direction:
                    if self.player1.colliderect(projectile.rect):
                        self.player1_hp -= 1
                        self.projectiles.remove(projectile)
                        continue
                # Remove projectile if it goes off-screen
                if projectile.rect.bottom < 0 or projectile.rect.top > self.res[1] or \
                   projectile.rect.right < 0 or projectile.rect.left > self.res[0]:
                    self.projectiles.remove(projectile)

            # Check for HP reaching 0 and update score/restart
            if self.player1_hp <= 0:
                self.player0_score += 1
                self.reset_players()
            elif self.player0_hp <= 0:
                self.player1_score += 1
                self.reset_players()

            # Drawing
            self.screen.fill(self.black)  
            pygame.draw.rect(self.screen, "blue", self.player1) 
            pygame.draw.rect(self.screen, "red", self.player0)
            
            # Draw HP and Score
            font = pygame.font.SysFont(None, 36)
            hp1 = font.render(f"Player 1 HP: {self.player1_hp}", True, self.white)
            hp0 = font.render(f"Player 0 HP: {self.player0_hp}", True, self.white)
            score1 = font.render(f"Score: {self.player1_score}", True, self.white)
            score0 = font.render(f"Score: {self.player0_score}", True, self.white)
            self.screen.blit(hp1, (20, 20))
            self.screen.blit(score1, (20, 60))
            self.screen.blit(hp0, (self.res[0] - 220, 20))
            self.screen.blit(score0, (self.res[0] - 220, 60))
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