import pygame
import sys

pygame.init()
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keypress Detection")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

key_history = []

running = True


def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

print("Press the keys for the output. Press ESC to quit.")

while running:
    screen.fill(BLACK)
    display_text("Press the key to see which key is pressed. Press ESC to exit.", small_font, WHITE, 10, 10)
    display_text("Key History (last 5):", small_font, WHITE, 10, 60)


    for i, key in enumerate(key_history[-5:]):
        display_text(f"{i+1}: {key}", small_font, RED, 10, 100 + i * 40)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            key_history.append(key_name)

            if event.key == pygame.K_ESCAPE:
                running = False

    
    if key_history:
        display_text(f"Last Key Pressed: {key_history[-1]}", font, WHITE, screen_width // 2 - 250, screen_height // 2 - 40)


    pygame.display.flip()


pygame.quit()
sys.exit()
