import pygame


grass = pygame.image.load('assets/tiles/grass.png')
dirt = pygame.image.load('assets/tiles/dirt.png')
# 2 = grass, 1 = dirt, 0 = air

game_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
]

tile_rects = []
TILE_SIZE = 16

def draw_map(screen):
    global game_map
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == 1:
                screen.blit(dirt, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == 2:
                screen.blit(grass, (x * TILE_SIZE, y * TILE_SIZE))
            if tile != 0:
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

def collision_test(player, tiles):
    hit_list = []
    for tile in tiles:
        if player.colliderect(tile):
            hit_list.append(tile)
    print(hit_list)
    return hit_list


def move(player, movement):
    global delta_y
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    hit_list = collision_test(player, tile_rects)

    player.x += movement[0]
    for tile in hit_list:
        if movement[0] > 0:
            player.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            player.left = tile.right
            collision_types['left'] = True
    if collision_types['top'] == True:
        movement[1] = 0
    
    player.y += movement[1]
    for tile in hit_list:
        if movement[1] > 0:
            player.bottom = tile.top + 1
            collision_types['bottom'] = True
            delta_y = 0
        elif movement[1] < 0:
            player.top = tile.bottom
            collision_types['top'] = True

    return player, collision_types