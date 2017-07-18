import pygame

class button():

    buttons = ['exit', 'play']

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.render( x, y, self.buttons[type])

    def render(self, x, y, text):
        surface = pygame.display.get_surface()
        font = pygame.font.Font("res/ubuntu.ttf", 30)
        text = font.render(text, 1, (0,0,0))
        textrect = text.get_rect()
        self.width = textrect.width
        self.height = textrect.height
        surface.blit(text, (x, y))

    def collision(self, x, y):
        if x >= self.x and x <= self.x + self.width:
            if y >= self.y and y <= self.y + self.height:
                return True
        return False