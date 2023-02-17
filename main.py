from generate import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


def draw_image(li: List[List[Union[Empty, Tile]]]):
    for i, row in enumerate(li):
        for j, value in enumerate(row):
            value.image.convert_alpha()
            rect = value.image.get_rect(topleft=(j * 16, i * 16))
            screen.blit(value.image, rect)


def run():
    li = init()
    start = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_ESCAPE:
                return
            if event.key == pygame.K_RETURN:
                li = init()
                start = True

        screen.fill((0, 100, 0))

        if start:
            if (pos := find_least_entropy(li)) != (-1, -1):
                x, y = pos
                prev = copy(li[y][x])
                li[y][x] = tile_list[choice([*li[y][x].can_be])]
                if not propagation(li, x, y):
                    li[y][x] = prev
            draw_image(li)
        pygame.display.update()

        clock.tick(60)


run()
