# 
# from plants import *
import pygame, os, sys, time
from random import randint

def find_resource(file_name):
    path = os.path.join(os.path.abspath(__file__ + "/.."), file_name)
    return path

FPS = 90
WINDOW_WIDTH = 1950
WINDOW_HEIGHT = 1080
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, file_name, x, y, speed, size = None):
        super().__init__()#kopijuje vse schoje v super classu => pygame.sprite.Sprite
        self.image = self.load_image(file_name, size)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.speed = speed

    def load_image(self, file_name, size = None):
        # print("abspath:",os.path.abspath(__file__))
        img_path = os.path.join(os.path.abspath(__file__ + "/.."), file_name)
        image = pygame.image.load(img_path).convert_alpha()
        #vlastni rozmiry, netreba zadavaty
        if not size:
            size = image.get_rect()#original size
            scaled_image = pygame.transform.scale(image, size)
        else:
            scaled_image = pygame.transform.scale(image, size)#mashtabujem
        return scaled_image

    #maluvanya objektu
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Interface_seeds(pygame.sprite.Sprite):
    def __init__(self, img, x, y, plant_num, size = None):
        self.img = pygame.transform.scale(img, size)
        self.rect = self.img.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.plant_num = plant_num
    
    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))


class Sun(GameSprite):
    def update(self):
        # global passed
        self.rect.y += self.speed
        if self.rect.y <= WINDOW_HEIGHT:
            del self
    
    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

suns = pygame.sprite.Group()

# for i in range(2):
#     # suns.add(Sun("/Users/Maria/OneDrive2/OneDrive/Desktop/Projekty/zavdanya pray for python/Final/PvZ like game/data(veci)/images/sun.png", randint(0, WINDOW_WIDTH - 100), -65, randint(1,5), (100, 65)))
#     suns.add(Sun("./images/sun.png", randint(0, WINDOW_WIDTH - 100), -65, randint(1,5), (100, 65)))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()

#     window.fill((0,0,0))
#     monsters.draw(window)
#     monsters.update()


#     pygame.display.update()
#     clock.tick(FPS)


# finish = False
# if not finish:
#     pygame.display.update()
#     clock.tick(FPS)








