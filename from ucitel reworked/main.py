from zombies import *
from utils import *
from plants import *
import pygame, os, sys, time
from random import randint,choice
pygame.init()

FPS = 90
WINDOW_WIDTH = 1980
WINDOW_HEIGHT = 1080

#WINDOW_WIDTH = 1920
#WINDOW_HEIGHT = 1080

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Plants vs Zombies")
clock = pygame.time.Clock()

# class GameSprite(pygame.sprite.Sprite):
#     def __init__(self, file_name, x, y, speed, size = None):
#         super().__init__()#kopijuje vse schoje v super classu => pygame.sprite.Sprite
#         self.image = self.load_image(file_name, size)
#         self.rect = self.image.get_rect()
#         self.rect.x = x 
#         self.rect.y = y
#         self.speed = speed

#     def load_image(self, file_name, size = None):
#         img_path = os.path.join(os.path.abspath(__file__ + "/.."), file_name)
#         image = pygame.image.load(img_path).convert_alpha()
#         #vlastni rozmiry, netreba zadavaty
#         if not size:
#             size = image.get_rect()#original size
#             scaled_image = pygame.transform.scale(image, size)
#         else:
#             scaled_image = pygame.transform.scale(image, size)#mashtabujem
#         return scaled_image

#     #maluvanya objektu
#     def draw(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

class Assets():
    def __init__(self):
        pygame.mixer.init()
        self.display = pygame.Surface((320, 180))
        self.assets = {
            "plants":{
                "peashooter":pygame.image.load(find_resource("./images/plants/peashooter.png")),
                "sunflower":pygame.image.load(find_resource("./images/plants/sunflower.png")),
                # "walnut":[pygame.image.load(find_resource("./images/plants/walnut.png")).subsurface((0,0,16,32)),
                #         pygame.image.load(find_resource("./images/plants/walnut.png")).subsurface((16,0,16,32)),
                #         pygame.image.load(find_resource("./images/plants/walnut.png")).subsurface((32,0,16,32))]
            },
            "seeds":{ # ui for plants
                "peashooter":pygame.image.load(find_resource("./images/seeds/peashooter.png")),
                "sunflower":pygame.image.load(find_resource("./images/seeds/sunflower.png")),
                "walnut":pygame.image.load(find_resource("./images/seeds/walnut.png"))
            },
            "zombies":{
                "ripboi":pygame.image.load(find_resource("./images/zombies/ripboi.png"))
            },
            "projectiles":{ # goroh
                "pea":pygame.image.load(find_resource("./images/projectiles/pea.png"))
            },
            "sun":pygame.image.load(find_resource("./images/sun.png")),
            "sfx":{ #sound effects 
                "plant":pygame.mixer.Sound(find_resource("./sound effects/plant.ogg")),
                "splat":pygame.mixer.Sound(find_resource("./sound effects/splat.ogg")),
                "gulp":pygame.mixer.Sound(find_resource("./sound effects/gulp.ogg")),
                "chomp":pygame.mixer.Sound(find_resource("./sound effects/chomp.ogg")),
                "throw":pygame.mixer.Sound(find_resource("./sound effects/throw.ogg")),
                "losemusic":pygame.mixer.Sound(find_resource("./sound effects/losemusic.ogg")),
                "losescream":pygame.mixer.Sound(find_resource("./sound effects/scream.ogg")),
                "seedlift":pygame.mixer.Sound(find_resource("./sound effects/seedlift.ogg")),
                "buzzer":pygame.mixer.Sound(find_resource("./sound effects/buzzer.ogg")),
                "points":pygame.mixer.Sound(find_resource("./sound effects/points.ogg"))
            }
        }

assets = Assets()

