import pygame, random

class Zombies:

    def __init__(self, game, type, lane, ui):
        self.game = game
        self.ui = ui
        self.type = type
        self.lane = lane
        #self.pos = [1980,(lane*113) + 275]

        self.img = pygame.transform.scale(game.assets["zombies"][type], (80,125))
        self.rect = self.img.get_rect()
        self.rect.x = 1920
        self.rect.y = lane*113 + 300
        self.speed = 0.6
        self.moving = True

        self.health = 250

    #def rect(self):
        #return pygame.Rect(self.rect.x+5, self.rect.y+16, 6, 16)

    def update(self):
        self.moving = True
        #for plant in self.ui.grid[self.lane]:
        for plant in self.ui.plants:
            #if plant != 0:
                #print(self.rect, plant.rect)
                if self.rect.colliderect(plant.rect):
                    self.moving = False
                    plant.damage()
        if self.moving:
            self.rect.x -= self.speed
        
    def kill(self):
        self.ui.zombies[self.lane].remove(self)

    def draw(self, display):
        display.blit(self.img, (int(self.rect.x), int(self.rect.y)))

