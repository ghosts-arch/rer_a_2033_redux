from typing import Tuple

import pygame
from entity import Entity
from settings import ENEMY_TOTAL_LIFE, ENEMY_WIDTH, RED


class Enemy(Entity):

    def __init__(
        self,
        left: float,
        top: float,
        width: float,
        height: float,
        color: Tuple[int, int, int],
        speed: int,
    ) -> None:
        super().__init__(left, top, width, height, color)
        self.lifebar = pygame.Rect(left, top - 15, width, 5)
        self.speed = speed
        self.life = ENEMY_TOTAL_LIFE

    def update(self):
        self.lifebar.width = (
            ((self.life * 100) / ENEMY_TOTAL_LIFE) * ENEMY_WIDTH
        ) / 100
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect)
        pygame.draw.rect(pygame.display.get_surface(), RED, self.lifebar)

    def move_right(self) -> None:
        self.rect.move_ip(self.speed, 0)
        self.lifebar.move_ip(self.speed, 0)