class UI():
    def __init__(self):
        self.plant_num = 1
        self.grid = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]
        self.plants = []
        self.suns = [] # [0,"asd", 222], "asdsadasdasds"
        self.interface = []
        self.zombies = [[],[],[],[],[]]
        self.peas = []
        self.create_plants()
        self.create_interface()

        
    # def run(self): # ui + клітинки
    #     pass
    def create_interface(self):
        self.interface.append(Interface_seeds(assets.assets["sun"], 160, 80, 0,(80,75)))
        self.interface.append(Interface_seeds(assets.assets["seeds"]["sunflower"], 460, 50, 1,(100,125)))
        self.interface.append(Interface_seeds(assets.assets["seeds"]["peashooter"], 580, 50, 2,(100,125)))
        #self.interface.append(Interface_seeds(assets.assets["seeds"]["walnut"], 700, 50, 2,(100,125)))
        #GameSprite(file_name = assets["seeds"]["sunflower"], (254, 4, 0, 50))
        #GameSprite(file_name = assets["seeds"]["walnut"], (262, 4, 0, 50))


    def draw_plants(self, display):
        for plant in self.plants:
            plant.draw(display)

    def create_plants(self):
        # GREEN = (0, 255, 0)
        offset_X = 470
        offset_Y = 275
        column_gap = 2
        row_gap = 25
        #offset_X = 700
        #offset_Y = 150
        GRID_size = 113
        GRID_columns = 9 
        GRID_rows = 5
        for row in range(GRID_rows):
            for column in range(GRID_columns):
                # rect = pygame.Rect(column * GRID_size, row * GRID_size, GRID_size, GRID_size)
                # pygame.draw.rect(window, GREEN, rect, 1)
                if self.grid[row][column] == 1:
                    x_position = column * GRID_size + offset_X + column_gap * column
                    y_position = row * GRID_size + offset_Y + row_gap * row
                    self.plants.append(Sunflower(assets, (x_position, y_position), 15, ui))
                elif self.grid[row][column] == 2:
                    x_position = column * GRID_size + offset_X + column_gap * column
                    y_position = row * GRID_size + offset_Y + row_gap * row
                    self.plants.append(Peashooter(assets, (x_position, y_position), 15, ui))
                #elif self.grid[row][column] == 3:
                    #x_position = column * GRID_size + offset_X + column_gap * column
                    #y_position = row * GRID_size + offset_Y + row_gap * row
                    #self.plants.append(Walnut(assets, (x_position, y_position)))
                    # window.blit(Sunflower(assets, ), (column * GRID_size, row * GRID_size))
                #elif self.grid[row][column] == 2:
                    #self.plants.append(Peashooter(assets, (column * GRID_size + offset_X, row * GRID_size + offset_Y)))
                #elif self.grid[row][column] == 2:
                    #x_position = column * GRID_size + offset_X + column_gap * column
                    #y_position = row * GRID_size + offset_Y + row_gap * row
                    #self.plants.append(Peashooter(assets, (x_position, y_position)))
                # elif self.grid[row][column] == 3:
                #     window.blit(Walnut, (column * GRID_size, row * GRID_size))

BLACK = (0,0,0)
suns = 500
text_count_suns = pygame.font.Font(None, 40).render(str(suns), True, BLACK)

def get_grid_position(mouse_pos, GRID_size):
    x, y = mouse_pos
    #print(x, y)
    column = (x - 470) // GRID_size
    row = (y - 370) // GRID_size
    #print(row, column)
    return row, column        

    
    

    # def dead(self, zombie):
    #     running = True
    #     self.rect.x += self.speed
    #     if self.rect.x > WINDOW_WIDTH:
    #         dead_text_1 = self.font32.render("THE ZOMBIES ATE UR BRAIN!", False, (50, 255, 50))
    #         dead_text_1_rect = dead_text_1.get_rect()

    #     while running:
    #         zombie.draw(self.display)
    #         self.display.blit(dead_text_0, dead_text_1_rect)

#music
pygame.mixer.music.load("./music/grasswalk.mp3")
pygame.mixer.music.play(-0, 0, 100)
pygame.mixer.music.set_volume(0.3)

