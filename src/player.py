from typing import Tuple
import pygame
from abc import ABC

Dimensions = Tuple[int, int]


class Entity(ABC):
    def __init__(
        self,
        left: float,
        top: float,
        width: float,
        height: float,
        color: pygame.Color,
    ) -> None:
        self.rect: pygame.Rect = pygame.Rect(left, top, width, height)
        self.color: pygame.Color = color

    def update(self) -> None:
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect)


class Player(Entity):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: pygame.Color,
        speed: int,
    ) -> None:
        super().__init__(left=x, top=y, width=width, height=height, color=color)
        self.speed = speed

    def move_left(self) -> None:
        self.rect.move_ip(-self.speed, 0)

    def move_right(self) -> None:
        self.rect.move_ip(self.speed, 0)
