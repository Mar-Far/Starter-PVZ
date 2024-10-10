import pygame, random
from utils import Sun
from zombies import Zombies

class Plant():
    def __init__(self, game, pos, max_health, ui):
        self.game = game # 
        #self.type = type # спрайт
        self.ui = ui
        #self.pos = pos
        self.max_health = max_health
        self.health = max_health

    def draw(self, display, draw_pos):
        display.blit(self.img, draw_pos)

    def damage(self):
        #random.choice(self.game.assets["sfx"]["chomp"]).play()
        self.health -= 0.5
        if self.health <= 0:
            self.kill()
    
    #def kill(self):
        #self.ui.plants.remove(self)
        #column = (self.rect.x - 470) // 113
        #row = (self.rect.y - 370) // 113
        #self.ui.grid[row][column] = 0

    def kill(self):
        if self in self.ui.plants:
            self.ui.plants.remove(self)
        column = (self.rect.x - 470) // 113
        row = (self.rect.y - 370) // 113
        if row >= 0 and column >= 0:
            self.ui.grid[row][column] = 0########HOLOVNEEEEEEE ZMINITY DOPOMOHOJU CHATGPT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Peashooter(Plant):
    def __init__(self, game, pos, max_health, ui):
        super().__init__(game, pos, max_health, ui)
        self.cost = 100
        #self.game = game
        #self.pos = pos
        #self.health = 15
        self.ui = ui
        self.img = pygame.transform.scale(game.assets["plants"]["peashooter"], (75, 150))
        self.rect = self.img.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.peas = []
        self.shoot_timer = pygame.time.get_ticks()  
        self.shoot_interval = 2500 

    def fire(self):
        new_pea = Pea(self.game, self.rect.x + 50, self.rect.y + 20, 10, self.ui) 
        self.ui.peas.append(new_pea)
        #print("peas", len(self.peas))
        #random.choice(self.game.assets["sfx"]["throw"]).play()

    def update(self, current_time):#draw_pos
        if current_time - self.shoot_timer > self.shoot_interval:
            self.fire()
            self.shoot_timer = current_time

        for pea in self.peas:
            pea.update()
            #pea.draw(display)
            #if pea.rect.x > 1980:
                #self.ui.peas.remove(pea)
            #self.peas.remove(self)

    def draw(self, display):
        display.blit(self.img, (self.rect.x, self.rect.y))
        #for pea in self.peas:
            #print("peas",pea)
            #pea.draw(display)
        
class Pea(Plant):
    #def __init__(self, game, x, y, speed=4, damage=5):
    def __init__(self, game, x, y, max_health, ui, speed=4, damage=5):
        super().__init__(game, (x,y), max_health, ui)
        self.game = game
        self.image = pygame.transform.scale(game.assets["projectiles"]["pea"], (50, 50)) 
        self.rect = self.image.get_rect()
        self.rect.x = x  
        self.rect.y = y
        self.speed = speed  
        self.damage = damage  

    def update(self):
        print("ja letuuuu")
        self.rect.x += self.speed
        self.check_collision()

    def check_collision(self):
        for zombie_list in self.ui.zombies:
            for zombie in zombie_list:
                if self.rect.colliderect(zombie.rect):
                    zombie.health -= self.damage
                    #random.choice(self.game.assets["sfx"]["splat"]).play()
                    if zombie.health <= 0:
                        zombie.kill()
                    
    def draw(self, display):
        print("horoch letyt", self.rect)
        display.blit(self.image, self.rect.topleft)#self.rect.topleft

        # якзо пулька торкнулась, щоб вона знакла, звук, урон
class Sunflower(Plant):
    #def __init__(self, game, pos, ui):
        #super().__init__(game, pos, ui)
    def __init__(self, game, pos, max_health, ui):
        super().__init__(game, pos, max_health, ui)
        self.cost = 50
        self.pos = pos
        self.health = 15
        self.game = game
        self.img = pygame.transform.scale(game.assets["plants"]["sunflower"], (75, 130))
        self.rect = self.img.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.reset_timer()

    def reset_timer(self):
        self.sun_timer = pygame.time.get_ticks()
        self.sun_timer_duration = random.randint(4500, 7000)

    def create_sun(self):
        return Sun("./images/sun.png", self.pos[0] + 15, self.pos[1] + 20, 1, (100, 65))

    def update(self, draw_pos, current_time, suns): # change hp, random timer
        if current_time >= self.sun_timer + self.sun_timer_duration:
            suns.append(self.create_sun())
            self.reset_timer()

    def draw(self, display):
        display.blit(self.img, self.pos)

#class Walnut(Plant):
    #def __init__(self, game, pos):
        #self.game = game
        #self.type = "walnut"
        #self.pos = pos
        #self.max_health = 30
        #self.health = 30
        #self.img = pygame.transform.scale(game.assets["plants"]["walnut"], (75, 130))

        #self.img = game.assets["plants"]["walnut"][0]

    #def update(self, draw_pos): # change hp
        #if self.health <= 20:
            #self.img = self.game.assets["plants"]["walnut"][1]
            #if self.health <= 10:
                #self.img = self.game.assets["plants"]["walnut"][2]

    #def draw(self, display, draw_pos):
        #display.blit(self.img, draw_pos)
