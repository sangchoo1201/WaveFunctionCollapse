from random import randrange, choice, random
from tile import *
from typing import Union, Tuple
from copy import copy


def init() -> List[List[Union[Empty, Tile]]]:
    li: List[List[Union[Empty, Tile]]] = [[Empty({*range(26)}) for _ in range(40)] for _ in range(30)]

    ix, iy = randrange(40), randrange(30)
    li[iy][ix] = choice(tile_list)
    propagation(li, ix, iy)
    return li


def propagation(li: List[List[Union[Empty, Tile]]], px: int, py: int) -> bool:
    tile = li[py][px]
    if type(tile) is not Tile:
        return False
    changes = []
    for direction in directions:
        dx, dy = direction.value
        nx, ny = dx + px, dy + py
        if not (0 <= nx < 40 and 0 <= ny < 30):
            continue
        new_tile = li[ny][nx]
        if type(new_tile) is not Empty:
            continue
        new_selection = new_tile.can_be & {*tile.can_attach[direction]}
        if not new_selection:
            return False
        changes.append((nx, ny, new_selection))
    for change in changes:
        nx, ny, new_selection = change
        li[ny][nx].can_be = new_selection
    return True


def find_least_entropy(li: List[List[Union[Empty, Tile]]]) -> Tuple[int, int]:
    mx, my = -1, -1
    min_value = float("inf")
    for i, row in enumerate(li):
        for j, value in enumerate(row):
            if type(value) is not Empty:
                continue
            key = len(value.can_be) + random()
            if key < min_value:
                mx, my = j, i
                min_value = key
    return mx, my


def main():
    li = init()
    while (pos := find_least_entropy(li)) != (-1, -1):
        x, y = pos
        prev = copy(li[y][x])
        li[y][x] = tile_list[choice([*li[y][x].can_be])]
        if not propagation(li, x, y):
            li[y][x] = prev
    for row in li:
        print(f"[{','.join(map(lambda tile: f'{tile.id:2d}', row))}]")


if __name__ == '__main__':
    main()
