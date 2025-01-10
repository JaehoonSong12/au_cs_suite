import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Domino's Time!")

# Set up fonts and colors
FONT = pygame.font.Font(None, 36)
COLOR_BG = (255, 255, 255)  # White
COLOR_TEXT = (0, 0, 0)      # Black
COLOR_BOX = (200, 200, 200) # Light grey

# Input box positions and dimensions
boxes = {
    "Pizza": pygame.Rect(150, 50, 200, 40),
    "Pasta": pygame.Rect(150, 110, 200, 40),
    "Chicken Wings": pygame.Rect(150, 170, 200, 40),
}

# Prices
PRICES = {"Pizza": 12, "Pasta": 6, "Chicken Wings": 8}


def calculate_total(inputs):
    try:
        pizza_price = int(inputs["Pizza"] or 0) * PRICES["Pizza"]
        pasta_price = int(inputs["Pasta"] or 0) * PRICES["Pasta"]
        chicken_price = int(inputs["Chicken Wings"] or 0) * PRICES["Chicken Wings"]
        return pizza_price + pasta_price + chicken_price
    except ValueError:
        return 0

def run():
    # Variables
    active_box = None
    inputs = {"Pizza": "", "Pasta": "", "Chicken Wings": ""}
    total_price = 0
    running = True
    while running:
        screen.fill(COLOR_BG)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked a box
                for key, box in boxes.items():
                    if box.collidepoint(event.pos):
                        active_box = key
                        break
                else:
                    active_box = None
            elif event.type == pygame.KEYDOWN:
                if active_box:
                    if event.key == pygame.K_RETURN:
                        total_price = calculate_total(inputs)
                    elif event.key == pygame.K_BACKSPACE:
                        inputs[active_box] = inputs[active_box][:-1]
                    else:
                        inputs[active_box] += event.unicode

        # Draw input boxes and text
        for key, box in boxes.items():
            color = COLOR_BOX if key != active_box else (255, 200, 200)
            pygame.draw.rect(screen, color, box)
            text_surface = FONT.render(inputs[key], True, COLOR_TEXT)
            screen.blit(text_surface, (box.x + 10, box.y + 5))

        # Draw labels
        labels = ["Pizza", "Pasta", "Chicken Wings"]
        for i, label in enumerate(labels):
            label_surface = FONT.render(label, True, COLOR_TEXT)
            screen.blit(label_surface, (50, 60 * i + 50))

        # Draw total price
        total_text = FONT.render(f"Total: ${total_price}", True, COLOR_TEXT)
        screen.blit(total_text, (50, 250))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    run()