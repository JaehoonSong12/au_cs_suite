import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elemental Clash Lite")
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)

# Player class
class Player:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = color
        self.health = 100
        self.velocity = 5
        self.jump_power = 10
        self.is_jumping = False
        self.jump_speed = 0
        self.controls = controls  # Dictionary for controls
        self.on_ground = True

    def move(self, keys):
        # Movement
        if keys[self.controls['left']]:
            self.rect.x -= self.velocity
        if keys[self.controls['right']]:
            self.rect.x += self.velocity
        
        # Jump
        if keys[self.controls['jump']] and self.on_ground:
            self.is_jumping = True
            self.jump_speed = -self.jump_power

        # Apply gravity
        if self.is_jumping:
            self.rect.y += self.jump_speed
            self.jump_speed += 1  # Gravity effect
            if self.rect.y >= SCREEN_HEIGHT - 100:  # Ground collision
                self.rect.y = SCREEN_HEIGHT - 100
                self.is_jumping = False
                self.on_ground = True
        else:
            self.on_ground = True

    def attack(self, keys, projectiles):
        if keys[self.controls['attack']]:
            projectiles.append(Projectile(self.rect.centerx, self.rect.y, self.color))

    def special_move(self, keys, projectiles):
        if keys[self.controls['special1']]:
            projectiles.append(Projectile(self.rect.centerx, self.rect.y, self.color, size=20, speed=10))
        if keys[self.controls['special2']]:
            projectiles.append(Projectile(self.rect.centerx, self.rect.y, self.color, size=30, speed=5))

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y - 10, self.health, 5))

# Projectile class
class Projectile:
    def __init__(self, x, y, color, size=10, speed=7):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.speed = speed

    def move(self):
        self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)



def main_logic():
    # Initialize players and projectiles
    player1 = Player(100, SCREEN_HEIGHT - 100, BLUE, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'jump': pygame.K_UP, 'attack': pygame.K_SPACE, 'special1': pygame.K_s, 'special2': pygame.K_d})
    player2 = Player(600, SCREEN_HEIGHT - 100, RED, {'left': pygame.K_a, 'right': pygame.K_d, 'jump': pygame.K_w, 'attack': pygame.K_f, 'special1': pygame.K_g, 'special2': pygame.K_h})

    projectiles = []

    # Main game loop
    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Player actions
        player1.move(keys)
        player2.move(keys)
        player1.attack(keys, projectiles)
        player2.attack(keys, projectiles)
        player1.special_move(keys, projectiles)
        player2.special_move(keys, projectiles)

        # Update projectiles
        for projectile in projectiles[:]:
            projectile.move()
            if projectile.rect.x > SCREEN_WIDTH or projectile.rect.x < 0:
                projectiles.remove(projectile)

        # Collision detection
        for projectile in projectiles[:]:
            if projectile.rect.colliderect(player1.rect) and projectile.color != player1.color:
                player1.health -= 10
                projectiles.remove(projectile)
            elif projectile.rect.colliderect(player2.rect) and projectile.color != player2.color:
                player2.health -= 10
                projectiles.remove(projectile)

        # Draw everything
        player1.draw()
        player2.draw()
        for projectile in projectiles:
            projectile.draw()

        # Check for win condition
        if player1.health <= 0 or player2.health <= 0:
            winner = "Player 1" if player2.health <= 0 else "Player 2"
            text = font.render(f"{winner} Wins!", True, BLACK)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()