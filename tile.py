from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Set
import pygame


class Dir(Enum):
    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)

    def __neg__(self):
        if self == Dir.left:
            return Dir.right
        if self == Dir.right:
            return Dir.left
        if self == Dir.up:
            return Dir.down
        if self == Dir.down:
            return Dir.up


directions = (Dir.left, Dir.right, Dir.up, Dir.down)


class Tile:
    def __init__(self, id: int, can_attach: Dict[Dir, List[int]]):
        self.id = id
        self.can_attach = can_attach
        self.image = pygame.image.load(f"tiles/{id}.png")


@dataclass
class Empty:
    can_be: Set[int]
    image: pygame.Surface = pygame.image.load("tiles/25.png")


tile_list = [
    Tile(0, {
        Dir.left: [0, 4],
        Dir.right: [0, 2],
        Dir.up: [0, 1],
        Dir.down: [0, 3]
    }),
    Tile(1, {
        Dir.left: [1, 8, 12],
        Dir.right: [1, 5, 9],
        Dir.up: [3, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [0]
    }),
    Tile(2, {
        Dir.left: [0],
        Dir.right: [4, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [2, 5, 9],
        Dir.down: [2, 6, 10]
    }),
    Tile(3, {
        Dir.left: [3, 7, 11],
        Dir.right: [3, 6, 10],
        Dir.up: [0],
        Dir.down: [1, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(4, {
        Dir.left: [2, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [0],
        Dir.up: [4, 8, 12],
        Dir.down: [4, 7, 11]
    }),
    Tile(5, {
        Dir.left: [1],
        Dir.right: [7, 8, 13, 14, 20, 23, 25],
        Dir.up: [6, 7, 13, 16, 19, 24, 25],
        Dir.down: [2]
    }),
    Tile(6, {
        Dir.left: [3],
        Dir.right: [7, 8, 13, 14, 20, 23, 25],
        Dir.up: [2],
        Dir.down: [5, 8, 14, 15, 21, 24, 25]
    }),
    Tile(7, {
        Dir.left: [5, 6, 15, 16, 22, 23, 25],
        Dir.right: [3],
        Dir.up: [4],
        Dir.down: [5, 8, 14, 15, 21, 24, 25]
    }),
    Tile(8, {
        Dir.left: [5, 6, 15, 16, 22, 23, 25],
        Dir.right: [1],
        Dir.up: [6, 7, 13, 16, 19, 24, 25],
        Dir.down: [4]
    }),
    Tile(9, {
        Dir.left: [1],
        Dir.right: [11, 12, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [10, 11, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [2]
    }),
    Tile(10, {
        Dir.left: [3],
        Dir.right: [11, 12, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [2],
        Dir.down: [9, 12, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(11, {
        Dir.left: [9, 10, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [3],
        Dir.up: [4],
        Dir.down: [9, 12, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(12, {
        Dir.left: [9, 10, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [1],
        Dir.up: [10, 11, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [4]
    }),
    Tile(13, {
        Dir.left: [5, 6, 15, 16, 22, 23, 25],
        Dir.right: [4, 11, 12, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [3, 10, 11, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [5, 8, 14, 15, 21, 24, 25]
    }),
    Tile(14, {
        Dir.left: [5, 6, 15, 16, 22, 23, 25],
        Dir.right: [4, 11, 12, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [6, 7, 13, 16, 19, 24, 25],
        Dir.down: [1, 9, 12, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(15, {
        Dir.left: [2, 9, 10, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [7, 8, 13, 14, 20, 23, 25],
        Dir.up: [6, 7, 13, 16, 19, 24, 25],
        Dir.down: [1, 9, 12, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(16, {
        Dir.left: [2, 9, 10, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [7, 8, 13, 14, 20, 23, 25],
        Dir.up: [3, 10, 11, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [5, 8, 14, 15, 21, 24, 25]
    }),
    Tile(17, {
        Dir.left: [2, 9, 10, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [4, 11, 12, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [3, 10, 11, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [1, 9, 12, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(18, {
        Dir.left: [2, 9, 10, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [4, 11, 12, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [3, 10, 11, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [1, 9, 12, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(19, {
        Dir.left: [2, 9, 10, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [4, 11, 12, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [3, 10, 11, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [5, 8, 14, 15, 21, 24, 25]
    }),
    Tile(20, {
        Dir.left: [5, 6, 15, 16, 22, 23, 25],
        Dir.right: [4, 11, 12, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [3, 10, 11, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [1, 9, 12, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(21, {
        Dir.left: [2, 9, 10, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [4, 11, 12, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [6, 7, 13, 16, 19, 24, 25],
        Dir.down: [1, 9, 12, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(22, {
        Dir.left: [2, 9, 10, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [7, 8, 13, 14, 20, 23, 25],
        Dir.up: [3, 10, 11, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [1, 9, 12, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(23, {
        Dir.left: [5, 6, 15, 16, 22, 23, 25],
        Dir.right: [7, 8, 13, 14, 20, 23, 25],
        Dir.up: [3, 10, 11, 14, 15, 17, 18, 20, 21, 22, 23],
        Dir.down: [1, 9, 12, 13, 16, 17, 18, 19, 20, 22, 23]
    }),
    Tile(24, {
        Dir.left: [2, 9, 10, 13, 14, 17, 18, 19, 20, 21, 24],
        Dir.right: [4, 11, 12, 15, 16, 17, 18, 19, 21, 22, 24],
        Dir.up: [6, 7, 13, 16, 19, 24, 25],
        Dir.down: [5, 8, 14, 15, 21, 24, 25]
    }),
    Tile(25, {
        Dir.left: [5, 6, 15, 16, 22, 23, 25],
        Dir.right: [7, 8, 13, 14, 20, 23, 25],
        Dir.up: [6, 7, 13, 16, 19, 24, 25],
        Dir.down: [5, 8, 14, 15, 21, 24, 25]
    })
]
