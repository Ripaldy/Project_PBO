import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Menu with OOP - Pygame")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (40, 40, 40)
GRAY = (100, 100, 100)
BLUE = (70, 130, 180)
LIGHT_BLUE = (100, 160, 210)

# Fonts
FONT = pygame.font.SysFont("arial", 36)
FONT_SMALL = pygame.font.SysFont("arial", 24)

class Button:
    def __init__(self, text, x, y, width, height, 
                 idle_color, hover_color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.idle_color = idle_color
        self.hover_color = hover_color
        self.action = action
        self.hovered = False
        self.text_surf = FONT.render(text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, surface):
        color = self.hover_color if self.hovered else self.idle_color
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        surface.blit(self.text_surf, self.text_rect)

    def update(self, mouse_pos, mouse_click):
        if self.rect.collidepoint(mouse_pos):
            self.hovered = True
            if mouse_click[0]:  # Left mouse button clicked
                if self.action:
                    self.action()
        else:
            self.hovered = False

class Menu:
    def __init__(self):
        self.buttons = []
        self.running = True

    def start_game(self):
        print("Start Game clicked!")
        # Here you could add game start logic or switch game states

    def options(self):
        print("Options clicked! (You can add your settings here)")

    def quit_game(self):
        print("Quit Game clicked!")
        pygame.quit()
        sys.exit()

    def setup(self):
        btn_w = 200
        btn_h = 50
        btn_x = (SCREEN_WIDTH - btn_w) // 2
        btn_y = 150
        btn_gap = 70

        self.buttons.append(Button("Start Game", btn_x, btn_y, btn_w, btn_h,
                                   BLUE, LIGHT_BLUE, self.start_game))
        self.buttons.append(Button("Options", btn_x, btn_y + btn_gap, btn_w, btn_h,
                                   BLUE, LIGHT_BLUE, self.options))
        self.buttons.append(Button("Quit", btn_x, btn_y + 2*btn_gap, btn_w, btn_h,
                                   BLUE, LIGHT_BLUE, self.quit_game))

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            SCREEN.fill(DARK_GRAY)

            # Draw title
            title_surf = FONT.render("Main Menu", True, WHITE)
            title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, 80))
            SCREEN.blit(title_surf, title_rect)

            # Update and draw buttons
            for button in self.buttons:
                button.update(mouse_pos, mouse_click)
                button.draw(SCREEN)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    menu = Menu()
    menu.setup()
    menu.run()