ui = UI()

GREEN = (0, 255, 0)

#text_loose = pygame.font.Font("/Users/Maria/OneDrive2/OneDrive/Desktop/Projekty/zavdanya pray for python/Final/PvZ like game/data(veci)/idkfont.ttf", 32).render(f"U LOOSE", True, GREEN)
#text_loose_pos = pygame.font.Font("/Users/Maria/OneDrive2/OneDrive/Desktop/Projekty/zavdanya pray for python/Final/PvZ like game/data(veci)/idkfont.ttf", 32).render(f"U LOOSE", True, GREEN)

backyard = GameSprite.load_image(None, "./images/backyard/background6ed.png", (WINDOW_WIDTH, WINDOW_HEIGHT))
finish = False

start_time = pygame.time.get_ticks()
current_time = pygame.time.get_ticks()
seconds = 1

while True:
    window.blit(backyard, (100,0))
    ui.draw_plants(window)
    window.blit(text_count_suns, (325, 110))
    # window.blit(text_loose, (10, 10))
    # window.blit(text_loose_pos, (10, 10))
    

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= 1000:
        start_time = current_time
        seconds += 1
    
    # True 1 100 -20
    # False 0 
    # 6 % 3 = 0
    #if not seconds % 10: #кожні 3 секунди  10 % 3 = 3 + 3 + 3 + 1  

    if not seconds % 3:
        lane = random.randint(0,4)
        ui.zombies[lane].append(Zombies(assets, "ripboi", lane, ui))
        seconds = 1
    for plant in ui.plants: 
        #if Sunflower: #перевірка що ця росни це соняшник
        if isinstance(plant,Sunflower):
            if current_time - plant.sun_timer >= plant.sun_timer_duration:
                ui.suns.append(plant.create_sun())
                plant.reset_timer()
        if isinstance(plant, Peashooter):
            plant.update(pygame.time.get_ticks()) 
            plant.draw(window)
    for pea in ui.peas:
        pea.draw(window)
        pea.update()   
        if pea.rect.x > 1980:
            ui.peas.remove(pea) 

    for interface in ui.interface:
        interface.draw()
        if interface.rect.collidepoint(pygame.mouse.get_pos()):
            ui.plant_num = interface.plant_num

    for zombie_list in ui.zombies:    
        for zombie in zombie_list:
            zombie.update()
            zombie.draw(window)

    for sun in ui.suns:
        if sun.rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                #random.choice(assets.assets["sfx"]["seedlift"]).play()
                suns += 100
                text_count_suns = pygame.font.Font(None, 40).render(str(suns), True, BLACK)
                ui.suns.remove(sun)
        sun.draw(window)
        sun.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_grid_position(mouse_pos, GRID_size = 113)
            if col <= 8 and col >=0 and row >= 0 and row <= 4 :
                #if ui.grid[row][col] = 0:
                    if ui.plant_num == 1 and suns >= 50:
                        ui.grid[row][col] = ui.plant_num
                        suns -= 50
                    elif ui.plant_num == 2 and suns >= 100:
                        ui.grid[row][col] = ui.plant_num
                        suns -= 100
                    ui.plants = []
                    ui.create_plants()
                    text_count_suns = pygame.font.Font(None, 40).render(str(suns), True, BLACK)
                   
                #elif ui.grid[row][col] = 2:
                    #ui.plants = []
                    #ui.create_plants()



    #if not finish:
        #text_count_suns = pygame.font.Font(None, 40).render(f"Пропущено {passed}", True, GREY)
        #zombies.update()
        #zombies.draw(window)
        #plants.update()
        #plants.draw()
        #bullets.draw(window)
        #bullets.update()

    pygame.display.update()
    clock.tick(FPS)

        



# обрізати фон (je)
# поправити одночасний спавн сонячок (je)
# 172 рядок if (je)
# для self.grid, робити заповнення клітинок, в залежності від положення кліка мишки (je)
