import pygame, os, sys


pygame.init()

main_directory = os.path.dirname(__file__)
images_directory = os.path.join(main_directory, "images")

width = 700
height = 700

player_x_sprite = 0
player_y_sprite = 0

player_x_pos = 500
player_y_pos = 500

run = True

tile_size = 35

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platform game")

class World:
    def __init__(self, data):
        self.tiles_list = []

        tile_spritesheet = pygame.image.load(os.path.join(images_directory, "tiles_spritesheet.png"))
        img_grass = tile_spritesheet.subsurface(0,0,64,64)
        img_wall = tile_spritesheet.subsurface(0,64,64,64)

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    wall = pygame.transform.scale(img_wall, (tile_size, tile_size))
                    wall_rect = wall.get_rect()
                    wall_rect.x = col_count * tile_size
                    wall_rect.y = row_count * tile_size
                    tile = (wall, wall_rect)
                    self.tiles_list.append(tile)
                if tile == 2:
                    grass = pygame.transform.scale(img_grass, (tile_size, tile_size))
                    grass_rect = grass.get_rect()
                    grass_rect.x = col_count * tile_size
                    grass_rect.y = row_count * tile_size
                    tile = (grass, grass_rect)
                    self.tiles_list.append(tile)
                col_count += 1
            row_count += 1
    
    def draw(self):
        for tile in self.tiles_list:
            window.blit(tile[0], tile[1])


world_data = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,1],
]

def draw_grid():
    for line in range(0,12):
        pygame.draw.line(window, (0,0,0), (0, line * tile_size), (width, line * tile_size))
        pygame.draw.line(window, (0,0,0), (line * tile_size, 0), (line * tile_size, height))

player_spritesheet = pygame.image.load(os.path.join(images_directory, "Player_spritesheet.png"))

w = World(world_data)

while run:
    os.system("cls")
    window.fill((175,175,255))
    w.draw()

    player_frame = player_spritesheet.subsurface(32 * int(player_x_sprite), 32 * int(player_y_sprite), 32, 32)
    player_frame = pygame.transform.scale(player_frame, (40, 40))
    player_rect = player_frame.get_rect(center=(player_x_pos, player_y_pos))
    
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if keys[pygame.K_d]:
            player_y_sprite = 0

            if player_x_sprite >= 4:
                player_x_sprite = 0
            else:
                player_x_sprite += 0.75
                
        if keys[pygame.K_a]:
            player_y_sprite = 1
                
            if player_x_sprite >= 4:
                player_x_sprite = 0
            else:
                player_x_sprite += 0.75
            
    window.blit(player_frame, player_rect)
    pygame.display.flip()
