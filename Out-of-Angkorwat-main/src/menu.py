import pygame

class Menu:
    def __init__(self, screen, font_path=None):
        self.screen = screen
        self.font = pygame.font.Font(font_path, 36) if font_path else pygame.font.SysFont("Arial", 36)
        self.options = ["Start Game", "Quit"]
        self.selected = 0
        self.running = True
        self.option_rects = []

    def create_option_rects(self):
        self.option_rects = []
        for i, option in enumerate(self.options):
            center_pos = (self.screen.get_width() // 2, 300 + i * 50)
            text_surface = self.font.render(option, True, (0,0,0))
            rect = text_surface.get_rect(center=center_pos)
            self.option_rects.append(rect)

    def draw(self):
        self.screen.fill((10, 10, 10))
        mouse_pos = pygame.mouse.get_pos()

        for i, option in enumerate(self.options):
            rect_center = self.option_rects[i].center
            is_hover = self.option_rects[i].collidepoint(mouse_pos)
            if is_hover:
                color = (255, 255, 100)
            elif i == self.selected:
                color = (255, 255, 0)
            else:
                color = (200, 200, 200)

            text_surface = self.font.render(option, True, color)
            text_rect = text_surface.get_rect(center=rect_center)
            self.screen.blit(text_surface, text_rect)

        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return "Quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    return self.options[self.selected].lower().replace(" ", "_")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, rect in enumerate(self.option_rects):
                        if rect.collidepoint(mouse_pos):
                            self.selected = i
                            return self.options[i].lower().replace(" ", "_")
        return None

    def run(self):
        self.create_option_rects()
        while self.running:
            aksi = self.handle_input()
            if aksi == "start_game":
                return "start"
            elif aksi == "quit":
                return "quit"
            self.draw()

